'''
Inserir 10 valores e retornar em formato de fila e de pilha 

'''


lista = []
contador = 0
while contador != 10:
    contador += 1
    valor = input(f'Digite o valor número {contador}:\n')
    lista.append(valor)


print('-' * 20)
print('Retornando os valores em formato de Fila:')
print(*lista)
lista.reverse()

print('-' * 20)
print('Retornando os valores em formato de Pila:')
print(*lista)