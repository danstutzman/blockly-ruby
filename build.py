#!/usr/bin/python
# Compresses the core Blockly files into a single JavaScript file.
#
# Copyright 2012 Google Inc.
# http://blockly.googlecode.com/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script generates two files:
#   blockly_compressed.js
#   blockly_uncompressed.js
# The compressed file is a concatenation of all of Blockly's core files which
# have been run through Google's Closure Compiler.  This is done using the
# online API (which takes a few seconds and requires an Internet connection).
# The uncompressed file is a script that loads in each of Blockly's core files
# one by one.  This takes much longer for a browser to load, but may be useful
# when debugging code since line numbers are meaningful and variables haven't
# been renamed.  The oncompressed file also allows for a faster developement
# cycle since there is no need to rebuild or recompile, just reload.

import httplib, json, os, urllib, sys

def import_path(fullpath):
  """
  Import a file with full path specification. Allows one to
  import from anywhere, something __import__ does not do.
  """
  path, filename = os.path.split(fullpath)
  filename, ext = os.path.splitext(filename)
  sys.path.append(path)
  module = __import__(filename)
  reload(module) # Might be out of date
  del sys.path[-1]
  return module


header = ('// Do not edit this file; automatically generated by build.py.\n'
          '"use strict";\n')

def gen_uncompressed():
  target_filename = 'blockly_uncompressed.js'
  f = open(target_filename, 'w')
  f.write(header)
  f.write("""if (!window.goog) {
  alert('Error: Closure not found.  Read this:\\n' +
        'http://code.google.com/p/blockly/wiki/Closure\\n');
}

""")
  calcdeps.PrintDeps(search_paths, [], f)
  f.write("""
// Load Blockly.
goog.require('Blockly');
""")
  f.close()
  print 'SUCCESS: ' + target_filename

def gen_compressed():
  target_filename = 'blockly_compressed.js'
  # Define the parameters for the POST request.
  params = [
      ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
      ('use_closure_library', 'true'),
      ('output_format', 'json'),
      ('output_info', 'compiled_code'),
      ('output_info', 'warnings'),
      ('output_info', 'errors'),
      ('output_info', 'statistics'),
    ]

  # Read in all the source files.
  filenames = calcdeps.CalculateDependencies(search_paths, ['core/blockly.js'])
  for filename in filenames:
    # Filter out the Closure files (the compiler will add them).
    if (filename.startswith('../')):
      continue
    f = open(filename)
    params.append(('js_code', ''.join(f.readlines())))
    f.close()

  # Send the request to Google.
  headers = { "Content-type": "application/x-www-form-urlencoded" }
  conn = httplib.HTTPConnection('closure-compiler.appspot.com')
  conn.request('POST', '/compile', urllib.urlencode(params), headers)
  response = conn.getresponse()
  json_str = response.read()
  conn.close

  # Parse the JSON response.
  json_data = json.loads(json_str)

  def file_lookup(name):
    if not name.startswith('Input_'):
      return '???'
    n = int(name[6:])
    return filenames[n]

  if json_data.has_key('errors'):
    errors = json_data['errors']
    for error in errors:
      print 'FATAL ERROR'
      print error['error']
      print '%s at line %d:' % (
          file_lookup(error['file']), error['lineno'])
      print error['line']
      print (' ' * error['charno']) + '^'
  else:
    if json_data.has_key('warnings'):
      warnings = json_data['warnings']
      for warning in warnings:
        print 'WARNING'
        print warning['warning']
        print '%s at line %d:' % (
            file_lookup(warning['file']), warning['lineno'])
        print warning['line']
        print (' ' * warning['charno']) + '^'
      print

    code = header + '\n' + json_data['compiledCode']

    stats = json_data['statistics']
    original_b = stats['originalSize']
    compressed_b = stats['compressedSize']
    if original_b > 0 and compressed_b > 0:
      f = open(target_filename, 'w')
      f.write(code)
      f.close()

      original_kb = int(original_b / 1024 + 0.5)
      compressed_kb = int(compressed_b / 1024 + 0.5)
      ratio = int(float(compressed_b) / float(original_b) * 100 + 0.5)
      print 'SUCCESS: ' + target_filename
      print 'Size changed from %d KB to %d KB (%d%%).' % (
          original_kb, compressed_kb, ratio)
    else:
      print 'UNKNOWN ERROR'

if __name__ == '__main__':
  try:
    calcdeps = import_path(
          '../closure-library-read-only/closure/bin/calcdeps.py')
  except ImportError:
    print """Error: Closure not found.  Read this:
http://code.google.com/p/blockly/wiki/Closure"""
    sys.exit(1)
  search_paths = calcdeps.ExpandDirectories(
      ['core/', '../closure-library-read-only/'])

  gen_uncompressed()
  gen_compressed()
