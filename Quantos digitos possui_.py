n = int(input("Informe um número inteiro positivo: "))
while n < 0:
    n = int(input("Informe um número inteiro positivo: "))
contador_dig = 0

while n > 0:
    n //= 10
    contador_dig += 1
print("O número de dígitos é:", contador_dig)