def main():
    listception()

def listception():
    bigList = [["One", "Two", "Three"],["4", "5", "6"]]
    for list in bigList:
        for index in range(len(list)):
            print(list[index])

            
if __name__ == '__main__':
    main()