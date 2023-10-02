from random import randint
N = int(input("Digite o número de 'chutes': "))
soma = 0
contador = 0
while contador < N:
    numero_sorteado = randint(1,100)
    print (numero_sorteado)
    soma = soma + numero_sorteado
    contador = contador + 1
print ("A soma é: ", soma)