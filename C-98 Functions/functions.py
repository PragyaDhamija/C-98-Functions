def countWord():
    fName = input("Enter a file name ")
    f = open(fName, 'r')
    numberOfWords = 0
    for i in f:
        words = i.split(" ")
        numberOfWords=numberOfWords+len(words)
    print(numberOfWords)

countWord()