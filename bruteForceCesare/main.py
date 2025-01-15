alfabeto = "abcdefghijklmnopqrstuvwxyz"


stringaDaDecifrare = input("Inserisci la stringa da decifrare: ")
stringaDaDecifrare = stringaDaDecifrare.lower()

for k in range(1, len(alfabeto)):
    for i in stringaDaDecifrare:
        newPos = alfabeto.index(i) - k
        if newPos >= len(alfabeto):
            newPos = newPos - len(alfabeto)
        print(alfabeto[newPos], end="")
    print(" Chiave: ", k)
    