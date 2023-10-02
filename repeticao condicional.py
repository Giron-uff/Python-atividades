from random import randint
num = int(input('Digite um numero inteiro entre 1 e 100: '))
numero_sorteado = randint(1,100)
soma = numero_sorteado
chutes = 1
print(numero_sorteado)
while num != numero_sorteado:
    numero_sorteado = randint(1,100)
    soma = soma + numero_sorteado
    chutes = chutes + 1
    print(numero_sorteado)
print('A soma é:', soma,' e o total de tentativas é:', chutes)