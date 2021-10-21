# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from builtins import print

defaultPath = "C:/Users/maria/PycharmProjects/Projeto_TAI/example.txt"

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


    




#main
if __name__ == '__main__':
    readFile(defaultPath)

