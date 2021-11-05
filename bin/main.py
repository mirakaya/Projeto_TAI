import time
from random import random
from builtins import print

defaultPath = "example.txt"

def readFile(path):
    #reads a .txt file
    file = open(path, "r")
    fileContent = file.read()

    createAlphabet(fileContent)
    write_dictionary(fileContent, 3)


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


dictionary = {}

def write_dictionary(text, k):

    count = 0 #used to iterate the text and tell which characters belong to the k interval
    listCharacters = list(text)

    for i in text:

        if count <= len(text)-k:

            nextPosition = count + k - 1 #position after the k characters

            temp = listCharacters[count - 1:nextPosition]  # characters of k

            separator = ''
            auxKey = separator.join(temp) #turns list into a string, k interval

            if len(auxKey) == k: #makes sure the dictionary only has keys of k length

                nextCharacter = listCharacters[nextPosition]#character after k

                if auxKey in dictionary: #known key, adds one to the frequency of the string

                    newList = []

                    for p in dictionary[auxKey]: #creates a list with all of the characters after the key

                        newList += p[0]


                    for j in dictionary[auxKey]:

                        if nextCharacter in newList: #if the character is known

                            positionCharacter = 0

                            for h in newList: #seek position of character

                                if newList[positionCharacter] == nextCharacter:
                                    break
                                else:
                                    positionCharacter += 1

                            freqNextCharacter = dictionary[auxKey][positionCharacter][1]
                            newValue = [nextCharacter, freqNextCharacter + 1]
                            dictionary[auxKey][positionCharacter] = newValue #finds out the frequency of the character, adds 1 and substitute on the right position

                            break

                        else: #first time the character has appeared after the key
                            dictionary[auxKey] += [[nextCharacter, 1]]
                            break


                else: #new key

                    dictionary[auxKey] = [[nextCharacter, 1]]


            #print(dictionary)

            count += 1

    printDictionary(dictionary)


def printDictionary(dictionary):

    print(dictionary)


def suitc() -> str: #example for the generator
    random_variable_instance = random()
    if 0 < random_variable_instance and 0.25 >= random_variable_instance:
        return "Diamonds"
    elif 0.25 < random_variable_instance and 0.5 >= random_variable_instance:
        return "Clubs"
    elif 0.5 < random_variable_instance and 0.75 >= random_variable_instance:
        return "Hearts"
    elif 0.75 < random_variable_instance and 1 >= random_variable_instance:
        return "Spades"





#main
if __name__ == '__main__':

    begin = time.perf_counter()
    readFile(defaultPath)
    #write_dictionary("aaabaaacaaabaaacaaazaaazaaazaaaxaaavacab", 3) # b2, c2, z3, x1, v1

    end = time.perf_counter()

    print("The time was -- " + str (end - begin))