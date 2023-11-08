#Rocco Malatesta and Matthew Moller

def main():
# remove comment on the functions you want to test (one at a time)
    lunch()
    #market()
    #leaves()
    #eagles()
    #teams()
    #menu()
    #restaurant()
    #chickFilA()
    #eaglesWin()

# Number 1
# “A Salesianum student puts $100 in their account. They spend $5 a day on lunch. Create a new variable and store the number of days
#  they could buy lunch.” 

def lunch():
    money = 100
    days = 0
    while money > 0:
        money -= 5
        days += 1
    print(days)

#Number 2
# A tree has 200,000 leaves at the start of Fall. 5,000 leaves fall off every day during Fall. 
# How many leaves will have fallen off the tree by the 30th day of Fall?

def leaves():
    remainingLeaves = 200000
    for days in range(30):
        remainingLeaves -= 5000
    print(remainingLeaves)

# Number 4
# “Taco Bell has 10 items on its menu. 
# Create a list and read over the list, print out each item in alphabetical order”.

def menu():
    list1 = ["Breakfast Burrito", "Breakfast Taco", "Bean Burrito", "Chicken Quesidilla", "Crunch Wrap", "Grilled Cheese Burrito", "Mexican Pizza", "Nachos", "Soft Taco",
     "Strawberry Twist"]
    list1.sort()
    for index in range(len(list1)):
        print(list1[index])

# Number 5
# A restaurant needs 10 waitresses/waiters on shift for operations to run smoothly.
# Only 7 clocked in today though. Using the schedule provided, create a loop that shows who clocked in or who didn’t show up. 

def restaurant():
    waiters = 10 
    waitersin = 7
    waitersin = ["John", "Amy", "Sean", "Jake", "Carla", "Zach", "Jack"]
    for index in range(len(waitersin)):
        print(waitersin[index])

# Number 6
# A grocery store has 10 different types of vegetables.
# Make a list and create a loop that writes the words from shortest to longest.

def market():
    foodList = ["Onions", "Celery", "Lettuce", "Carrots", "Peppers", "Cabbage", "Cucumber", "Asparagus", "Green Beans", "Brussels Sprouts"]
    for index in range(len(foodList)):
        print(foodList[index])

# Number 7
# Chick-fil-A has 5 types of menu items (Sandwiches, nuggets, chicken tenders, salads, fries).
# Create a list and iterate it over the list to print out each type of menu item

def chickFilA():
    menu = ["Sandwiches", "Nuggets", "Chicken Tenders", "Salads", "Fries"]
    for index in range(len(menu)):
        print(menu[index])

# Number 8
# If the Eagles play 7 games, use the numbers below (Eagles are on the left side):
# List = [(21,7), (32,24), (16, 15), (20,19), (25, 4), (15,5), (30, 19)]
# Create a loop with the list of numbers to determine how many there were.

def eagles():
    games = ["(21,7)", "(32,24)", "(16, 15)", "(20,19)", "(25, 4)", "(15,5)", "(30, 19)"]
    print(len(games))

# Number 9
# How Many games have the Eagles won?
# Listofwins = [“patriots”, “buccaneers”, “Vikings”, “commanders”, “rams”, “Jets”, “dolphins”, “commanders”, “cowboys”]

def eaglesWin():
    gamesWon = ["Patriots", "Buccaneers", "Vikings", "Commanders", "Rams", "Jets", "Dolphins", "Commanders", "Cowboys"]
    print(len(gamesWon))

# Number 10
# The NFC has 16 teams. Create a list that can go over and print out each team in the NFC. NFC teams are listed -
# [Eagles, Commanders, Cowboys, Giants, Bears, Packers, Saints, Falcons, Vikings, 49ers, Cardinals, Panthers, Lions, Rams, Seahawks, Buccaneers]

def teams():
    teamsList = ["Eagles", "Commanders", "Cowboys", "Giants", "Bears", "Packers", "Saints", "Falcons", "Vikings", "49ers", "Cardinals", "Panthers", "Lions", "Rams", "Seahawks", "Buccaneers"]
    for NFC in teamsList:
        print(NFC)

#----------------------------------------------

if __name__ == "__main__":
    main()