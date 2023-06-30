def filtro_user(cad_cpf, users):
    retorno = ''
    for user in users:
        if cad_cpf == user['cpf']:
            print('existe cpf cadastrado')
            return user
        else:
            retorno = 'não existe cpf cadastrado'
    return retorno


lista = [{'nome': 'matheus', 'cpf': 1234},
         {'nome': 'pedro', 'cpf': 4567},
         {'nome': 'maria', 'cpf': 7890}
         ]
novo = int(input('teste: '))
resp = filtro_user(novo, lista)
print(resp)
