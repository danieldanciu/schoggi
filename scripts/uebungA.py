import re
import sys
import xml.etree.ElementTree

    
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
  text = text.replace('\n', '')
  text = text.replace('<p', '\n <p')
  scripts = re.compile(r'<script.*?/script>')
  css = re.compile(r'<style.*?/style>')
  
  text = text[text.find('<table '):]
  
  text = scripts.sub('', text)
  text = css.sub('', text)
  text = TAG_RE.sub('', text)
  print text.split('\n')
  return text.split('\n')

def main (argv=sys.argv):
  _, filename = argv
  f = open(filename)
  content = f.read()
  f.close()
  wordlist = remove_tags(content)
  content = content.replace('<p><span style="background: yellow;">', '<p><span style="background:yellow">')
  
  content = content.replace('<p><span>', '<p class="wrap" id=\'AUDIO_FILE\'  onclick="playAudio(this)">\n  ')
  content = content.replace('<p><span style="background:yellow">', '<p class="wrap" id=\'AUDIO_FILE\'  onclick="playAudio(this)">\n  <span style="background:yellow">')
  content = content.replace('</span></p>', 
"""
  <button style="float:right" class="gcb-button-author noshow">
  <img style="vertical-align:middle" src="assets/img/speaker_icon16.png">
  </button>
</p>""")
  for word in wordlist:
    word = word.replace(" ", "").lower()
    if not word:
      continue
    content = content.replace('AUDIO_FILE', word, 1)
  f = open(filename.split('.')[0] + '1.html', 'w')
  f.write("""
<style>
.wrap {
    height: 30px;
}
.noshow, .wrap:hover .show {
    display: none
}
.wrap:hover .noshow {
    display: block
}
</style>""")
  f.write(content)
  f.close()
  
if __name__ == "__main__":
    main()