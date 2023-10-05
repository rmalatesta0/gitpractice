greetx = "Hello gangsta'"
greet1x = 'What should \n "bruh"'
greet2x = '''I can use "quotes" and a'postrophes'''

print(greetx)
print(greet1x)
print(len(greet1x))
# \n = escape characters, not in char count
print(greet2x)

#---------------------------------------------------------------

greet = "Hello"
greet1 = "Bonjour"
greet2 = "Hola"

list1 = [greet, greet1, greet2]
print(list1)

testString = "Hello Bonjour Hola"
noOsTest = testString.split("o")
print(noOsTest)

#---------------------------------------------------------------

song = "See how the brain plays around..."
wds = song.split()
print(wds)

#---------------------------------------------------------------

weezer = ["Rivers", "Patrick", "Brian", "Scott"]
print(weezer[1])
intro = "These are the members of Weezer, "

commaSeparator = ", "

print(intro + commaSeparator.join(weezer))
print(intro + ", ".join(weezer))

#-----------------------------------------------------------------

testList = weezer, 22, song
print(testList)

#-----------------------------------------------------------------

print(weezer.count("e")) #"e" is not an item in the list
print(weezer.count("Rivers")) #"rivers" is an item in the list
print(intro.count("e")) #this works cause its a normal string
