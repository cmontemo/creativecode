#installing weasyprint
!pip install weasyprint

#import needed elements
import string
import random
from weasyprint import HTML

#opening text file of Milton's Paradise Lost
#from Project Gutenberg - https://www.gutenberg.org/ebooks/20
#printing to a file
with open('paradise.txt') as f:
  n = f.read()

#replace all lowercase "s" with random number of "s" from 3 to 9
n = n.replace("s", "s" * random.randint(3,9))

#replace all capital "S" with "Sssss"
n = n.replace("S", "Sssss")


#from Zach Whalen's PrintingToPdfExample.ipynb
#https://colab.research.google.com/drive/1-xEMjJ-6zbzA_c8pqnQOKRVIe8Jwdwna
#add the novel into an HTML template
#<pre> allows original formatting of txt file

html_template = f"""
<html>
  <head>
  <title>Paradisssssse Losssssst</title>
  </head>
  <body>
  <pre>
  {n}
  </pre>
  </body>
</html>
"""

#this line saves that template as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("paradisssssse_novel.pdf")
