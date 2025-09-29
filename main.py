import json
from função import deposito, saque, mostrar_extrato, criarusuario, input_cpf, input_nome, input_data, input_endereco
from datetime import datetime

# Carregar banco
try:
    with open('banco_dio.json', 'r') as f:
        banco = json.load(f)
except FileNotFoundError:
    banco = {}

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
        if not banco:  # banco vem do JSON carregado
            print('\033[31mNenhum usuário cadastrado. Por favor, crie um usuário primeiro.\033[0m')
            continue
        cpf_acesso = input_cpf('Digite o CPF para acessar a conta: ')
        
        # Procurar usuário pelo CPF
        usuario_id = None
        for uid, dados in banco.items():
            if dados['cpf'] == cpf_acesso:
                usuario_id = uid
                break
        
        if usuario_id:
            print('\n\033[32mAcesso concedido!\033[0m\n')
            break  # sai do menu principal e vai para menu da conta
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
       deposito(usuario_id)    
    elif escolha == 2:
       saque(usuario_id)
    elif escolha == 3:
        mostrar_extrato(usuario_id)
    elif escolha == 4:
        print('Obrigado por usar nosso sistema, volte sempre!')
        break
    else:
        print('\n\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m\n')