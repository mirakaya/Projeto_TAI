from random import random



def avancarUmaCasa(text, alpha, k):
    sequencia = ""
    flag = False
    n_appearances = {}
    entropy = {}
    with open(text) as f:
        while True:
            c = f.read(1)
            if not c:
                #print(list(n_appearances.keys()))
                for i in range(0, len(list(n_appearances.keys()))):
                    sequencia = list(n_appearances.keys())[i]
                    entropy[sequencia] = {}
                    for j in range(0, len(list(n_appearances[sequencia].keys()))):
                        entropy[sequencia][list(n_appearances[sequencia].keys())[j]] = ((list(n_appearances[sequencia].values())[j] + alpha)/(sum(list(n_appearances[sequencia].values()))+ alpha * len(list(n_appearances[sequencia].keys()))))
                #print(n_appearances)
                #print(entropy)
                break
            if c.isascii():
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
    return entropy


def generator(entropy, prior):
    # checks if prior is valid

    aux = list(entropy.keys())

    if prior in entropy:
        if len(aux[0]) == len(prior):
            print("VALID")
        else:
            return "INVALID"
    else:
        return "INVALID"


    #for the moment I'll consider a 10000 char generation
    priorList = list(prior)

    generated_text = [None] * 10000
    index = 0

    '''for i in prior: #fills list with prior

        generated_text[index] = prior[index]
        index += 1

    print(generated_text)'''


    for i in generated_text:

        #print("I am index", index)

        if index >= len(prior):#generates text

            aux = generated_text[index-len(prior): index] #last k positions
            #aux_str = ""
            aux_str = listToString(aux)

            keys_list = list(entropy.get(aux_str).keys())
            values_list = list(entropy.get(aux_str).values())

            #print("I am valueslist", values_list)

            position = sorting(values_list)

            #print("I am position", position)

            answerKey = keys_list[position]

            generated_text[index] = answerKey

            '''values = list(entropy[i].values())
            next_chars_list = list(entropy[i].keys())'''

            '''  # receives the position

            next_character = next_chars_list[position]'''

            #return next_chars_list[position]
            index += 1

        else: #fills list with prior
            generated_text[index] = prior[index]

            index += 1
        #print(generated_text)

    result = listToString(generated_text)

    with open('file.txt', 'w') as data: #writes to file.txt the dictionary #12
        data.write(result)


    return result



def listToString (list):
    aux = ""

    for a in list:  # last k positions in a string
        aux += a

    return aux


def sorting (values): #returns the position chosen

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

    return len(values)-1



def main():
    while(True):
        text = input("Enter name of text file: ")
        alpha = input("Enter name of alpha: ")
        k = input("Enter k value: ")
        if os.path.isfile(text) and alpha.isnumeric() and k.isnumeric:
            break
        if os.path.isfile(text) == False:
            print("File not found! Please insert a valid file")
        elif alpha.isnumeric() == False:
            print("Please insert a valid number")
        elif k.isnumeric() == False:
            print("Please insert a valid k")

    print(text)
    print(alpha)

    print("encontrado")
    a = avancarUmaCasa(str(text), int(alpha), int(k))

    #a = avancarUmaCasa("example.txt", 0, 3)

    generator(a, "wsl")



if __name__ == "__main__":
    import os.path
    chars = []
    main()