#Ex01.: Dicionários
def ex01():
    pessoa_vazio = {} #dicionário vazio
    dict_pessoa = {}
    dict_pessoa['Nome'] = 'João'    
    dict_pessoa['Idade'] = 25
    dict_pessoa['Cidade'] = 'Niterói'
    print(dict_pessoa) #Printa o dicionário
    print(dict_pessoa['Cidade']) #Printa Niterói
    dict_pessoa['Profissão'] = 'Programador' #Criou a chave programador
    print(dict_pessoa['Profissão'])

#Ex02.: Alterando valor
def ex02():
    dict_pessoa = {}
    dict_pessoa['Nome'] = 'João'    
    dict_pessoa['Idade'] = 25
    dict_pessoa['Cidade'] = 'Niterói'
    print(dict_pessoa['Idade'])
    dict_pessoa['Idade'] = 18  #Altera o valor da chave idade
    print(dict_pessoa['Idade'])

#Ex03.: Deletando uma chave
def ex03():
    dict_pessoa = {}
    dict_pessoa['Nome'] = 'João'    
    dict_pessoa['Idade'] = 25
    dict_pessoa['Cidade'] = 'Niterói'
    print(dict_pessoa)
    del dict_pessoa['Cidade'] #Deleta a chave cidade e seu valor
    print(dict_pessoa)