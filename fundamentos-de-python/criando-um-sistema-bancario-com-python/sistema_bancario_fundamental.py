'''
Versão Fundamental de um sistema bancário Python. 
'''

#Criar um menu
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

#Inicializar
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
operacoes = []

#Loop de verificação contínua
while True:
    #Selecionar Operação
    opcao = input(menu)
    #Depositar
    if opcao == "d":
        print("Depósito")
        #Receber valor
        valor = float(input("\nInsira o valor desejado: "))
        #Verificar se positivo
        if valor > 0:
            #Receber valor, armazenar em lista, incrementar saldo
            deposito = valor
            operacoes.append(deposito)
            saldo += deposito
            print("\nOperação realizada com sucesso!")
        else:
            print("\nOperação falhou, o valor informado é inválido")
    #Sacar
    elif opcao == "s":
        print("Saque")
        #Verificar número de saques permitidos
        if numero_saques<LIMITE_SAQUES:
            #Receber valor
            saque = float(input("\nInsira o valor desejado: "))
            #Verificar se positivo
            if saque > 0:
                #Verificar se tem saldo
                if saque <= saldo:
                    #Verificar se dentro do limite de saque
                    if saque<=limite:
                        #Armezenar em lista, decrementar saldo, incrementar numero de saque
                        operacoes.append(-saque)
                        saldo -= saque
                        numero_saques += 1
                        print("\nOperação realizada com sucesso!")
                    else:
                        print("\nLimite de saque excedido!")
                else:
                    print("\nSaldo insuficiente!")
            else:
                print("\nOperação falhou, o valor informado é inválido!")
        else:
            print("\nNúmero de saques diários excedido!")
    #Extrato
    elif opcao == "e":
        print(" Extrato ".center(35, "="))
        print("\nDepósitos:\n")
        #Verificar depósitos
        depositos = [operacao for operacao in operacoes if operacao>0]
        if depositos:
            for item_extrato in depositos:
                print(f"+ R${item_extrato: .2f}")
        else:
            print("Nenhum depósito registrado.")
        print("\nSaques:\n")
        #Verifcar saques
        saques = [operacao for operacao in operacoes if operacao<0]
        if saques:
            for item_extrato in saques:
                print(f"- R${abs(item_extrato): .2f}\n")
        else:
            print("Nenhum saque registrado.")
        print(f"\nSeu saldo é: R${saldo: .2f}\n\nOperação realizada com sucesso!")
        print("\n"*2 + "="*35 + "\n")

    #Sair
    elif opcao == "q":
        break

    #Erro
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
