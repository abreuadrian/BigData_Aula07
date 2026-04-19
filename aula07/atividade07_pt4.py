import os 
import time
#Atividade04
dict_aluno_media = {}
for i in range(15):
    nome = input(f'Informe o nome do {i+1}º aluno: ').capitalize().strip()
    list_notas = []
    for n in range(2):
        while True:
            try: 
                nota = float(input(f'Informe a {n+1} nota: '))
                break
            except ValueError:
                print('Erro. Por favor, digite uma nota válida')
        list_notas.append(nota)
    med = sum(list_notas) / 2
    dict_aluno_media[nome] = med
for x, y in dict_aluno_media.items():
    if y >= 7:
        print(f'{x} média: {y} = Aprovado')
    else:
        print(f'{x} média: {y} = Reprovado')

    
