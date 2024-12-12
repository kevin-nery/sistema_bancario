menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

'''

LIMITE_POR_SAQUE = 500.00
saldo = 0
LIMITE_DE_SAQUE = 3
extrato = ''
numero_de_saque = 0

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('\nDigite o valor do depósito: '))
        if valor > 0:
            print("\nValor depositado com sucesso.")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nImpossível depositar valor desejado.")
    
    elif opcao == 's':
        
        if numero_de_saque < LIMITE_DE_SAQUE:
            valor = float(input("\nDigite o valor que deseja sacar: "))
            if valor <= saldo and valor <= LIMITE_POR_SAQUE:
                saldo -= valor
                print(f'\nValor R$ {valor:.2f} sacado.')
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saque += 1
            elif valor > LIMITE_POR_SAQUE:
                print(f'\nNão foi possível realizar saque. \nSeu limite de valor para saque é de: R$ {LIMITE_POR_SAQUE:.2f}')
            else:
                print('\nSaldo Insuficiente.')
        else:
            print('\nLimite de saques diário atingido.')
    elif opcao == 'e':
        print('\n========== Extrato ==========\n')
        print('Não foi realizado movimentações!\n' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}\n')
        print('=============================\n')
    elif opcao =='q':
        break
    else:
        print("\nOpção invalida, por favor, digite uma opção válida\n")