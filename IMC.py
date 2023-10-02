import math
print ('Seja bem vindo(a) ao programa para calcular seu IMC (Índice de massa corpórea)')
nome = input('Qual seu nome? -> ')
idade = input('Qual sua idade? -> ')
massa = float(input('Qual seu peso? -> '))
altura = float(input('Qual sua altura? -> '))
imc = (massa / altura**2)
if imc < 18.5:
    print('Seu IMC é:', "%.2f" % imc,'e voce está abaixo do peso!')
elif imc == 18.5 or imc < 25:
    print ('Seu IMC é:', "%.2f" % imc,'e voce é saudável!')
elif imc == 25 or imc < 30:
    print ('Seu IMC é:', "%.2f" % imc,'e voce está acima do peso!')
elif imc == 30 or imc < 35:
    print ('Seu IMC é:', "%.2f" % imc,'e voce possui obesidade de grau 1!')
elif imc == 35 or imc < 40:
    print ('Seu IMC é:', "%.2f" % imc,'e voce possui obesidade de grau 2!')
elif imc > 40:
    print ('Seu IMC é:', "%.2f" % imc,'e voce possui obesidade de grau 3!')