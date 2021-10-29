# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from builtins import print
from cgi import print_form

defaultPath = "example.txt"

def readFile(path):
    #reads a .txt file
    file = open(path, "r")
    fileContent = file.read()

    k = 2

    createAlphabet(fileContent)
    write_dictionary(fileContent, k)


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

def write_dictionary(texto, k):

    count = 0

    listCharacters = list(texto) #useful for knowing the characters in k

    for i in texto:

        if count <= len(texto)-k:

            nextPosition = count + k - 1 #letter after k

            temp = listCharacters[count - 1:nextPosition]  # characters of k

            separator = ''
            auxKey = separator.join(temp) #turns list into a string, value of k

            if len(auxKey) == k:


                nextCharacter = listCharacters[nextPosition]# character after k

                if auxKey in dictionary: # if it is a known term, adds one to the times the string has occurred in the text

                    newList = []

                    for p in dictionary[auxKey]:

                        newList += p[0]


                    for j in dictionary[auxKey]:

                        if nextCharacter in newList: #only works if the repeated value is on the [0] position

                            positionCharacter = 0

                            for h in newList: #seek position of character

                                if newList[positionCharacter] == nextCharacter:
                                    break
                                else:
                                    positionCharacter += 1


                            print("exists")


                            freqNextCharacter = dictionary[auxKey][positionCharacter][1]


                            newValue = [nextCharacter, freqNextCharacter + 1]
                            dictionary[auxKey][positionCharacter] = newValue
                            break

                        else: #i think it works
                            print("nope")
                            dictionary[auxKey] += [[nextCharacter, 1]]
                            break


                else: # if it is a new term, adds to dictionary

                    dictionary[auxKey] = [[nextCharacter, 1]]


            print(dictionary)

            count += 1




#main
if __name__ == '__main__':
    #readFile(defaultPath)
    write_dictionary("aaabaaacaaabaaacaaazaaazaaazaaaxaaav", 3) # b2, c2, z3, x1, v1
