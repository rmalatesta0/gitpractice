import random

def main():
    eightBall()


def eightBall():
    input("Ask a question: ")

    rolled = (random.randint(1,10))

    if (rolled == 1):
        print("Try again later...")
    elif (rolled == 2):
        print("Most Definitely!")
    elif (rolled == 3):
        print("Probably So.")
    elif (rolled == 4):
        print("It is likely")
    elif (rolled == 5):
        print("I am unsure at the moment.")
    elif (rolled == 6):
        print("It is unlikely")
    elif (rolled == 7):
        print("Probably Not.")
    elif (rolled == 8):
        print("No chance lmao")
    elif (rolled == 9):
        print("Maybe, but it depends")
    else:
        print("With 100% Certainty")

if __name__ == '__main__':
    main()