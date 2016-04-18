#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re

PREFIX_TMPL="""
<script src="assets/lib/lesson.js"></script>

<link rel="stylesheet" type="text/css" href="assets/css/lesson.css">
%s
<audio id="chd-wort" src=""></audio>"""

EXPLANATION1="""
<script>
var wordList=[%s]
</script>
<p>Lesen Sie die folgenden Wörter auf Schweizerdeutsch, indem Sie die Umformungsregeln anwenden.
<br>Wenn Sie das Schweizerdeutsche Wort hören wollen, klicken Sie darauf.</p>
<p class="wrap" id="play_all" onclick="playAudioAll(this, wordList)">
  Play All
  <button class="gcb-button-speaker">
  <img src="assets/img/speaker_icon16.png" style="vertical-align:middle">
  </button>
</p>

"""

EXPLANATION2="""<p>
  Lesen Sie die folgenden Wörter auf Schweizerdeutsch, indem Sie die Umformungsregeln anwenden.
  <br/>Wenn Sie mit der Maus auf das Wort gehen, wird die Stelle markiert die Sie umformen müssen.
  <br/>Wenn Sie das Schweizerdeutsche Wort hören wollen, klicken Sie darauf.</p>
  
"""

PREFIX1 = '' 
PREFIX2 = PREFIX_TMPL % EXPLANATION2

def eliminate_junk(old):
    old = re.sub("<\!\-\-(.|[\r\n])*?\-\->", "", old, re.MULTILINE)
    old = old.replace('&quot;', '\'')
    old = old.replace('yellow', 'orange')
    old = old.replace('#FFC000', 'orange')
   
 #   old = old.replace('<p class="MsoNormal">', '<p>')
 #   old = old.replace('class="MsoNormal" ', '')
   

  #  old = old.replace('lang="DE" ', '')
   
   # old = old.replace('<o:p>', '')
    #old = old.replace('</o:p>', '')
    old = eliminate_newlines(old)
    old = old.replace("""<span style="font-size:20.0pt;font-family:\'Sylfaen\',\'serif\';
    background:orange\">""", '<span style=\"background:orange\">')
    old = old.replace("""<span style="font-size:20.0pt;font-family:'Sylfaen','serif'">""", '<span>')
    #old = old.replace("""<span style="font-size:20.0pt;font-family:
    #'Sylfaen','serif'">""", '<span>')
    old = old.replace("""<span lang=DE style='font-size:20.0pt;font-family:"Sylfaen","serif"'>""", "<span>")
    old = re.sub('[\r\n\s;\"]mso-[^\"\;]*', "", old)


    
    #newer word version
    old = old.replace('<p class=MsoNormal>', '<p>')
    old = old.replace("background:transparent", "background:orange")
    old = old.replace("background:\r\ntransparent", "background:orange")
    old = old.replace("background:white", "background:orange")

    old = old.replace('class=MsoNormal ', '')
    old = old.replace('lang=DE ', '')
    old = old.replace('lang=DE\r\n', '')
    old = old.replace("""<span style='font-size:20.0pt;font-family:"Sylfaen","serif"'>""", "<span>")
    old = old.replace("<p style='background:orange'>", '<p>')
    old = old.replace('<tr>', '<tr id="de">')
    old = old.replace("""<span style='font-size:20.0pt;font-family:"Sylfaen","serif";background:orange'>""", "<span style='background:orange'>")
    # these variants are now probably unnecessary, as we eliminated the newlines
    old = old.replace("""<span\r\nstyle='font-size:20.0pt;font-family:"Sylfaen","serif";background:orange'>""", "<span style='background:orange'>")
    old = old.replace("""<span style='font-size:20.0pt;\r\nfont-family:"Sylfaen","serif";background:orange'>""", "<span style='background:orange'>")
    old = old.replace("""<span style='font-size:24.0pt;font-family:"Sylfaen","serif";\r\nbackground:orange'>""", "<span style='background:orange'>")
    old = old.replace("""<span style='font-size:20.0pt;font-family:"Sylfaen","serif";\r\nbackground:orange'>""", "<span style='background:orange'>")
    old = old.replace("""<span style='font-size:\r\n20.0pt;font-family:"Sylfaen","serif";background:orange'>""", "<span style='background:orange'>")
    old = old.replace("""<span style='font-size:20.0pt;\r\nfont-family:"Sylfaen","serif"'>""", "<span>")
    old = old.replace("""<span\r\nstyle='font-size:20.0pt;font-family:"Sylfaen","serif"'>""", "<span>")
    old = old.replace("""<span style='font-size:\r\n20.0pt;font-family:"Sylfaen","serif"'>""", "<span>")
    old = old.replace("<p><span>&nbsp;</span></p>", "")
    old = old.replace("<p><span style='background:orange'>&nbsp;</span></p>", "")
    old = old.replace("""<p><span style='font-size:24.0pt;font-family:"Sylfaen","serif"'>&nbsp;</span></p>""", "")
    old = old.replace("""<span\r\nstyle='background:orange'>""", "<span style='background:orange'>")
    #parts = re.split('<p><span>&nbsp;</span></p>', old)
    #old = """\n\n\n<table width="100%" border="0">\n<tbody><tr><td width="50%" border="0">""" + parts[0] + '</td><td>' + parts[len(parts)-1] + '</td></tr></tbody></table>'
    print "AFter junk is:\n" + old
    return old
    

def eliminate_newlines(str):
  """
  Eliminates the unnecessary newlines from the HTML file. Only the newlines outside of <p> elements are left
  """
  in_p = 0
  new = ''
  for i in range(0, len(str)-7):
    if in_p == 0 or (str[i] != '\r' and str[i]!='\n'):
      new += str[i]
    elif in_p > 0 and str[i] == '\r' and str[i-1] != ';' and str[i-1]!=':':
      new +=' '
    if str[i] == '<' and str[i+1] == 'p':
      in_p+=1
    elif str[i]=='<' and str[i+1] == '/' and str[i+2] == 'p' and str[i+3] == '>':
      in_p-=1
  return new

def create_highlighted_wordlist1(old):
	words = open('wordlist.txt', 'r')
	explanation = EXPLANATION1 % ", ".join([('"' + word.rstrip() + '"') for word in words if word.rstrip()])
	global PREFIX1
	PREFIX1 = PREFIX_TMPL % explanation
	new = '<div style="border:solid windowtext 1.0pt; padding:1.0pt 4.0pt 1.0pt 4.0pt" class="yui-wk-div">'
	new += '<table style="width:100%;border:0"><tbody>'
	isFirstRow = True
	for line in old.splitlines():
	  if line.startswith('<p><span>') or line.startswith("<p><span style='background:orange'>"):
	    if isFirstRow:
	      new +=  '\n<tr id = "de">'
	    new += '\n\t<td style="width:50%;border:0">'+line+'</td>'
	    if  not isFirstRow:
	      new += '</tr>'
	    isFirstRow =  not isFirstRow
	old = new + '</tbody></table></div>'
	
	old = old.replace("<p><span style='background:orange'>", '<p><span class="wrap" id="to_be_replaced" onclick="playAudio(this)"><span style="background:orange">')
	old = old.replace('</span></p>', """</span>
  <button style="float:right" class="gcb-button-speaker noshow">
  <img style="vertical-align:middle" src="assets/img/speaker_icon16.png">
  </button>
</p>""")
	old = old.replace('<p><span>', '<p><span class="wrap" id="to_be_replaced" onclick="playAudio(this)"><span>')
	old = old.replace('</span></p>', """
</span>
  <button style="float:right" class="gcb-button-speaker noshow">
  <img style="vertical-align:middle" src="assets/img/speaker_icon16.png">
  </button>
</p>""")
	words = open('wordlist.txt', 'r')    
	for word in words:
	  word = word.rstrip()
	  if not word:
		continue
	  old = old.replace('to_be_replaced', word, 1)
	return old

def create_highlighted_wordlist2(old):
  words = open('wordlist.txt', 'r')
  new = '<div style="border:solid windowtext 1.0pt; padding:1.0pt 4.0pt 1.0pt 4.0pt" class="yui-wk-div">'
  new += '<table style="width:100%;border:0"><tbody>'
  isFirstRow = True
  for line in old.splitlines():
    if line.startswith('<p><span>') or line.startswith("<p><span style='background:orange'>"):
  	  if isFirstRow:
	    new +=  '\n<tr id = "de">'
	  new += '\n\t<td style="width:50%;border:0">'+line+'</td>'
	  if  not isFirstRow:
	    new += '</tr>'
	  isFirstRow =  not isFirstRow
  old = new + '</tbody></table></div>'
  old = old.replace("<p><span style='background:orange'>", """<p class="wrap" id="to_be_replaced" onclick="playAudio(this)">
<span class="show">to_be_replaced</span>
<span class="noshow"><span style="background:orange">""")
  old = old.replace('<p><span>', '<p class="wrap" id="to_be_replaced" onclick="playAudio(this)"><span class="show">to_be_replaced</span><span class="noshow"><span>')
  old = old.replace('</span></p>', """
</span>
  <button style="float:right" class="gcb-button-speaker noshow">
  <img style="vertical-align:middle" src="assets/img/speaker_icon16.png">
  </button>
</p>""")
  words = open('wordlist.txt', 'r')
  for word in words:
    word = word.rstrip()
    if not word:
      continue
    print "Replacing word %s" % word
    old = old.replace('to_be_replaced', word, 2)
  return old
    
def generate_word_list(old):
  old = re.sub("<style>(.|[\r\n])*?<\/style>", "", old, re.MULTILINE)
  old = re.sub("<script>(.|[\r\n])*?<\/script>", "", old, re.MULTILINE)
  old = re.sub("<button(.|[\r\n])*?<\/button>", "", old, re.MULTILINE)
  old = old.replace("<span style='background:orange'>", '')
  old = old.replace('<span>', '')
  old = old.replace('<p>', '')
  old = old.replace('</span>', '')
  old = old.replace('</p>', '')
  old = old.replace('</div>', '')
  old = old.replace('</body>', '')
  old = old.replace('</html>', '')
  
  
  
  debug = open('debug.txt', 'w')
  debug.write(old)
  debug.close()
  old = old.replace('\r\n\r\n', '___')
  old = old.replace('\r\n', ' ')
  parts = old.split('___')
  new = ''
  for part in parts:
    if part and not part.strip().startswith('<'):
      new += part + '\n'
  
  wordlist = open('wordlist.txt', 'w')
  wordlist.write(new)
  wordlist.close() 
  