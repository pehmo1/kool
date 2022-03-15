""" numbrid = [1,3734,2,7,55,3,4,5]

biggest = 0
for i in numbrid:
    if i > biggest: biggest = i

print("Suurim " + str(biggest)) """

""" numbrid = []
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
numbrid.append(number1)
numbrid.append(number2)
numbrid.append(number3)
for i in numbrid:
    print(i) """

inputs = int(input("\nMitu vanust tahad sisestada? "))
vanused = []
for i in range(1,inputs+1):
    vanused.append(int(input(f"Sisesta vanus nr{i}: ")))

print(f"\nSuurim vanus on: {max(vanused)}")