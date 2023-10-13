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

newPara = ""

start = 0
end = 14

newPara += passage[start:end]
newText1 = input("Enter a Place (Non Proper Noun): ")
newPara += newText1

start = end + 6
end = start + 20 

newPara += passage[start:end]
newText1 = input("Enter a Plural Noun: ")
newPara += newText1

start = end + 5
end = start + 64

newPara += passage[start:end]
newText1 = input("Enter a Noun: ")
newPara += newText1

start = end + 5
end = start + 19

newPara += passage[start:end]
newText1 = input("Enter a Place: ")
newPara += newText1

start = end + 10
end = start + 38

newPara += passage[start:end]
newText1 = input("Enter a Plural Noun: ")
newPara += newText1

start = end + 6
end = start + 29 + 13

newPara += passage[start:end]
newText1 = input("Enter a Place: ")
newPara += newText1

start = end + 13
end = start + 21

newPara += passage[start:end]
newText1 = input("Enter a Plural Noun: ")
newPara += newText1

start = end + 7
end = start + 8

newPara += passage[start:end]
newText1 = input("Enter a Place: ")
newPara += newText1

start = end + 6
end = start + 49

newPara += passage[start:end]
newText1 = input("Enter a Verb: ")
newPara += newText1

start = end + 6
end = start + 33

newPara += passage[start:end]
newText1 = input("Enter a Way to Move: ")
newPara += newText1

start = end + 5
end = start + 18

newPara += passage[start:end]
newText1 = input("Enter a (Plural) Dangerous Animal: ")
newPara += newText1

start = end + 5
end = start + 5

newPara += passage[start:end]
newText1 = input("Enter a Scary Thing (Plural): ")
newPara += newText1

start = end + 14
end = start + 52

newPara += passage[start:end]
newText1 = input("Enter a Place: ")
newPara += newText1

start = end + 13
end = start + 12

newPara += passage[start:end]
newText1 = input("Enter a Verb: ")
newPara += newText1

start = end + 4
end = start + 5

newPara += passage[start:end]
newText1 = input("Enter a Mystical Sounding Object: ")
newPara += newText1

start = end + 27
end = start + 33

newPara += passage[start:end]
newText1 = input("Enter a Thing Somoneone Owns: ")
newPara += newText1

start = end + 6
end = start + 16 + 12

newPara += passage[start:end]
newText1 = input("Enter a Job (Plural): ")
newPara += newText1

start = end + 9
end = start + 22

newPara += passage[start:end]
newText1 = input("Enter an Animal (Plural): ")
newPara += newText1

start = end + 4
end = start + 38

newPara += passage[start:end]
newText1 = input("Enter an Adjective: ")
newPara += newText1

start = end + 4
end = start + 74

newPara += passage[start:end]
newText1 = input("Enter a Place: ")
newPara += newText1

start = end + 10
end = start + 73

newPara += passage[start:end]

print(newPara)