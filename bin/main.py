from random import random
import time
import math
from sys import argv

def readFile(path):
    #reads a .txt file
    file = open(path, "r")
    fileContent = file.read()
    
    return fileContent

def createAlphabet(fileContent):
    #creates a set with all the possible characters
    #each letter only appears once and it's unordere
    alphabet = set()
    for i in fileContent:
       alphabet.add(i)

    return alphabet
    
def initDictionary(cols, combs):
    n_appearances = {}
    for i in combs:
        n_appearances[i] = {}
        for j in cols:
            n_appearances[i][j] = 0
    return n_appearances

def calcProb(n_appearances, c, e, a, cols):
    prob = (n_appearances[c][e]+a) / (sum(n_appearances[c].values()) + (a*len(cols)))
    return prob

def calcEntropy(n_appearances, a, cols):
    H_dict = {}
    Probs = {}
    for c in n_appearances.keys():
        Hc = 0
        Probs[c] = {}        
        for s in n_appearances[c].keys():
            prob = calcProb(n_appearances, c, s, a, cols)
            Probs[c][s] = prob

            Hc += -prob*math.log2(prob)
            
        H_dict[c] = round(Hc, 2)

    return H_dict, Probs

def calculatingFCM(text, a, k):
    fileContent = readFile(text)
    cols = list(createAlphabet(fileContent))

    n_appearances = {}
    #Make table(Dictionary)
    for i in range(k, len(fileContent[k:])+1):
        c = fileContent[i-k:i]
        e = fileContent[i]

        #Update table
        if c not in n_appearances:
            n_appearances[c] = {}
            
        if e not in n_appearances[c]:
            n_appearances[c][e] = 1

        else:
            n_appearances[c][e] += 1

    #Entropy of each context
    H_dict, Probs = calcEntropy(n_appearances, a, cols)          #key - context; value - H

    #AVG Entropy
    entropy_sum = 0
    total_sum = sum(sum(i.values()) for i in n_appearances.values())
    for c in H_dict:
        Pc = sum(n_appearances[c].values()) / total_sum
        entropy_sum += H_dict[c] * Pc

    print("Value of entropy ", round(entropy_sum, 2), " bits/symbol")
    return Probs


def generator(entropy, prior):
    # checks if prior is valid

    aux = list(entropy.keys())

    if prior in entropy:
        if len(aux[0]) == len(prior):
            print("VALID")
        else:
            print("INVALID")
            return
    else:
        print("INVALID")
        return


    #for the moment I'll consider a 10000 char generation

    generated_text = [None] * 10000
    index = 0

    for i in range(len(generated_text)):

        if i >= len(prior): # Generates text
            
            aux = generated_text[i-len(prior): i] #last k positions

            aux_str = listToString(aux)
            if entropy.get(aux_str):

                keys_list = list(entropy.get(aux_str).keys())
                values_list = list(entropy.get(aux_str).values())

                position = sorting(values_list)

                answerKey = keys_list[position]

                generated_text[i] = answerKey

                #return next_chars_list[position]
                index += 1

        else: #fills list with prior
            generated_text[i] = prior[i]

            index += 1

    result = listToString(generated_text)

    with open('file.txt', 'w') as data: #writes to file.txt the dictionary #12
        data.write(result)


    return result



def listToString (l):
    aux = ""
    for a in l:  # last k positions in a string
        if a:
            aux += a

    return aux


def sorting (values): #returns the position chosen
    random_variable_instance = random()
    entropySum = values[0]

    for i in range(len(values)):
        if entropySum < random_variable_instance:
            if i != 0:
                entropySum = entropySum + values[i]
        else:
            return i

    return len(values)-1



def main(example):

    # FCM
    alpha = 1
    k = 2
    begin = time.perf_counter()
    a = calculatingFCM(example, alpha, k)
    end = time.perf_counter()
    print(end-begin)

    # Generator
    generator(a, "wl")


if __name__ == "__main__":
    
    example = argv[1]
    main(example)