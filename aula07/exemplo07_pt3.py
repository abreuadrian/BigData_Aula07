#Ex01.:
def ex01():
    list_vendas = []

    for i in range(10):
        venda = float(input(f'Informe o valor da {i+1}ª venda: '))
        list_vendas.append(venda)
    print(f'\nTodas as vendas: {list_vendas}')

    for c in list_vendas:
        if c >= 1000:
            print(f'{list_vendas.index(c)+1}ª venda: Meta Batida! - Valor: R${c:.2f}')
        elif c >= 700:
            print(f'{list_vendas.index(c)+1}ª venda: Quase! - Valor: R${c:.2f}')
        else:
            print(f'{list_vendas.index(c)+1}ª venda: Abaixo do esperado! - Valor: R${c:.2f}')

