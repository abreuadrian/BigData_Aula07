#Atividade02
def contatos(n_contact=5):
    list_contatos = []
    for i in range(n_contact):
        dict_contatos = {}
        dict_contatos['Nome'] = input(f'Informe o nome do {i+1}º contato: ').capitalize().strip()
        dict_contatos['Telefone'] = input(f'Informe o telefone do {i+1}º contato: ')
        dict_contatos['Email'] = input(f'Informe o email do {i+1}º contato: ')
        list_contatos.append(dict_contatos)
    return list_contatos

def display(contacts):
    for c in contacts:
        print(f'\n{c['Nome']} - {c['Telefone']} - {c['Email']}')

display(contatos())
