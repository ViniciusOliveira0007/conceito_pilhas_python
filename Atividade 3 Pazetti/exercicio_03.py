'''
Inserir 5 elementos na fila,
imprimir a fila
remover dois elementos, e se é uma fila então será os 2 primeiros 
imprimir a fila
Inserir 2 elementos na fila,
imprimir a fila

'''

lista = []
contador = 0
while contador != 5:
    contador += 1
    valor = int(input(f'Digite o valor número {contador}:\n'))
    lista.append(valor)

print('-' * 20)
print('Retornando os valores em formato de Fila:')
print(*lista)

lista.pop(0)
lista.pop(0)
print(*lista)


print('-' * 20)
print('Adicionando novos valores na Fila:')

contador = 0
while contador != 2:
    contador += 1
    valor = int(input(f'Digite o valor número {contador}:\n'))
    lista.append(valor)
print(*lista)
