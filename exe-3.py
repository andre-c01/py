import random

num = random.randint(10, 100)

print(num)
while True:
    uinput =  int(input("Digite um numero: "))
    if uinput < num:
        print("menor")
    elif uinput > num:
        print("maior")
    elif uinput == num:
        print("encontrado")
        break