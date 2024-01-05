# Myoro 2023

import os
import sys
import re

def quit():
  print('Bad input')
  exit(1)

def validLink(link):
  if re.match(r'https://www\.youtube\.com/watch\?v=[\w-]+', sys.argv[i]) is not None:
    return True
  elif re.match(r'https://youtu\.be/[\w-]+', link) is not None:
    return True
  elif re.match(r'https://soundcloud\.com/[\w-]+/[\w-]+', link) is not None:
    return True
  else:
    return False

os.system('clear' if os.name == 'posix' else 'cls')

if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == '--help':
  print('A simple Python script to convert YouTube & SoundCloud links to MP3.\n')
  print('Usage:')
  print('1) scyt2mp3 OR scyt2mp3 --help')
  print('- Displays this screen')
  print('2) scyt2mp3 -l <link1> <link2> <linkN> -o <directory>')
  print('- Converts links to <directory> or the directory you are in if -o not specified')
  print('- Links accepted')
  print('   - youtu.be/...')
  print('   - youtube.com/...')
  print('   - soundcloud.com/<artist>/<song>')
  print('3) scyt2mp3 -t <file> -o <directory>')
  print('- Converts a file with links to <directory> or the directory you are in if -o not specified')
  print('- Links in the file must be seperated with line breaks, no commas allowed')

if len(sys.argv) == 2 or (len(sys.argv) > 2 and (sys.argv[1] != '-l' and sys.argv[1] != '-t')):
  quit()

# Grabbing links
links = []
if sys.argv[1] == '-l':
  for i in range(2, len(sys.argv)):
    if sys.argv[i] != '-d':
      if validLink(sys.argv[i]):
        links.append(sys.argv[i])
      else:
        quit()
    else:
      break
elif sys.argv[1] == '-t':
  print('text file')

print(links)