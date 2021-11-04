sala = float(input('salario: '))

au10 = sala * 0.1

au15 = sala * 0.15

sala10 = sala + au10

sala15 = sala + au15

if sala > 1250:
    print(sala10)
elif sala <= 1250:
    print(sala15)