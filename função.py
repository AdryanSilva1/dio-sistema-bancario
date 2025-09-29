import json
from datetime import datetime

try: 
    with open('banco_dio.json', 'r') as f:
        banco = json.load(f)
except FileNotFoundError:
    banco = {}

#salvar dados no banco
def salvar_banco():
    with open('banco_dio.json', 'w') as f:
        json.dump(banco, f, indent=4)
        
#função de criar usuário
def criarusuario(nome, data_nascimento, cpf, endereco):
    for u in banco.values():
        if u['cpf'] == cpf:
            print('\033[31mJá existe um usuário com esse CPF!\033[0m')
            return None
    novoId = str(max([int(i) for i in banco.keys()], default=1000) + 1)
    banco[novoId] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
            "saldo": 0,
            "extrato":[],
            "movimentacao_diario":0,
            "ultima_data": str(datetime.now().date())}
    salvar_banco()
    print('\n\033[32mUsuário criado com sucesso!\033[0m\n')
    return novoId
    
#função do deposito
def deposito(usuario_id):
    u = banco[usuario_id]
    
    dta_atual = str(datetime.now().date())
    if u["ultima_data"] != dta_atual:
        u['movimentacao_diario'] = 0
        u['ultima_data'] = dta_atual
        
    if u['movimentacao_diario'] >= 10:
        print('\033[31mOperação falhou! você atingiu o limite de movimentações diários, volte amanhã...\033[0m\n')
        return
    
    valor = float(input('Digite o valor do depósito: R$ '))
    if valor <= 0:
        print('\033[31mOperação falhou! O valor informado é inválido.\033[0m')
        return
    u['saldo'] += valor
    u['extrato'].append(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - Depósito: R$ {valor:.2f}')
    u['movimentacao_diario'] += 1
    salvar_banco()
    print(f'\033[32mDepósito de R$ {valor:.2f} realizado com sucesso\033[0m')
    return

#função do saque
def saque(usuario_id):
    u = banco[usuario_id]
    
    data_atual = str(datetime.now().date())
    if u["ultima_data"] != data_atual:
        u['movimentacao_diario'] = 0
        u['ultima_data'] = data_atual
        
    if u['movimentacao_diario'] >= 10:
        print('\033[31mOperação falhou! você atingiu o limite de movimentações diários, volte amanhã...\033[0m\n')
        return
    
    valor = float(input('Digite o valor do saque: R$ '))
    limite = 500
    
    if valor <= 0:
        print('\033[31mOperação falhou! O valor informado é inválido.\033[0m')
        return
    elif valor > u['saldo']:
        print('\033[31mOperação falhou! Saldo insuficiente.\033[0m')
        return
    elif valor > limite:
        print('\033[31mOperação falhou! O valor do saque excede o limite de R$ 500,00.\033[0m')
        return
    
    u['saldo'] -= valor
    u['extrato'].append(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - Saque: R$ {valor:.2f}')
    u['movimentacao_diario'] += 1
    salvar_banco()
    print(f'\033[32mSaque de R$ {valor:.2f} realizado com sucesso\033[0m')
    return

#função que mostra o extrato     
def mostrar_extrato(usuario_id):
    u = banco[usuario_id]
    print("\n================ EXTRATO ================")
    if not u["extrato"]:
        print('\033[31mNão foram realizadas movimentações.\033[0m')
    else:
        for mov in u["extrato"]:
            print(mov)
    print(f"\nSaldo: R$ {u['saldo']:.2f}")
    print("=========================================")

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