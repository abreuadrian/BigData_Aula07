#Ex01.:
def ex01():
    list_livros = []

    for i in range(10):
        print(f'\n{i+1}º Livro\n')
        dict_livro = {}
        dict_livro['Título'] = input('Informe o título do livro: ')
        dict_livro['Autor'] = input('Informe o autor do livro: ')
        dict_livro['Ano'] = int(input('Informe o ano de publicação: '))
        dict_livro['Gênero'] = input('Informe o gênero do livro: ')
        dict_livro['Páginas'] = int(input('Número de páginas: '))
        list_livros.append(dict_livro)
        print('\nLivro Cadastrado')

    print('\nLivros a partir de 2020:')
    for c in list_livros:
        if c['Ano'] >= 2020:
            print(f'{c['Nome']} - {c['Ano']}') 
ex01()