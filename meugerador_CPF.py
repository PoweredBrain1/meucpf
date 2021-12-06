from random import randint
numero = str(randint(100000000, 999999999))
cpftratado = str(numero) #cpf sem os 2 ultimos digitos de controle
acumulaCalcNcfp = 0
acumulaCalcNcfp2 = 0
#print(cpftratado)

# Iteração para achar valor do 1 digito de controle
for j, i in enumerate(range(10,1,-1), start=1):
#    print(f'o j é {j}, e o i é {i}')
    ncpf = int((cpftratado[j-1]))
#    print(f'ncpf é: {ncpf}')
    calcncpf = ncpf * i
#    print(f'o calcncpf {calcncpf}')
    acumulaCalcNcfp = acumulaCalcNcfp + calcncpf
#print(acumulaCalcNcfp)

if ((11-(acumulaCalcNcfp % 11)) > 9):
    acumulaCalcNcfp = 0
else:
    acumulaCalcNcfp = (11-(acumulaCalcNcfp % 11))

#print(acumulaCalcNcfp)


# Iteração para achar valor do 2 digito de controle
for j, i in enumerate(range(11,2,-1), start=1):
#    print(f'o j é {j}, e o i é {i}')
    ncpf = int((cpftratado[j-1]))
#    print(f'ncpf é: {ncpf}')
    calcncpf = ncpf * i
#    print(f'o calcncpf {calcncpf}')
    acumulaCalcNcfp2 = acumulaCalcNcfp2 + calcncpf
#print(acumulaCalcNcfp)

calcncpf = acumulaCalcNcfp * 2
acumulaCalcNcfp2 = acumulaCalcNcfp2 + calcncpf
if ((11-(acumulaCalcNcfp2 % 11)) > 9):
    acumulaCalcNcfp2 = 0
else:
    acumulaCalcNcfp2 = (11-(acumulaCalcNcfp2 % 11))
# print(acumulaCalcNcfp2)

# verificação do CPF
cpfcalculado = str(cpftratado)+str(acumulaCalcNcfp)+str(acumulaCalcNcfp2)
print(cpfcalculado)
