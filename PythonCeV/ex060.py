num = int(input('numero: '))

fat = num

cont = 1

while num - cont > 1:
    fat = fat*(fat - cont)
    cont = cont + 1

print(fat)