#Ex01.: Altera item da lista
def ex01():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    print(list_prod)
    list_prod[0] = 'PC'
    print(f'Alterar o primeiro elemento {list_prod}')
    print(list_prod)

#Ex02.: Adiciona item na lista
def ex02():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    list_prod.append('WebCam')
    print(list_prod)

#Ex03.: Remove produto específico 
def ex03():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    print(list_prod)
    list_prod.remove('Teclado')
    print(list_prod)

#Ex04.: Remove o último item da lista
def ex04():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    print(list_prod)
    list_prod.pop()
    print(list_prod)

#Ex05.: Remove pelo índice
def ex05():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    print(list_prod)
    del list_prod[1]
    print(list_prod)

#Ex06.:
def ex06():
    list_prod = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
    for p in list_prod:
        print(p)