V = float(input("Insira o valor que desejas investir: "))
i = float(input("Insira a taxa de juros mensal: "))
k = 12
S = 0
continuar = True

while(continuar):
    for j in range(1,k+1):
        S = S+V
        S = S*(1+(i/100))
    print("Seu saldo do investimento após de ano é: {:.2f}".format(S))
    r = ((S-k*V)/(k*V))*100
    print("Seu rendimento em relaçao ao total investido é: {: .2f}%".format(r))
    op = input("Deseja processar mais um ano? (S/N) -->  ").lower()

    if op == "n" or op == "nao" or op == "não":
        continuar = False
        print("Obrigado por utilizar nosso programa! Até a próxima!")
    elif op != "s" and op != "sim":
        print("Resposta inválida, até a próxima")
        continuar = False
    print ("Fim do programa")