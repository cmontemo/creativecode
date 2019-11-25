# Two Novels

This project folder contains two novels that I generated, both of which follow the parameters outlined by [NaNoGenMo](http://nanogenmo.github.io). 

## Paradissssse Lossssst ("serpent-ify")
This novel is generated using Python (which I find appropriate given the theme).  Using the Plain Text file from [Project Gutenberg,](https://www.gutenberg.org/ebooks/20) this code replaces every lowercase "s" with at least 3 to at most 9 "s's" (creating random degrees of snakiness with each generation) and replaces every uppercase "S" with "Sssss."  With this program, I reflect upon what it would be like for the Serpent to tell Milton's tale.  It gives a very distinct sense of narration and impacts the tone and mood of the piece.

In the future, I'd like to apply additional "s's" that would coincide with different ssstressssssssesssss on words.  I think that this method of transforming a text would be entertaining if applied to other works.

## Student Panoptic ("student-ify")
This novel using Python code adds chunks of interruptions after certain words of an academic text.  I started with the text of Michel Foucault's chapter in Discipline and Punish about the [Panopticon] (https://foucault.info/documents/foucault.disciplineAndPunish.panOpticism/) and ran it through a [script](https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0) that extracted and listed the most common words of the work.  I selected 50 words that usually trigger confusion or lack of focus, which I can credibly do based on my status as an anthropology major who has read Foucault for various daily readings and essays. I listed these words and added different sections of random thoughts (ones that I sometimes have when doing a challenging reading) that were in some way related to their respective Foucauldian word. I kept the formatting of the generated PDF as a large chunk of text to emphasize a stream-or-consciousness effect.

I selected Discipline and Punish as my target text because it is a challenging piece that I've read in the past.  I wanted to create a novel that reflected the frustration of a student working her way through a reading.  My result was way more annoying and repetitive than expected, mostly because some of the words that I selected from the original text overlapped with the random thoughts that I wrote, causing the code to print long strings of thought that continued to interrupt each other.  I hope that other students' minds don't get crowded and distracted to this extent!

In the future, I'd like to do a longer text (perhaps the whole book and not just one chapter, though this version does hit 54888 words...).  I would also make sure that words don't overlap to the extent that they do in this version.
