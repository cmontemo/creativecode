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

  
# Using this chunk of code instead of the above
# generates a poem that has 10 lines of randomly-selected chunks of words.

#seeed = random.randint(0,len(wordlist)-1)
#wordlist[seeed:seeed+5]
#line10=wordlist[seeed:seeed+10]
#print(" ".join(line10) )

# seed = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line1=wordlist[seed:seed+9]
#print(" ".join(line1) )

#seed1 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line2=wordlist[seed1:seed1+8]
#print(" ".join(line2) )

#seed2 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line3=wordlist[seed2:seed2+7]
#print(" ".join(line3) )

#seed3 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line4=wordlist[seed3:seed3+6]
#print(" ".join(line4) )

#seed4 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line5=wordlist[seed4:seed4+5]
#print(" ".join(line5) )

#seed5 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line6=wordlist[seed5:seed5+4]
#print(" ".join(line6) )

#seed6 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line7=wordlist[seed6:seed6+3]
#print(" ".join(line7) )

#seed7 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line8=wordlist[seed7:seed7+2]
#print(" ".join(line8) )

#seed8 = random.randint(0,len(wordlist)-1)
#wordlist[seed:seed+5]
#line9=wordlist[seed8:seed8+1]
#print(" ".join(line9) )


# Old code
# If you run this, it selects a 10-word chunk of text
# and prints the same line, removing another word each time.

#from textblob import TextBlob
#blob = TextBlob(text)
#poison = blob.words[random.randint(0,400)]

#n = random.randint(0,30000)
#randomWord = wordlist[n]

#c =  10
#for i in range(10):
  
# print (" ".join(wordlist[n:n+c]))
#   c -= 1
