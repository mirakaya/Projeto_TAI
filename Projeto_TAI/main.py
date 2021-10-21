# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from builtins import print

defaultPath = "example.txt"

def readFile(path):
    #reads a .txt file
    file = open(path, "r")
    fileContent = file.read()
    createAlphabet(fileContent)


def createAlphabet(fileContent):
   #creates a set with all the possible characters
   #each letter only appears once and it's unordered

   alphabet = set()

   for i in fileContent:
       alphabet.add(i)

   print(alphabet)
   print(len(alphabet))

   checkStartPoint("abc[", alphabet)


def checkStartPoint(begin, alphabet): #change to correct names, maybe alphabet is not an arg

    k=4 #change this, we should probably be able to check k from the table

    if len(begin) != k:
        print("Error - the start point does not have the same length as k")

    for i in begin:

        if i in alphabet:
            print("yes -  " + i)

        else:
            print("Error - at least one of the characters is not on the alphabet of the text - " + i )




#main
if __name__ == '__main__':
    readFile(defaultPath)

