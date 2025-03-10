LIMITE_POR_SAQUE = 500.00
saldo = 0
LIMITE_DE_SAQUE = 3
extrato = ''
numero_de_saque = 0
valor = 0
usuarios = []
contas = []
AGENCIA = "0001"

def chamar_menu():
    LIMITE_POR_SAQUE = 500.00
    LIMITE_DE_SAQUE = 3
    saldo = 0
    extrato = ''
    numero_de_saque = 0
    valor = 0

    menu = '''
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [nu] Criar novo Usuario
        [nc] Criar nova conta
        [lc] Listar contas
    
    '''
    while True:
        print(menu)
        opcao = input('Escolha uma opção: ')
        
        if opcao == 'd':
            valor = float(input('\nDigite o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input('\nDigite o valor do saque: '))
            saldo, extrato,numero_de_saque = sacar(saldo = saldo,valor = valor,extrato = extrato,numero_de_saque = numero_de_saque)
            
    
        elif opcao == 'e':
            ver_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao =='nc':
            numero_da_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        else:
            print("\nOpção invalida, por favor, digite uma opção válida\n")

            break

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        print("\nValor depositado com sucesso.")
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("\nImpossível depositar valor desejado.")
    return saldo, extrato

def sacar(saldo=saldo, valor=valor, extrato=extrato, numero_de_saque=numero_de_saque):
    if numero_de_saque < LIMITE_DE_SAQUE:
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
    return saldo, extrato, numero_de_saque

def ver_extrato(saldo, /, *, extrato = extrato):
    print('\n========== Extrato ==========\n')
    print('Não foi realizado movimentações!\n' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}\n')
    print('=============================\n')

def criar_usuario(usuarios):
    cpf = (input("Informe o CPF (Somente números)"))
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("CPF já existe, por favor, informe outro CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro- cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
    return usuarios

def criar_conta(AGENCIA, numero_da_conta, usuarios):
    cpf = input(("Informe o CPF do usuário a qual deseja vincular a conta: "))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"Agencia": AGENCIA, "numero_da_conta": numero_da_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de contas cancelados. Cadastre o usuario antes de criar a conta. ")

    
def filtrar_usuarios(cpf, usuarios_list):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['Agencia']}
        C/C:\t{conta['numero_da_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(linha)

chamar_menu()
