#preparation for adding chunks of wandering thoughts
#extract most common words from a text
#Tirthajyoti Sarkar, https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0 
import collections
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Read input file, note the encoding is specified here 
# It may be different in your text file
file = open('panoptic.txt', encoding="utf8")
a= file.read()

# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}

# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['the','a','is']))

# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')




#installing weasyprint
!pip install weasyprint

#import needed elements
import string
import random
from weasyprint import HTML

#opening text file of Foucault's Panopticism - from Discipline and Punish
#https://foucault.info/documents/foucault.disciplineAndPunish.panOpticism/ 
with open('panoptic.txt') as f:
  n = f.read()

#replace/add text
#song lyrics - https://genius.com/Rockwell-somebodys-watching-me-lyrics, https://genius.com/The-beatles-eleanor-rigby-lyrics 
n = n.replace(" power "," power [*looks at the clock* wow, it's that time already? time flies when you're doing work] ")
n = n.replace(" power, "," power, [*looks at the clock* wow, it's that time already? time flies when you're doing work] ")
n = n.replace(" Power "," Power [*looks at the clock* wow, it's that time already? time flies when you're doing work] ")
n = n.replace(" disciplinary "," disciplinary [one YouTube video won't hurt. or two. or five.] ")
n = n.replace(" disciplinary, "," disciplinary, [one YouTube video won't hurt. or two. or five.] ")
n = n.replace(" Disciplinary "," Disciplinary [one YouTube video won't hurt. or two. or five.] ")
n = n.replace(" discipline "," discipline [hahaha look at this meme oh i need to save this and send it to my friend later. wait what if they don't like it? well i like it, i'm gonna save it anyway] ")
n = n.replace(" discipline, "," discipline, [hahaha look at this meme oh i need to save this and send it to my friend later. wait what if they don't like it? well i like it, i'm gonna save it anyway] ")
n = n.replace(" Discipline "," Discipline [hahaha look at this meme oh i need to save this and send it to my friend later. wait what if they don't like it? well i like it, i'm gonna save it anyway] ")
n = n.replace(" disciplines "," disciplines [*checks phone* sweet a new update notification, i've been looking forward to this comic all week!] ")
n = n.replace(" disciplines, "," disciplines, [*checks phone* sweet a new update notification, i've been looking forward to this comic all week!] ")
n = n.replace(" Disciplines "," Disciplines [*checks phone* sweet a new update notification, i've been looking forward to this comic all week!] ")
n = n.replace(" society "," society [ugh i feel so lonely. is that the point of this? to feel sad and alone and isolated?] ")
n = n.replace(" society, "," society, [ugh i feel so lonely. is that the point of this? to feel sad and alone and isolated?] ")
n = n.replace(" Society "," Society [ugh i feel so lonely. is that the point of this? to feel sad and alone and isolated?] ")
n = n.replace(" mechanism ", " mechanism [what's the point of doing all this reading? is this really going to make me happy in the future? i mean, in 5 years am i going to look back and think wow, that reading totally changed my life? i'm a better person because i spent hours doing philosophy readings?] ")
n = n.replace(" mechanism, ", " mechanism, [what's the point of doing all this reading? is this really going to make me happy in the future? i mean, in 5 years am i going to look back and think wow, that reading totally changed my life? i'm a better person because i spent hours doing philosophy readings?] ")
n = n.replace(" Mechanism ", " Mechanism [what's the point of doing all this reading? is this really going to make me happy in the future? i mean, in 5 years am i going to look back and think wow, that reading totally changed my life? i'm a better person because i spent hours doing philosophy readings?] ")
n = n.replace(" mechanisms "," mechanisms [why am i even doing this? i feel stuck. i could be on a super awesome vacation right now. or playing a game. or reading a book for fun. god, i miss that, just reading for fun. i don't think that i'm particularly having fun right now. maybe i am? i don't really know.] ")
n = n.replace(" mechanisms, "," mechanisms, [why am i even doing this? i feel stuck. i could be on a super awesome vacation right now. or playing a game. or reading a book for fun. god, i miss that, just reading for fun. i don't think that i'm particularly having fun right now. maybe i am? i don't really know.] ")
n = n.replace(" Mechanisms "," Mechanisms [why am i even doing this? i feel stuck. i could be on a super awesome vacation right now. or playing a game. or reading a book for fun. god, i miss that, just reading for fun. i don't think that i'm particularly having fun right now. maybe i am? i don't really know.] ")
n = n.replace(" individual "," individual [i bet my friends are having fun without me right now. jerks.] ")
n = n.replace(" individual, "," individual, [i bet my friends are having fun without me right now. jerks.] ")
n = n.replace(" Individual "," Individual [i bet my friends are having fun without me right now. jerks.] ")
n = n.replace(" individuals "," individuals [i wonder what my friends are up to, should i text them?] ")
n = n.replace(" individuals, "," individuals, [i wonder what my friends are up to, should i text them?] ")
n = n.replace(" Individuals "," Individuals [i wonder what my friends are up to, should i text them?] ")
n = n.replace(" function ", " function [wow this reading is such a downer. i need to put the fun back in function ya know what i mean hahaha oh i get myself every time. maybe i should do stand-up. or start a comedy podcast.] ")
n = n.replace(" function, ", " function, [wow this reading is such a downer. i need to put the fun back in function ya know what i mean hahaha oh i get myself every time. maybe i should do stand-up. or start a comedy podcast.] ")
n = n.replace(" Function ", " Function [wow this reading is such a downer. i need to put the fun back in function ya know what i mean hahaha oh i get myself every time. maybe i should do stand-up. or start a comedy podcast.] ")
n = n.replace(" exercise "," exercise [a walk would be really nice right now, i don't even have to go outside, just walking around the dorm would be really nice. i should stretch my legs and maybe get something out of the vending machine in the creepy basement. i wonder if there's sour cream and onion chips] ")
n = n.replace(" exercise, "," exercise, [a walk would be really nice right now, i don't even have to go outside, just walking around the dorm would be really nice. i should stretch my legs and maybe get something out of the vending machine in the creepy basement. i wonder if there's sour cream and onion chips] ")
n = n.replace(" Exercise "," Exercise [a walk would be really nice right now, i don't even have to go outside, just walking around the dorm would be really nice. i should stretch my legs and maybe get something out of the vending machine in the creepy basement. i wonder if there's sour cream and onion chips] ")
n = n.replace(" increase "," increase [ughhhhhh so hungry. i could really go for some cereal right now. or maybe a sandwich. yeah, a nice, hot, melty, ciabatta roll caprese sandwich. i'm so craving fresh basil right now. is the cafe still open? if i hurry, i can grab a quick bite before they close. maybe a drink too. i should try the chai latte again, with vanilla syrup this time. almond milk was good, but i hope they foam it properly. i mean i like warm milk as much as the next gal, but when i want a latte i just gotta have that foam, you know?] ")
n = n.replace(" increase, "," increase, [ughhhhhh so hungry. i could really go for some cereal right now. or maybe a sandwich. yeah, a nice, hot, melty, ciabatta roll caprese sandwich. i'm so craving fresh basil right now. is the cafe still open? if i hurry, i can grab a quick bite before they close. maybe a drink too. i should try the chai latte again, with vanilla syrup this time. almond milk was good, but i hope they foam it properly. i mean i like warm milk as much as the next gal, but when i want a latte i just gotta have that foam, you know?] ")
n = n.replace(" Increase "," Increase [ughhhhhh so hungry. i could really go for some cereal right now. or maybe a sandwich. yeah, a nice, hot, melty, ciabatta roll caprese sandwich. i'm so craving fresh basil right now. is the cafe still open? if i hurry, i can grab a quick bite before they close. maybe a drink too. i should try the chai latte again, with vanilla syrup this time. almond milk was good, but i hope they foam it properly. i mean i like warm milk as much as the next gal, but when i want a latte i just gotta have that foam, you know?] ")
n = n.replace(" techniques "," techniques [*opens new browser window* *forgets why she opened browser window* *closes brower window* *opens browser window*] ")
n = n.replace(" techniques, "," techniques, [*opens new browser window* *forgets why she opened browser window* *closes brower window* *opens browser window*] ")
n = n.replace(" Techniques "," Techniques [*opens new browser window* *forgets why she opened browser window* *closes brower window* *opens browser window*] ")
n = n.replace(" panopticon "," panopticon [i always feel like, somebody's watching meeeeeeeeee and i have no privacy oooooOOOOOoooooh i always feel like] ")
n = n.replace(" panopticon, "," panopticon, [i always feel like, somebody's watching meeeeeeeeee and i have no privacy oooooOOOOOoooooh i always feel like] ")
n = n.replace(" Panopticon "," Panopticon [i always feel like, somebody's watching meeeeeeeeee and i have no privacy oooooOOOOOoooooh i always feel like] ")
n = n.replace(" panoptic "," panoptic [i'm just an average girl with an average life i work way more than nine to five, hey, hell, i'll pay the price all i want is to be left alone in my average dorm but why do i always feel like i'm in the twilight zone and...? i always feel like] ")
n = n.replace(" panoptic, "," panoptic, [i'm just an average girl with an average life i work way more than nine to five, hey, hell, i'll pay the price all i want is to be left alone in my average dorm but why do i always feel like i'm in the twilight zone and...? i always feel like] ")
n = n.replace(" Panoptic "," Panoptic [i'm just an average girl with an average life i work way more than nine to five, hey, hell, i'll pay the price all i want is to be left alone in my average dorm but why do i always feel like i'm in the twilight zone and...? i always feel like] ")
n = n.replace(" political "," political [*sees news app update* wow everything's falling apart. nothing i can really do about it. i want to do something but i'm just stuck here doing my job, being a student...reading this passage about societal structure as society crumbles around me...] ")
n = n.replace(" political, "," political, [*sees news app update* wow everything's falling apart. nothing i can really do about it. i want to do something but i'm just stuck here doing my job, being a student...reading this passage about societal structure as society crumbles around me...] ")
n = n.replace(" Political "," Political [*sees news app update* wow everything's falling apart. nothing i can really do about it. i want to do something but i'm just stuck here doing my job, being a student...reading this passage about societal structure as society crumbles around me...] ")
n = n.replace(" surveillance "," surveillance [karaoke break! i can totally listen to this and read at the same time but why would i want to? i would much rather jam. my next-door-neighbor doesn't care. at least she doesn't say anything to me about it. she should be happy, i'm an amazing singer. and it makes me happy so whatever, it's probably fine. turn it up!] ")
n = n.replace(" surveillance, "," surveillance, [karaoke break! i can totally listen to this and read at the same time but why would i want to? i would much rather jam. my next-door-neighbor doesn't care. at least she doesn't say anything to me about it. she should be happy, i'm an amazing singer. and it makes me happy so whatever, it's probably fine. turn it up!] ")
n = n.replace(" Surveillance "," Surveillance [karaoke break! i can totally listen to this and read at the same time but why would i want to? i would much rather jam. my next-door-neighbor doesn't care. at least she doesn't say anything to me about it. she should be happy, i'm an amazing singer. and it makes me happy so whatever, it's probably fine. turn it up!] ")
n = n.replace(" relations "," relations [i should call my mom. she'd probably like to hear from me. i wonder how her day was. i miss her. maybe i can convince her to bake me some chocolate chip cookies. i'd like that. she'd probably laugh if i ask her. i hope that she's in a good mood because if she's not and i ask her for cookies then she won't think it's funny and honestly i just want to make her laugh and also cookies would be nice too.] ")
n = n.replace(" relations, "," relations, [i should call my mom. she'd probably like to hear from me. i wonder how her day was. i miss her. maybe i can convince her to bake me some chocolate chip cookies. i'd like that. she'd probably laugh if i ask her. i hope that she's in a good mood because if she's not and i ask her for cookies then she won't think it's funny and honestly i just want to make her laugh and also cookies would be nice too.] ")
n = n.replace(" Relations "," Relations [i should call my mom. she'd probably like to hear from me. i wonder how her day was. i miss her. maybe i can convince her to bake me some chocolate chip cookies. i'd like that. she'd probably laugh if i ask her. i hope that she's in a good mood because if she's not and i ask her for cookies then she won't think it's funny and honestly i just want to make her laugh and also cookies would be nice too.] ")
n = n.replace(" police "," police [ughhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh booorrrrrrrrrrrrrred] ")
n = n.replace(" police, "," police, [ughhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh booorrrrrrrrrrrrrred] ")
n = n.replace(" Police "," Police [ughhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh booorrrrrrrrrrrrrred] ")
n = n.replace(" order "," order [i haven't washed my dishes in a while, i should do that. and clean my sink. and vacuum. oh, it feels so nice to clean! really helps clear my headspace and focus. ugh gross everything's dusty too. that nice chemical bleach smell just reminds me of how clean and nice everything is now :)] ")
n = n.replace(" order, "," order, [i haven't washed my dishes in a while, i should do that. and clean my sink. and vacuum. oh, it feels so nice to clean! really helps clear my headspace and focus. ugh gross everything's dusty too. that nice chemical bleach smell just reminds me of how clean and nice everything is now :)] ")
n = n.replace(" Order "," Order [i haven't washed my dishes in a while, i should do that. and clean my sink. and vacuum. oh, it feels so nice to clean! really helps clear my headspace and focus. ugh gross everything's dusty too. that nice chemical bleach smell just reminds me of how clean and nice everything is now :)] ")
n = n.replace(" bodies "," bodies [i should stretch, i've been hunched over this desk all day and if i keep it up i could get early-onset arthritis or something] ")
n = n.replace(" bodies, "," bodies, [i should stretch, i've been hunched over this desk all day and if i keep it up i could get early-onset arthritis or something] ")
n = n.replace(" Bodies "," Bodies [i should stretch, i've been hunched over this desk all day and if i keep it up i could get early-onset arthritis or something] ")
n = n.replace(" effects "," effects [bathroom break bathroom break bathroom break everyone out of my way need to go] ")
n = n.replace(" effects, "," effects, [bathroom break bathroom break bathroom break everyone out of my way need to go] ")
n = n.replace(" Effects "," Effects [bathroom break bathroom break bathroom break everyone out of my way need to go] ")
n = n.replace(" knowledge "," knowledge [i know that i'm taking too long to read this] ")
n = n.replace(" knowledge, "," knowledge, [i know that i'm taking too long to read this] ")
n = n.replace(" Knowledge "," Knowledge [i know that i'm taking too long to read this] ")
n = n.replace(" social "," social [*scrolls through Facebook*] ")
n = n.replace(" social, "," social, [*scrolls through Facebook*] ")
n = n.replace(" Social "," Social [*scrolls through Facebook*] ")
n = n.replace(" investigation "," investigation [what is that oh god no a spider oh no no no no no i need to leave right now shit get the vacuum get the vacuum] ")
n = n.replace(" investigation, "," investigation, [what is that oh god no a spider oh no no no no no i need to leave right now shit get the vacuum get the vacuum] ")
n = n.replace(" Investigation "," Investigation [what is that oh god no a spider oh no no no no no i need to leave right now shit get the vacuum get the vacuum] ")
n = n.replace(" state "," state [whyyyyy is this so hard *sobs*] ")
n = n.replace(" state, "," state, [whyyyyy is this so hard *sobs*] ")
n = n.replace(" State "," State [whyyyyy is this so hard *sobs*] ")
n = n.replace(" being "," being [birds are so lucky, they just get to exist. unless you believe that conspiracy theory that birds aren't real and the government is lying to us about them. does anything get to just exist then?] ")
n = n.replace(" being, "," being, [birds are so lucky, they just get to exist. unless you believe that conspiracy theory that birds aren't real and the government is lying to us about them. does anything get to just exist then?] ")
n = n.replace(" Being "," Being [birds are so lucky, they just get to exist. unless you believe that conspiracy theory that birds aren't real and the government is lying to us about them. does anything get to just exist then?] ")
n = n.replace(" forms "," forms [*checks email* my professor assigned another reading? are you serious?? wait, this reading is supposed to replace the one i just finished are you serious?!?] ")
n = n.replace(" forms, "," forms, [*checks email* my professor assigned another reading? are you serious?? wait, this reading is supposed to replace the one i just finished are you serious?!?] ")
n = n.replace(" Forms "," Forms [*checks email* my professor assigned another reading? are you serious?? wait, this reading is supposed to replace the one i just finished are you serious?!?] ")
n = n.replace(" methods "," methods [i need a fizzy water and some hummus crisps. and maybe some chocolate, i've been good today] ")
n = n.replace(" methods, "," methods, [i need a fizzy water and some hummus crisps. and maybe some chocolate, i've been good today] ")
n = n.replace(" Methods "," Methods [i need a fizzy water and some hummus crisps. and maybe some chocolate, i've been good today] ")
n = n.replace(" principle "," principle [my brain hurts, my brain hurts so much it feels like it's melting down my brin stem and working its way down my spinal column and collecting in a weird hidden pouch at the small of my back and if i'm not careful and move too quickly it might pop and spill everywhere and i won't be able to finish any of my work so i'll just sit at my desk until someone happens to come check on me and by then i'll probably have melted into a puddle on the floor.] ")
n = n.replace(" principle, "," principle, [my brain hurts, my brain hurts so much it feels like it's melting down my brin stem and working its way down my spinal column and collecting in a weird hidden pouch at the small of my back and if i'm not careful and move too quickly it might pop and spill everywhere and i won't be able to finish any of my work so i'll just sit at my desk until someone happens to come check on me and by then i'll probably have melted into a puddle on the floor.] ")
n = n.replace(" Principle "," Principle [my brain hurts, my brain hurts so much it feels like it's melting down my brin stem and working its way down my spinal column and collecting in a weird hidden pouch at the small of my back and if i'm not careful and move too quickly it might pop and spill everywhere and i won't be able to finish any of my work so i'll just sit at my desk until someone happens to come check on me and by then i'll probably have melted into a puddle on the floor.] ")
n = n.replace(" apparatus "," apparatus [awww my pen is broken! maybe if i take it apart and put it back together it will work again...oh great now it won't write, guess i need to find another one *digs through backpack and laptop bag and pencil case*] ")
n = n.replace(" apparatus, "," apparatus, [awww my pen is broken! maybe if i take it apart and put it back together it will work again...oh great now it won't write, guess i need to find another one *digs through backpack and laptop bag and pencil case*] ")
n = n.replace(" Apparatus "," Apparatus [awww my pen is broken! maybe if i take it apart and put it back together it will work again...oh great now it won't write, guess i need to find another one *digs through backpack and laptop bag and pencil case*] ")
n = n.replace(" observation "," observation [when did i smudge my glasses? *gets up and washes single lens* oh, there we go WAIT NOW THE OTHER LENS IS DIRTY AND THE ONE I JUST CLEANED IS ALL SMUDGED ughhh *gets up and washes glasses again* oh that's better, i'll be able to focus so much better now.] ")
n = n.replace(" observation, "," observation, [when did i smudge my glasses? *gets up and washes single lens* oh, there we go WAIT NOW THE OTHER LENS IS DIRTY AND THE ONE I JUST CLEANED IS ALL SMUDGED ughhh *gets up and washes glasses again* oh that's better, i'll be able to focus so much better now.] ")
n = n.replace(" Observation "," Observation [when did i smudge my glasses? *gets up and washes single lens* oh, there we go WAIT NOW THE OTHER LENS IS DIRTY AND THE ONE I JUST CLEANED IS ALL SMUDGED ughhh *gets up and washes glasses again* oh that's better, i'll be able to focus so much better now.] ")
n = n.replace(" functioning "," functioning [what else do i have to do today again? *checks planner*] ")
n = n.replace(" functioning, "," functioning, [what else do i have to do today again? *checks planner*] ")
n = n.replace(" Functioning "," Functioning [what else do i have to do today again? *checks planner*] ")
n = n.replace(" machine "," machine [i wonder if i have any grades updated *logs into Canvas* nope, doesn't look like it. might want to check email *refreshes already-opened email* nope, nothing here either.] ")
n = n.replace(" machine, "," machine, [i wonder if i have any grades updated *logs into Canvas* nope, doesn't look like it. might want to check email *refreshes already-opened email* nope, nothing here either.] ")
n = n.replace(" Machine "," Machine [i wonder if i have any grades updated *logs into Canvas* nope, doesn't look like it. might want to check email *refreshes already-opened email* nope, nothing here either.] ")
n = n.replace(" production "," production [i still need to write my 5-page paper for pop culture and finish up my coding assignment due on Friday and read 50 pages of that ethnography for anthropology tomorrow and i'm also setting up at church on Saturday so i need to make sure to remember that and get everything done ahead of time but i was going to go to the play today i guess i don't have time i'm already late and can't do anything about that oh well and i really can't forget that group project submisssion that i need to get done by 10 PM tonight that's worth 20% of my final grade, i can't afford to fail that class] ")
n = n.replace(" production, "," production, [i still need to write my 5-page paper for pop culture and finish up my coding assignment due on Friday and read 50 pages of that ethnography for anthropology tomorrow and i'm also setting up at church on Saturday so i need to make sure to remember that and get everything done ahead of time but i was going to go to the play today i guess i don't have time i'm already late and can't do anything about that oh well and i really can't forget that group project submisssion that i need to get done by 10 PM tonight that's worth 20% of my final grade, i can't afford to fail that class] ")
n = n.replace(" Production "," Production [i still need to write my 5-page paper for pop culture and finish up my coding assignment due on Friday and read 50 pages of that ethnography for anthropology tomorrow and i'm also setting up at church on Saturday so i need to make sure to remember that and get everything done ahead of time but i was going to go to the play today i guess i don't have time i'm already late and can't do anything about that oh well and i really can't forget that group project submisssion that i need to get done by 10 PM tonight that's worth 20% of my final grade, i can't afford to fail that class] ")
n = n.replace(" force "," force [use the Force, Luke] ")
n = n.replace(" force, "," force, [use the Force, Luke] ")
n = n.replace(" Force "," Force [use the Force, Luke] ")
n = n.replace(" forces "," forces [if you really think about it, most things are out of any one individual's control. as one person, you pretty much just go with the flow for your whole life, not really thinking about it too terribly much, following the well-worn paths of those who came before you, following the rules that society has laid out already, not questioning, defining yourself by other people's standards, just breathing and working and sleeping and dying until everything is over.] ")
n = n.replace(" forces, "," forces, [if you really think about it, most things are out of any one individual's control. as one person, you pretty much just go with the flow for your whole life, not really thinking about it too terribly much, following the well-worn paths of those who came before you, following the rules that society has laid out already, not questioning, defining yourself by other people's standards, just breathing and working and sleeping and dying until everything is over.] ")
n = n.replace(" Forces "," Forces [if you really think about it, most things are out of any one individual's control. as one person, you pretty much just go with the flow for your whole life, not really thinking about it too terribly much, following the well-worn paths of those who came before you, following the rules that society has laid out already, not questioning, defining yourself by other people's standards, just breathing and working and sleeping and dying until everything is over.] ")
n = n.replace(" according "," according [what a lovely time for a headache.  did i take any pain medicine today? i can't remember.] ")
n = n.replace(" according, "," according, [what a lovely time for a headache.  did i take any pain medicine today? i can't remember.] ")
n = n.replace(" According "," According [what a lovely time for a headache.  did i take any pain medicine today? i can't remember.] ")
n = n.replace(" because "," because [why is it so cold in here? i'm wearing a sweatshirt and drinking a mug of tea, i should not be this cold. i guess i could grab a blanket, but then i'd get too hot. maybe i could put on fingerless gloves, they make me feel like a hacker haha. but honestly, that doesn't help either. my fingertips are cold. i think all this sitting in front of a screen is not allowing my blood to flow properly. dad gets like that sometimes, and mom too. i don't really want to get up, though.] ")
n = n.replace(" because, "," because, [why is it so cold in here? i'm wearing a sweatshirt and drinking a mug of tea, i should not be this cold. i guess i could grab a blanket, but then i'd get too hot. maybe i could put on fingerless gloves, they make me feel like a hacker haha. but honestly, that doesn't help either. my fingertips are cold. i think all this sitting in front of a screen is not allowing my blood to flow properly. dad gets like that sometimes, and mom too. i don't really want to get up, though.] ")
n = n.replace(" Because "," Because [why is it so cold in here? i'm wearing a sweatshirt and drinking a mug of tea, i should not be this cold. i guess i could grab a blanket, but then i'd get too hot. maybe i could put on fingerless gloves, they make me feel like a hacker haha. but honestly, that doesn't help either. my fingertips are cold. i think all this sitting in front of a screen is not allowing my blood to flow properly. dad gets like that sometimes, and mom too. i don't really want to get up, though.] ")
n = n.replace(" men ", " men [dance party. dance party RIGHT NOW. ohmygosh i need this, i need this so bad. let's go. 80s synthpop and angsty middle school playlist here i come.] ")
n = n.replace(" men, ", " men, [dance party. dance party RIGHT NOW. ohmygosh i need this, i need this so bad. let's go. 80s synthpop and angsty middle school playlist here i come.] ")
n = n.replace(" Men ", " Men [dance party. dance party RIGHT NOW. ohmygosh i need this, i need this so bad. let's go. 80s synthpop and angsty middle school playlist here i come.] ")
n = n.replace(" all ", " all [the lonely people, where do they all come from? all the lonely people, where do they all belong?] ")
n = n.replace(" all, ", " all, [the lonely people, where do they all come from? all the lonely people, where do they all belong?] ")
n = n.replace(" All ", " All [the lonely people, where do they all come from? all the lonely people, where do they all belong?] ")
n = n.replace(" more ", " more [i wish i had more time to get everything done. then i might have more time to relax and eat and sleep. i never seem to get enough of any of those things. i think i need sleep the most. maybe getting a couple of extra hours in every night would make my mind wander less.] ")
n = n.replace(" more, ", " more, [i wish i had more time to get everything done. then i might have more time to relax and eat and sleep. i never seem to get enough of any of those things. i think i need sleep the most. maybe getting a couple of extra hours in every night would make my mind wander less.] ")
n = n.replace(" More ", " More [i wish i had more time to get everything done. then i might have more time to relax and eat and sleep. i never seem to get enough of any of those things. i think i need sleep the most. maybe getting a couple of extra hours in every night would make my mind wander less.] ")
n = n.replace(" time ", " time [for a snack! then again, it is always time for a snack. or chocolate.] ")
n = n.replace(" time, ", " time, [for a snack! then again, it is always time for a snack. or chocolate.] ")
n = n.replace(" Time ", " Time [for a snack! then again, it is always time for a snack. or chocolate.] ")
n = n.replace(" other ", " other [is it normal to feel different from other people? like so different that no one will truly understand you for who you are? is it just the individualism of Western society that's just taking over my way of thinking, or am i truly alone?] ")
n = n.replace(" other, ", " other, [is it normal to feel different from other people? like so different that no one will truly understand you for who you are? is it just the individualism of Western society that's just taking over my way of thinking, or am i truly alone?] ")
n = n.replace(" Other ", " Other [is it normal to feel different from other people? like so different that no one will truly understand you for who you are? is it just the individualism of Western society that's just taking over my way of thinking, or am i truly alone?] ")
n = n.replace(" possible ", " possible [it's also possible that i want to stop reading. very, very possible.] ")
n = n.replace(" possible, ", " possible, [it's also possible that i want to stop reading. very, very possible.] ")
n = n.replace(" Possible ", " Possible [it's also possible that i want to stop reading. very, very possible.] ")
n = n.replace(" without ", " without [without you i can be free to sketch and dream and play video games] ")
n = n.replace(" without, ", " without, [without you i can be free to sketch and dream and play video games] ")
n = n.replace(" Without ", " Without [without you i can be free to sketch and dream and play video games] ")
n = n.replace(" great ", " great [that'd be greeeeeaaaat] ")
n = n.replace(" great, ", " great, [that'd be greeeeeaaaat] ")
n = n.replace(" Great ", " Great [that'd be greeeeeaaaat] ")
n = n.replace(" every ", " every [little thing she does is magic] ")
n = n.replace(" every, ", " every, [little thing she does is magic] ")
n = n.replace(" Every ", " Every [little thing she does is magic] ")
n = n.replace(" plague ", " plague [is it just me, or is there something in the air? i hope i'm not getting sick. i'd better make some tea with lemon and honey right away. maybe have some vitamin c drops too. don't want to take any chances, i can't afford to get sick.] ")
n = n.replace(" plague, ", " plague, [is it just me, or is there something in the air? i hope i'm not getting sick. i'd better make some tea with lemon and honey right away. maybe have some vitamin c drops too. don't want to take any chances, i can't afford to get sick.] ")
n = n.replace(" Plague ", " Plague [is it just me, or is there something in the air? i hope i'm not getting sick. i'd better make some tea with lemon and honey right away. maybe have some vitamin c drops too. don't want to take any chances, i can't afford to get sick.] ")
n = n.replace(" another ", " another [ANOTHER! *slams empty water bottle on the floor, grabs another one from the fridge* haha maybe i can watch a superhero movie later] ")
n = n.replace(" another, ", " another, [ANOTHER! *slams empty water bottle on the floor, grabs another one from the fridge* haha maybe i can watch a superhero movie later] ")
n = n.replace(" Another ", " Another [ANOTHER! *slams empty water bottle on the floor, grabs another one from the fridge* haha maybe i can watch a superhero movie later] ")

#from Zach Whalen's PrintingToPdfExample.ipynb
#https://colab.research.google.com/drive/1-xEMjJ-6zbzA_c8pqnQOKRVIe8Jwdwna
#add the novel into an HTML template
#formatting = a giant hunk of text, "stream of consciousness"

html_template = f"""
<html>
  <head>
  <title>Student Panoptic</title>
  </head>
  <body>
  {n}
  </body>
</html>
"""

# this line saves that template as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("student_panoptic_novel.pdf")




#check word count
#last check = 54888 words
n.split(" ")
len(n.split(" "))
print(str(len(n.split(" "))))

