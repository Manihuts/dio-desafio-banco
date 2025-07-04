menu = """
    -=-=- BANCO PYTHON -=-=-
    Seja bem-vindo(a), qual
    operação deseja fazer?

    1. Depositar
    2. Sacar
    3. Ver extrato
    4. Sair

    -=-=- -=-=- -=-=- -=-=-
"""

saldo = 0
limite = 500
num_saques = 0
LIMITE_SAQUES = 3
extrato = ""
contador_depositos = 1
contador_saques = 1

while True:
    operacao = input(menu).strip()

    if operacao == "1": ## Depósito
        try:
            montante = float(input("Quanto deseja depositar? => "))
        except:
            print("[Erro] :: O valor de depósito inserido não é um número.")
            continue

        if montante <= 0:
            print("[Operação inválida] :: Valor de depósito é zero ou negativo.")
        else:
            saldo += montante
            extrato += f"Depósito {contador_depositos} => R${montante:.2f} \n"
            contador_depositos += 1
    
    elif operacao == "2": ## Saque
        try:
            montante = float(input("Quanto deseja sacar? => "))
        except:
            print("[Erro] :: O valor de saque inserido não é um número.")
            continue

        if num_saques == LIMITE_SAQUES:
            print("[Operação inválida] :: Você atingiu o limite de saques diários.")
        elif montante <= 0:
            print("[Operação inválida] :: Valor de saque é zero ou negativo.")
        elif montante > limite:
            print("[Operação inválida] :: O valor de saque excede o limite de R$500.")
        elif montante > saldo:
            print("[Operação inválida] :: Você não possui saldo suficiente para realizar o saque.")
        else:
            saldo -= montante
            num_saques += 1
            extrato += f"Saque {contador_saques} => R${montante:.2f} \n"
            contador_saques += 1

    elif operacao == "3": ## Ver extrato
        print("Extrato atual: ")
        if not extrato:
            print("Por enquanto não houveram operações!")
            print(f"Saldo => R${saldo:.2f}")
        else: 
            print(extrato)
            print("===================")
            print(f"Saldo => R${saldo:.2f}")

    elif operacao == "4":
        print("Obrigado pela confiança, até mais!")
        break

    else:
        print("Opção inválida, escolha novamente!")