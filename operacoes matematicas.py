nome = input('Olá,qual seu nome? -> ')
print("Olá,",nome, "seja bem vindo(a) ao nosso programa de matemática!")
op = input('Desejas somar (S), Multiplicar (M), Dividir (D) ou Subtrair (T)? -> ')
if (op == "S" or op =="M" or op == "D" or op == "T"):
    x = int (input ("Digite o primeiro número:" ))
    y = int (input ("Digite o segundo número:" ))
if (op == "S"):
    r = x + y
    print ("O resultado da soma é", r)
elif (op == "M"):
    r = x * y
    print ("O resultado da multiplicação é", r)
elif (op == "D"):
    r = x / y
    print("O resultado da divisão é", r)
elif (op == "T"):
    r = x - y
    print("O resultado da subtração é", r)
else:
    print ("Opção inválida !!")