print('**************Calculadora**************')


def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

print('\nSelecione a opção desejada: \n')
print('1-- Adição')
print('2-- Multiplicação')
print('3-- Subtração')
print('4-- Divisão')

escolha = input('\nDigite a opção desejada: ')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if escolha == '1':
    print('\n')
    print(num1, '+', num2, '=', add(num1, num2))
    print('\n')

elif escolha == '2':
    print('\n')
    print(num1, '*', num2, '=', multiply(num1, num2))
    print('\n')

elif escolha == '3':
    print('\n')
    print(num1, '-', num2, '=', subtract(num1, num2))
    print('\n')

elif escolha == '4':
    print('\n')
    print(num1, '/', num2, '=', divide(num1, num2))
    print('\n')

else:
    print('Opção Inválida!!')
