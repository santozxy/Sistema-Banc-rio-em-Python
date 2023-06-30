
def menu():
    return '''
===============MENU====================
[D]-Depositar           [S]-Sacar               [E]-Extrato
[U]-Novo Usuário      [CC]-Criar Conta     [LS]-Listar Contas
[Q]-Sair
'''


# Função depositar
def depositar(dep, ext, sld):
    if dep > 0:  # caso o depósito seja maior que zero
        sld += dep  # adiciona o valor do deposito no saldo da conta
        ext = ext + f'Depósito de: R${dep:.2f}\n'  # registra no extrato a operação realizada
        print(f'\nDepósito de R${dep:.2f} realizado!')
    else:  # se o valor não for maior que zero retorna erro
        print(f'\nValor de depósito incompatível!\nReinicie a operação.')
    return ext, sld  # retorna o valor atualizado para as variáveis extrato e saldo


# Função sacar
def sacar(*, saque1, saldo1, n_saques1, extrato1, limite1, lim_saque1):
    if 0 < saque1 <= saldo1 and saque1 <= limite1:  # verifica se o saque é maior igual que zero e menor igual ao saldo
        if n_saques1 <= lim_saque1:  # verifica se o número de saques do dia é menor que o limite por dia
            saldo1 -= saque1  # subtrai o valor do saque no total do saldo
            print('\nOperação realizada com sucesso.\nRetire o valor na boca do caixa!')
            extrato1 = extrato1 + f'Saque de: R${saque1:.2f}\n'  # registra no extrato a operação realizada
            n_saques1 += 1  # adiciona 1 no número total de saques realizados no dia
        else:  # verifica se excedeu o limite de saques, encerra e reinicia o processo
            print('\nLimite de 3 saques excedido!\nOperação cancelada.')
    elif saque1 > limite1:  # verifica se o valor do saque é maior que o limite em conta disponível
        print('\nValor indisponível\nPermitido somente R$500,00 por saque.')
    else:  # verifica se o valor do saque é maior que o saldo ou menor igual a zero
        print('\nNão é possível sacar esta quantia!')
    return saldo1, extrato1, n_saques1


def extract(saldo, *, extrato2):
    mostra = f'\n========================' \
             f'\n         Saldo: {saldo}\n\n' \
             f'== == == == == == == == == =='\
             f'\n         {extrato2}'\
             f'\n========================'
    return mostra


def criar_user(users):
    cad_cpf = int(input('\nDigite o CPF (somente números): '))
    validacao = filtro_user(cad_cpf, users)
    if validacao:
        print('\n== Usuário já cadastrado! ==')
        return
    else:
        nome = input('\nDigite o nome do novo usuário: ')
        data_nascimento = input('\nDigite a data de nascimento (dd-mm-ano): ')
        endereco = input('\nDigite o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
        users.append({'cpf': cad_cpf, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco})
        print('\nNovo usuário cadastrado com sucesso!')
        return users


def filtro_user(cad_cpf, users):
    for user in users:
        if user['cpf'] == cad_cpf:
            return user
    return


def criar_conta(numero_conta, agencia, users):
    if not users:
        teste = input('\nNão existem usuários criados para vincular conta.\n\nDeseja cadastrar novo usuário? S/N ').upper()
        if teste == 'S':
            criar_user(users)
            return
    else:
        cad_cpf = int(input('\nDigite o CPF (somente números): '))
        user = filtro_user(cad_cpf, users)
        if user:
            print('\nConta cadastrada com sucesso!')
            return {'agencia': agencia, 'num_conta': numero_conta, 'usuário': user}
        else:
            print('\nUsuário não localizado, operação encerrada.')
            return


def listar_contas(contas):
    if contas:
        for conta in contas:
            print(f'''
                Agência:    {conta['agencia']}
                C/C:          {conta['num_conta']}
                Titular:      {conta['usuário']['nome']}
            ''')
    else:
        return


def main():
    limite_saque = int(2)
    saldo = float(0.0)  # inicia a variável saldo como zerada
    extrato = ''  # inicia a variável extrato sem texto algum
    limite = float(500.0)  # define o limite diário de saque em 500 reais
    n_saques = int(0)  # inicia variável de contagem do número de saques zerada
    users = []
    contas = []
    agencia = '0001'
    while True:  # inicia um loop infinito
        operation = input(menu()).upper()  # entrada de dados da operação desejada no menu
        if operation == 'D':  # condição para operação de depósito
            deposito = float(input('\nDigite o valor do depósito: '))  # recebe o valor do depósito
            extrato, saldo = depositar(deposito, extrato, saldo)  # chama a função depositar atribuindo o retorno nas variáveis extrato e saldo
        elif operation == 'S':  # condição para operação de saque
            saque = float(input('\nDigite o valor do saque: '))
            saldo, extrato, n_saques = sacar(
                saque1=saque, saldo1=saldo, n_saques1=n_saques, extrato1=extrato, limite1=limite, lim_saque1=limite_saque,
            )  # chama a função sacar
        elif operation == 'E':  # condição para operação de saque
            print(extract(saldo, extrato2=extrato,))  # chama as variáveis que armazena o saque e o extrato
        elif operation == 'U':
            criar_user(users)
        elif operation == 'CC':
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, agencia, users)
            if conta:
                contas.append(conta)
        elif operation == 'LS':
            listar_contas(contas)
        elif operation == 'Q':  # condição para saída do 'loop' infinito
            break  # encerra o loop infinito
        else:
            print('\n\nOpção inválida, digite novamente.')


main()
