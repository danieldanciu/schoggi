import re
import sys

    
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
  content = content.replace('yellow', 'orange')
  content = content.replace('<p><span style="background: orange;">', '<p><span style="background:orange">')
  
  content = content.replace('<p><span class="wrap">', '<p class="wrap" id=\'AUDIO_FILE\'  onclick="playAudio(this)">\n  ')
  content = content.replace('</span></span></p>',
"""
    <button style="float:right" class="gcb-button-author noshow">
      <img style="vertical-align:middle" src="assets/img/speaker_icon16.png">
    </button>
  </span>
</p> 
""")
  for word in wordlist:
    word = word.strip();
    word = word[:len(word)/2]
    word = word.replace(" ", "").lower()
    if not word:
      continue
    content = content.replace('AUDIO_FILE', word, 1)
  f = open(filename.split('.')[0] + '1.html', 'w')
  f.write(content)
  f.close()
  
if __name__ == "__main__":
    main()