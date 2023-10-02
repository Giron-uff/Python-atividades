n = int(input('Digite um número inteiro positivo: '))
fatorial = 1
while n > 0:
    fatorial = fatorial * n
    n = n - 1

print('O fatorial desse número é ', fatorial)