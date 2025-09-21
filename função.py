saldo = 0
saqueDiario = 0
extrato = []
#função do deposito
def deposito(saldo, extrato):
    valor = float(input('Digite o valor do depósito: R$ '))
    if valor <= 0:
        print('\033[31mOperação falhou! Não é possível depositar valores negativos ou zero.\033[0m')
    else:
        saldo += valor
        extrato.append( f'Depósito: R$ {valor:.2f}')
        print(f'\033[32mDepósito de R$ {valor:.2f} realizado com sucesso\033[0m')
    return saldo, extrato
#função do saque
def saque(saldo, extrato, saqueDiario):
    if saqueDiario >= 3:
        print('\033[31mOperação falhou! você atingiu o limite de saques diários.\033[0m\n')
        return saldo, extrato, saqueDiario
    
    valor = float(input('Digite o valor do saque: R$ '))
    
    if valor > saldo:
        print('\033[31mOperação falhou! Você não tem saldo suficiente.\033[0m')
    elif valor > 500:
        print('\033[31mOperação falhou! Saque máximo de R$500.\033[0m')
    elif valor <= 0:
        print('\033[31mOperação falhou! Valor inválido.\033[0m')
    else:
        saldo -= valor
        extrato.append(f'Saque: R$ {valor:.2f}')
        saqueDiario += 1
        print(f'\033[32mSaque de R$ {valor:.2f} realizado com sucesso\033[0m')
    return saldo, extrato, saqueDiario
    
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
        
while True:    
    escolha = int(input(''' Escolha uma das opções abaixo:
                            
            [1] - depositar
            [2] - sacar
            [3] - extrato
            [4] - sair
            
        digite a opção desejada: '''))
    
    #execução da escolha
    if escolha == 1:
        saldo, extrato = deposito(saldo, extrato)
    elif escolha == 2:
        saldo, extrato, saqueDiario = saque(saldo, extrato, saqueDiario)
    elif escolha == 3:
        mostrar_extrato(saldo, extrato)
    elif escolha == 4:
        print('Obrigado por usar nosso sistema, volte sempre!')
        break
    else:
        print('\n\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[0m\n')