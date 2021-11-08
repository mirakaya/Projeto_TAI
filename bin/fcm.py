from random import random
import time
import os.path
import math
from sys import argv


def readFile(path):
    # reads a .txt file
    file = open(path, "r", encoding= "UTF-8")
    fileContent = file.read()

    return fileContent


def createAlphabet(fileContent, k):
    # creates a set with all the possible characters
    # each letter only appears once and it's unordere
    prio=""
    alphabet = set()
    for i in fileContent:
        alphabet.add(i)
        if len(prio) < k:
            prio += i

    return alphabet, prio


def initDictionary(cols, combs):
    n_appearances = {}
    for i in combs:
        n_appearances[i] = {}
        for j in cols:
            n_appearances[i][j] = 0
    return n_appearances


def calcProb(n_appearances, c, e, a, cols):
    prob = (n_appearances[c][e] + a) / (sum(n_appearances[c].values()) + (a * len(cols)))
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

            Hc += -prob * math.log2(prob)

        H_dict[c] = round(Hc, 2)

    return H_dict, Probs


def calculatingFCM_v2(text, a, k):
    fileContent = readFile(text)

    # Example in moodle (55 symbols) -- k=2, a=1--> E=2.54  |   k=3, a=0.1--> E=1.97

    cols, prio = list(createAlphabet(fileContent, k))

    n_appearances = {}
    # Make table(Dictionary)
    for i in range(k, len(fileContent[k:]) + 1):
        c = fileContent[i - k:i]
        e = fileContent[i]

        # Update table
        if e.isascii():
            if c not in n_appearances:
                n_appearances[c] = {}

            if e not in n_appearances[c]:
                n_appearances[c][e] = 1

            else:
                n_appearances[c][e] += 1

    # Entropy of each context
    H_dict, Probs = calcEntropy(n_appearances, a, cols)  # key - context; value - H

    # AVG Entropy
    entropy_sum = 0

    total_sum = sum(sum(i.values()) for i in n_appearances.values())

    for c in H_dict:
        Pc = sum(n_appearances[c].values()) / total_sum
        entropy_sum += H_dict[c] * Pc

    print("Value of entropy ", round(entropy_sum, 2), " bits/symbol")
    return Probs, prio


# ----------------------------------------------------------------------------------------------------------


def calculatingFCM(text, alpha, k):
    sequencia = ""
    flag = False
    n_appearances = {}
    P = {}
    Hc = {}
    alphabet = []
    valorH = 0
    contagem = 0

    with open(text, encoding="UTF-8") as f:
        while True:
            c = f.read(1)
            if not c:

                for i in range(0, len(list(n_appearances.keys()))):
                    sequencia = list(n_appearances.keys())[i]
                    P[sequencia] = {}
                    Hc_value = 0

                    for j in range(0, len(list(n_appearances[sequencia].keys()))):
                        # Calculating the probability
                        P[sequencia][list(n_appearances[sequencia].keys())[j]] = (
                                    (list(n_appearances[sequencia].values())[j] + alpha) / (
                                        sum(list(n_appearances[sequencia].values())) + alpha * len(alphabet)))

                        # Calculating Entropy of a sub-model(sequence)
                        Hc_value -= (list(P[sequencia].values()))[j] * math.log2(
                            (list(P[sequencia].values()))[j]) / contagem

                    # dictionary of Hc values for each sequence
                    Hc[sequencia] = Hc_value

                # Calculating the overall Entropy of the model
                for i in range(0, len(list(P.keys()))):
                    sequencia = list(n_appearances.keys())[i]
                    valorH += (Hc[sequencia] * (sum(list(n_appearances[sequencia].values())) + alpha * len(alphabet)))

                print("Value of entropy ", round(valorH, 2), " bits/symbol")
                break

            contagem += 1
            if c.isascii():

                if c not in alphabet:
                    alphabet += c

                if len(sequencia) < k and flag == False:
                    sequencia += c

                else:
                    flag = True

                    if sequencia not in n_appearances:
                        n_appearances[sequencia] = {}

                    if c not in n_appearances[sequencia]:
                        n_appearances[sequencia][c] = 1

                    else:
                        n_appearances[sequencia][c] = n_appearances[sequencia][c] + 1
                    sequencia = sequencia[1:]
                    sequencia = sequencia + c
    return P


def generator(dictionary, prior, lenText):
    # checks if prior is valid

    aux = list(dictionary.keys())

    if prior in dictionary:
        if len(aux[0]) == len(prior):
            print("VALID")
        else:
            return "INVALID"
    else:
        return "INVALID"

    # for the moment I'll consider a 10000 char generation
    priorList = list(prior)

    generated_text = [None] * lenText
    index = 0

    '''for i in prior: #fills list with prior
        generated_text[index] = prior[index]
        index += 1
    print(generated_text)'''

    for i in generated_text:

        # print("I am index", index)

        if index >= len(prior):  # generates text

            aux = generated_text[index - len(prior): index]  # last k positions
            # aux_str = ""
            aux_str = listToString(aux)

            keys_list = list(dictionary.get(aux_str).keys())
            values_list = list(dictionary.get(aux_str).values())

            # print("I am valueslist", values_list)

            position = sorting(values_list)

            # print("I am position", position)

            answerKey = keys_list[position]

            generated_text[index] = answerKey


            # return next_chars_list[position]
            index += 1

        else:  # fills list with prior
            generated_text[index] = prior[index]

            index += 1
        # print(generated_text)

    result = listToString(generated_text)

    with open('file.txt', 'w') as data:  # writes to file.txt the dictionary #12
        data.write(result)

    return result


def listToString(list):
    aux = ""

    for a in list:  # last k positions in a string
        aux += a

    return aux


def sorting(values):  # returns the position chosen

    count = 0
    random_variable_instance = random()

    entropySum = values[count]

    for i in values:
        if entropySum < random_variable_instance:
            if count != 0:
                entropySum = entropySum + values[count]

            count += 1

        else:
            return count

    return len(values) - 1


def main(example):
    # while(True):
    #     text = input("Enter name of text file: ")
    #     alpha = input("Enter name of alpha: ")
    #     k = input("Enter k value: ")
    #     if os.path.isfile(text) and alpha.isnumeric() and k.isnumeric:
    #         break
    #     if os.path.isfile(text) == False:
    #         print("File not found! Please insert a valid file")
    #     elif alpha.isnumeric() == False:
    #         print("Please insert a valid number")
    #     elif k.isnumeric() == False:
    #         print("Please insert a valid k")

    # print(text)
    # print(alpha)

    # print("encontrado")
    # a = calculatingFCM(str(text), int(alpha), int(k))

    alpha = 1
    k = 2
    begin = time.perf_counter()
    a, prio = calculatingFCM_v2(example, alpha, k)
    end = time.perf_counter()
    print(end - begin)

    ans = generator(a, prio, 10000)
    print(ans)


if __name__ == "__main__":
    #example = argv[1]
    main("../examples/example.txt")
