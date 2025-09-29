from datetime import datetime

saldo = 0
MovimentacaoDiario = 0  
extrato = []
ultima_data = datetime.now().date()
usuario = []

def criarusuario(nome, data_nascimento, cpf, endereco):
    for u in usuario:
        if u['cpf'] == cpf:
            print('\033[31mJá existe um usuário com esse CPF!\033[0m')
            return None
        
    novo_usuario = {'nome': nome,
               'data_nascimento': data_nascimento,
               'cpf': cpf,
               'endereco': endereco}
    usuario.append(novo_usuario)
    print('\n\033[32mUsuário criado com sucesso!\033[0m\n')
    return usuario
    
#checkl da movimentação diária
def checar_limite_diario(MovimentacaoDiario, ultima_data):
    data_atual = datetime.now().date()
    if data_atual != ultima_data:
        MovimentacaoDiario = 0
        ultima_data = data_atual
    return MovimentacaoDiario, ultima_data

#função do deposito
def deposito(saldo, extrato, MovimentacaoDiario, ultima_data):
    MovimentacaoDiario, ultima_data = checar_limite_diario(MovimentacaoDiario, ultima_data)
    if MovimentacaoDiario >= 10:
        print('\033[31mOperação falhou! você atingiu o limite de movimentações diários, volte amanhã...\033[0m\n')
        return saldo, extrato, MovimentacaoDiario, ultima_data
    valor = float(input('Digite o valor do depósito: R$ '))
    if valor <= 0:
        print('\033[31mOperação falhou! Não é possível depositar valores negativos ou zero.\033[0m')
    else:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        extrato.append(f'{data_hora} - Deposito: R$ {valor:.2f}')
        print(f'\033[32mDepósito de R$ {valor:.2f} realizado com sucesso\033[0m')
        MovimentacaoDiario += 1
    return saldo, extrato, MovimentacaoDiario, ultima_data

#função do saque
def saque(saldo, extrato, MovimentacaoDiario, ultima_data):
    MovimentacaoDiario, ultima_data = checar_limite_diario(MovimentacaoDiario, ultima_data)
    if MovimentacaoDiario >= 10:
        print('\033[31mOperação falhou! você atingiu o limite de movimentações diários, volte amanhã...\033[0m\n')
        return saldo, extrato, MovimentacaoDiario, ultima_data
    
    valor = float(input('Digite o valor do saque: R$ '))
    
    if valor > saldo:
        print('\033[31mOperação falhou! Você não tem saldo suficiente.\033[0m')
    elif valor > 500:
        print('\033[31mOperação falhou! Saque máximo de R$500.\033[0m')
    elif valor <= 0:
        print('\033[31mOperação falhou! Valor inválido.\033[0m')
    else:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        extrato.append(f'{data_hora} - Saque: R$ {valor:.2f}')
        MovimentacaoDiario += 1
        print(f'\033[32mSaque de R$ {valor:.2f} realizado com sucesso\033[0m')
    return saldo, extrato, MovimentacaoDiario, ultima_data

#função que mostra o extrato     
def mostrar_extrato(saldo, extrato):
    print('\n================ EXTRATO ================')
    if not extrato:
        print('\033[31mNão foram realizadas movimentações.\033[0m')
    else:
        for mov in extrato:
            print(mov)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('=========================================')
  
#nome  

def input_nome():
    while True:
        nome = input('Digite o seu nome do usuário: ').strip()
        nome = ' '.join(nome.split())
        
        if nome and all(ch.isalpha() or ch.isspace() for ch in nome):
            return nome.title()  # primeira letra maiúscula
        print("Nome inválido! Use apenas letras e espaços.")

#data de nascimento
def input_data():
    while True:
        data = input('Digite a data de nascimento (dd/mm/aaaa): ').strip()
        if len(data) == 10 and data[2] == '/' and data[5] == '/':
            try:
                dia = int(data[0:2])
                mes = int(data[3:5])
                ano = int(data[6:10])

                if 1 <= mes <= 12 and 1 <= dia <= 31:
                    if mes in [4, 6, 9, 11] and dia > 30:
                        print("❌ Este mês tem apenas 30 dias!")
                        continue
                    elif mes == 2 and dia > 29:
                        print("❌ Fevereiro tem no máximo 29 dias!")
                        continue
                    # Se chegou aqui, data é válida
                    return data
                else:
                    print("❌ Dia ou mês fora do intervalo válido!")
            except ValueError:
                print("❌ Use apenas números na data!")
        else:
            print("❌ Formato deve ser dd/mm/aaaa!")

#CPF
def input_cpf(cpf):
    while True:
        cpf = input('Digite o CPF (somente números): ').strip() 
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
#Endereço
def input_endereco():
    while True:
        endereco = input('Digite o endereço: ').strip()
        if len(endereco) >= 5:
            return endereco
        print("❌ Endereço muito curto! Digite um endereço completo.")

while True:
    print('''\n==================== MENU ====================
    [1] - Criar usuário
    [2] - Acessar conta existente
    [3] - Sair
    =============================================''')
    
    opcao = input('Escolha uma das opções acima: ')
    
    if opcao == '1':
        nome = input_nome()
        data_nascimento = input_data()
        cpf = input_cpf('')
        endereco = input_endereco()
        criarusuario(nome, data_nascimento, cpf, endereco)
        
    elif opcao == '2':
        if not usuario:
            print('\033[31mNenhum usuário cadastrado. Por favor, crie um usuário primeiro.\033[0m')
            continue
        cpf_acesso = validar_cpf('Digite o CPF para acessar a conta: ')
        usuario_encontrado = any(u['cpf'] == cpf_acesso for u in usuario)
        if usuario_encontrado:
            print('\n\033[32mAcesso concedido!\033[0m\n')
            break
        else:
            print('\033[31mUsuário não encontrado. Verifique o CPF e tente novamente.\033[0m')
            
    elif opcao == '3':
        print('Obrigado por usar nosso sistema, volte sempre!')
        exit()
        
    else:
        print('\033[31mOpção inválida! Tente novamente.\033[0m')


while True:
    escolha = int(input(''' Escolha uma das opções abaixo:
                            
            [1] - depositar
            [2] - sacar
            [3] - extrato
            [4] - sair
            
        digite a opção desejada: '''))
    
    #execução da escolha
    if escolha == 1:
        saldo, extrato, MovimentacaoDiario, ultima_data = deposito(saldo, extrato, MovimentacaoDiario, ultima_data)    
    elif escolha == 2:
        saldo, extrato, MovimentacaoDiario, ultima_data = saque(saldo, extrato, MovimentacaoDiario,ultima_data)
    elif escolha == 3:
        mostrar_extrato(saldo, extrato)
    elif escolha == 4:
        print('Obrigado por usar nosso sistema, volte sempre!')
        break
    else:
        print('\n\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m\n')