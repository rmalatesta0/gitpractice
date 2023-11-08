def main():
    #test1("Monday")
    #test1("Tuesday")
    #test1("Wednesday")
    #test1("Thursday")
    #test1("Friday")
    #test1("Saturday")
    #test1("Sunday")
    logicOperators()
    logicErrors()

def test1(today):
    if(today == "Monday"):
        print("It's the first day of the week.")
    elif(today == "Tuesday"):
        print("No more practices today :(")
    elif(today == "Wednesday"):
        print("Hump Day")
    elif(today == "Thursday"):
        print("I love Thursday!!!")
    elif(today == "Friday"):
        print("Football Game!!!")
    elif(today == "Saturday"):
        print("It is Saturday!")
    elif(today == "Sunday"):
        print("Tomorrow is Monday")
    else:
        print("Not Monday")
    #----------------------------------
    if(today == "Sunday","Saturday"):
        print("It's the Weekend!")
    else:
        (print("It's not the Weekend..."))
    #----------------------------------
def logicOperators():
    isRaining = True
    rainIsLikely = False

    if (isRaining or rainIsLikely):
        print("Bring an umbrella.")
    else:
        print("Not going to rain.")
#df
    philsWon = False
    astrosWon = True

    if (philsWon and astrosWon):
        print("Phillies Play Astros in World Series.")
    else:
        print("World series matchup is different.")
    if (not philsWon and not astrosWon):
        print("Diamondbacks vs Rangers in the WS")
#df
    cowboysWon = False

    if (not cowboysWon):
        print("football sux")
    #----------------------------------
def logicErrors():
    number = 7
    if (number == 6 or number == 8):
        print("yea")
    else:
        print("bruhg tf u doinnnnn")

if __name__ == '__main__':
    main()
    