#Atividade04
def situation(med):
    return 'Aprovado' if med >= 7 else 'Reprovado'

def calc_media(n1, n2):
    return (n1 + n2) / 2

def validar_nota(txt,min=0.0, max=10):
    while True:
        try:
            n = float(input(txt))
            if min <= n <= max: 
                return n
            else: print(f'A nota deve estar entre {min} e {max}')
        except ValueError:
            print('ERRO. Informe uma nota válida')
            
def display(nome, media, situation):
    return f'Aluno: {nome} - Média: {media:.1f} - Situação: {situation}'

def alunos_notas(qnt_alunos=3):
    list_relatorio = []
    for i in range(qnt_alunos): 
        nome = input(f'Informe o nome do {i+1}º aluno: ').capitalize().strip()
        n1 = validar_nota('Informe a 1ª nota: ')
        n2 = validar_nota('Informe a 2ª nota: ')
        media = calc_media(n1, n2)
        situacao = situation(media)
        list_relatorio.append({
            'Nome': nome,
            '1ª nota': n1,
            '2ª nota': n2,
            'Média': media,
            'Situação':situacao})
    for a in list_relatorio:
        print(display(a['Nome'], a['Média'], a['Situação']))

if __name__ == '__main__':
    alunos_notas()