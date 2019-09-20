from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
  text = uploaded[fn].decode()

# This looks for a file called "culinarypoisons.txt" 
# The text file's contents are stored in the variable "text."
with open('culinarypoisons.txt', 'r') as file:
    text = file.read()

import random

# In order to run TextBlob
import nltk
nltk.download('punkt')

# This parses the text file contents into a TextBlob oject called "blob"
from textblob import TextBlob
blob = TextBlob(text)

# This generates a ten-line poem by selecting a chunk of text
# and printing it one less word with each line.
countdown = 10
s = random.randint(0,len(wordlist))
for i in range(1,11):
  s += countdown + 1
  print(" ".join(wordlist[s:s+countdown]))
  countdown -= 1
