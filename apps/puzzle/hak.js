// This file was automatically generated from template.soy.
// Please don't edit this file by hand.

if (typeof puzzlepage == 'undefined') { var puzzlepage = {}; }


puzzlepage.messages = function(opt_data, opt_ignored, opt_ijData) {
  return '<div id="MSG" style="display: none"><span id="country1">澳大利亞</span><span id="country1Flag">flag_au.png</span><span id="country1FlagHeight">50</span><span id="country1FlagWidth">100</span><span id="country1Language">英語</span><span id="country1City1">墨爾本</span><span id="country1City2">悉尼</span><span id="country1HelpUrl">http://en.wikipedia.org/wiki/Australia</span><span id="country2">德國</span><span id="country2Flag">flag_de.png</span><span id="country2FlagHeight">60</span><span id="country2FlagWidth">100</span><span id="country2Language">德語</span><span id="country2City1">柏林</span><span id="country2City2">慕尼黑</span><span id="country2HelpUrl">http://en.wikipedia.org/wiki/Germany</span><span id="country3">中國</span><span id="country3Flag">flag_cn.png</span><span id="country3FlagHeight">66</span><span id="country3FlagWidth">100</span><span id="country3Language">中文</span><span id="country3City1">北京</span><span id="country3City2">上海</span><span id="country3HelpUrl">http://en.wikipedia.org/wiki/China</span><span id="country4">巴西</span><span id="country4Flag">flag_br.png</span><span id="country4FlagHeight">70</span><span id="country4FlagWidth">100</span><span id="country4Language">葡萄牙語</span><span id="country4City1">里約熱内盧</span><span id="country4City2">聖保羅</span><span id="country4HelpUrl">http://en.wikipedia.org/wiki/Brazil</span><span id="flag">旗幟</span><span id="language">語言</span><span id="languageChoose">選擇</span><span id="cities">城市</span><span id="error0">讚！\n%1 格仔全部正確。</span><span id="error1">差滴！有 1 格毋著。</span><span id="error2">%1 格毋著。</span><span id="tryAgain">加光个格仔毋著。\n繼續努力。</span></div>';
};


puzzlepage.start = function(opt_data, opt_ignored, opt_ijData) {
  return puzzlepage.messages(null, null, opt_ijData) + '<table id="header" width="100%"><tr><td valign="bottom"><h1><span id="title"><a href="../index.html">Blockly</a> : 迷局</span></h1></td><td><select id="languageMenu" onchange="BlocklyApps.changeLanguage();"></select>&nbsp; &nbsp;<button id="helpButton" onclick="Puzzle.showHelp(true);">幫助</button>&nbsp; &nbsp;<button id="checkButton" class="launch" onclick="Puzzle.checkAnswers();">核對答案</button></td></tr></table><script type="text/javascript" src="../../blockly_compressed.js"><\/script><script type="text/javascript" src="../../' + soy.$$escapeHtml(opt_ijData.langSrc) + '"><\/script><script type="text/javascript" src="blocks.js"><\/script><div id="blockly"></div><div id="shadow"></div><div id="helpBorder"></div><div id="help"><div style="padding-bottom: 0.7ex">每隻國家（青色），選擇其對應个旗幟，語言，與城市。</div><iframe src="help.html?lang=' + soy.$$escapeHtml(opt_ijData.lang) + '" style="height: 200px; width: 100%; border: none;"></iframe><div class="farSide" style="padding: 1ex 3ex 0"><button id="okButton" onclick="Puzzle.hideHelp(true)">確定</button></div></div>';
};


puzzlepage.help = function(opt_data, opt_ignored, opt_ijData) {
  return puzzlepage.messages(null, null, opt_ijData) + '<script type="text/javascript" src="../../blockly_compressed.js"><\/script><script type="text/javascript" src="../../' + soy.$$escapeHtml(opt_ijData.langSrc) + '"><\/script><script type="text/javascript" src="blocks.js"><\/script><div id="blockly"></div><div id="notouch"></div>';
};
