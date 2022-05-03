tehe = int(input("Kas tahad liita(1) / lahutada(2)? "))
arv1 = int(input("Arv 1: "))
arv2 = int(input("Arv 2: "))

if tehe == 1:
    print("Vastus: " + str(arv1 + arv2))
else:
    print("Vastus: " + str(arv1 - arv2))