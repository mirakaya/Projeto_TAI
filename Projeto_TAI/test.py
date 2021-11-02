# def obterCardi(text_file):
#     with open(text_file) as f:
#         while True:
#             c = f.read(1)
#             if not c:
#                 return(chars)
#             if c not in chars and c.isascii():
#                 chars.append(c)
            
def avancarUmaCasa(text, alpha, k):
    sequencia = ""
    flag = False
    n_appearances = {}
    entropy = {}
    with open(text) as f:
        while True:
            c = f.read(1)
            if not c:
                print(list(n_appearances.keys()))
                for i in range(0, len(list(n_appearances.keys()))):
                    sequencia = list(n_appearances.keys())[i]
                    entropy[sequencia] = {}
                    for j in range(0, len(list(n_appearances[sequencia].keys()))):
                        entropy[sequencia][list(n_appearances[sequencia].keys())[j]] = ((list(n_appearances[sequencia].values())[j] + alpha)/(sum(list(n_appearances[sequencia].values()))+ alpha * len(list(n_appearances[sequencia].keys()))))
                print(n_appearances)
                print(entropy)
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
    avancarUmaCasa(str(text), int(alpha), int(k))

if __name__ == "__main__":
    import os.path
    chars = []
    main()