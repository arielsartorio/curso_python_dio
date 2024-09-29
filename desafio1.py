menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite_saque = 500.0
extrato = ""
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

def depositar (valor):
    global saldo
    global extrato
    if valor > 0:
        saldo += valor
        extrato += f"R$ {valor:.2f}\n"
        return True
    else:
        print("Não é possível depositar valor negativo!")
        return False
    
def sacar (valor):
    global saldo
    global extrato
    global numero_saques
    if numero_saques < LIMITE_NUMERO_SAQUES:
        if valor <= limite_saque:
            if valor <= saldo:
                saldo -= valor
                extrato += f"-R$ {valor:.2f}\n"
                numero_saques += 1
                return True
            else:
                print("Não há saldo suficiente na conta.")
                return False
        else:
            print("Valor desejado acima do limite para saque.")
            return False
    else:
        print("Limite de saques diário excedido.")
        return False

def imprime_extrato ():
    global extrato
    print(extrato)
    return

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor para depositar: "))
        if depositar(valor = deposito):
            print("Depósito realizado com sucesso!")

    elif opcao == "s":
        saque = float(input("Digite o valor para sacar: "))
        if sacar(valor = saque):
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        imprime_extrato()

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção do menu!")