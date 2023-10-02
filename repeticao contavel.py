num1 = int(input("Entre com o valor inicial: "))
num2 = int(input("Entre com o valor final: "))
soma = 0
for i in range(num1, num2, +1 ):
    if i %2 == 0:
        soma = soma + 1
print ("A soma é:", soma)