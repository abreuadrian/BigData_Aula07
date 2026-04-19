#Atividade03
def candidatos(num_candidatos):
    list_candidatos = []
    for i in range(num_candidatos):
        dict_candidatos = {}
        dict_candidatos['Nome'] = input(f'Informe o nome do {i+1}º candidato: ')
        while True:
            try:
                dict_candidatos['Idade'] = int(input(f'Informe a idade do {i+1}º candidato: '))
                break
            except ValueError:
                print('Por favor digite sua idade')    
        dict_candidatos['Telefone'] = input(f'Informe o telefone do {i+1}º candidato: ')
        dict_candidatos['E-mail'] = input(f'Informe o email do {i+1}º candidato: ')
        dict_candidatos['Formação'] = input(f'Informe a formação academica do {i+1}º candidato: ')
        list_candidatos.append(dict_candidatos)
    return list_candidatos

def verificar_idade(candidatos):
    for c in candidatos:
        if c['Idade'] >= 18:
            print(c)
        
lista_candidatos = candidatos(2)
verificar_idade(lista_candidatos)
