passage = '''He was in the forest looking to see the trees
But none were there
He found a girl
She found the Erlking (the lover)
They were in the white wood
Gamboling out to picnic
In the light leaves broke above
Then fell below
I was in the middle ground
Looking to find the flowers in the garden
Wearying of the hate me, hate me not
Wait. they forgot
Woe, oh, the rot
Deeper in they crept
Oblivious of the bears and darker terrors
Or none were there
How did they dare?
I was in the middle ground
Looking to find the fountain of infinite mirror
Tree falling, no one would hear
Shadow of nobody there
Murders of murderers living in fear of it
Owls on the night watch
Solemn and easily wise to what we thought
They thought above
Sound broke below
They were in the black wood
Coveting indiscreetly her for him
Or him for her
Shown what they were'''

#______________________________________

newPara = ""

def madlibsJoiner(passage,prompt,start,end):
    return(passage[start:end]+input(prompt))

newPara += madlibsJoiner(passage,"Please enter a Place: ",0,14)
newPara += madlibsJoiner(passage,"Please enter a Plural Noun: ",20,40)
newPara += madlibsJoiner(passage,"Please enter a Profession: ",44,109)
newPara += madlibsJoiner(passage,"Please enter a Place: ",114,133)
newPara += madlibsJoiner(passage,"Please enter a Plural Noun: ",143,181)
newPara += madlibsJoiner(passage,"Please enter a Place: ",187,229) 
newPara += madlibsJoiner(passage,"Please enter a Place: ",242,278)
newPara += madlibsJoiner(passage,"Please enter a Verb: ",284,333)  
newPara += madlibsJoiner(passage,"Please enter a Way to Move (Past Tense): ",339,372)
newPara += madlibsJoiner(passage,"Please enter a Dangerous Animal (Plural): ",377,395)
newPara += madlibsJoiner(passage,"Please enter a Scary Thing (Plural): ",400,405)
newPara += madlibsJoiner(passage,"Please enter a Place: ",419,471)
newPara += madlibsJoiner(passage,"Please enter a Majestic Sounding Object: ",484,505)
newPara += madlibsJoiner(passage,"Please enter a Verb: ",532,538)
newPara += madlibsJoiner(passage,"Please enter a Possesion of Someone: ",545,565)
newPara += madlibsJoiner(passage,"Please enter a Profession: ",571,599)
newPara += madlibsJoiner(passage,"Please enter an Animal (Plural): ",608,630)
newPara += madlibsJoiner(passage,"Please enter a Adjective: ",634,672)
newPara += madlibsJoiner(passage,"Please enter a Place: ",676,750)
newPara += madlibsJoiner(passage,"Please enter a Adjective Ending in -ly: ",760,770)

def madlibsEnd(passage,start):
    return(passage[start:])

newPara += madlibsEnd(passage,782)

print(newPara)