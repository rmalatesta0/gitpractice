passage = '''He was in the forest looking to see the trees
But none were there
He found a girl
She found the Erlking (the lover)
They were in the white wood
Gamboling out to picnic
In the light leaves broke above
Then fell below'''

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
end = start + 29

newPara += passage[start:end]

print(newPara)