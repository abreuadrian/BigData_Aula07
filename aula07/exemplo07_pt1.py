#Ex01.: (Lista)
def ex01():
    list_vazia_meses = []
    list_meses = []
    for i in range(12):
        meses = input(f'Escreva o nome do {i+1}º mês: ')
        list_meses.append(meses)
    print(list_meses)

#Ex02.:
def ex02():
    list_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
    print(list_meses[0]) #Primeiro item da lista
    print(list_meses[2]) #Terceiro (2º índice) item da lista
    print(list_meses[-1]) #Último índice da lista
    print(list_meses[-2]) #Penúltimo índice da lista
    print(len(list_meses)) #Conta quantos índices a lista possui

#Ex03.: Fatiamento de lista
def ex03():
    list_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
    print(list_meses[:4]) #['Janeiro', 'Fevereiro', 'Março', 'Abril']
    print(list_meses[2:]) #['Março', 'Abril', 'Maio', 'Junho']
    print(list_meses[2:4]) #['Março', 'Abril']

