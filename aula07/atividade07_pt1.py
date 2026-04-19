#Atividade01
def nums(n=10):
    list_nums = []
    for i in range(n):
        while True:
            try:
                num = int(input(f'Informe o {i+1}º número: '))
                break
            except ValueError:
                print('ERRO. Insira um número válido')
        list_nums.append(num)
    return list_nums

def even_odd(nums):
    list_even = []
    list_odd = []
    for c in nums:
        if c % 2 == 0:
            list_even.append(c)
        else: 
            list_odd.append(c)
    return list_even, list_odd

def show_even_odds(evens, odds):
    return f'Números pares: {evens}\nNúmeros impares: {odds}'

even, odd = even_odd(nums())
print(show_even_odds(even, odd))

        
