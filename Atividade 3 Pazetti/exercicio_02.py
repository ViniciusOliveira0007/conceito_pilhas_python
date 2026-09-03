'''
Fazer o usuário inserir 5 valores na fila, 
imprimir a fila
mostrar o maior valor dentro da fila 
mostrar o menor valor dentro da fila 

fazer a conta de média dos valores para mostrar a diferença entre a média e o maior valor da fila
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


print('-' * 20)
maior_valor = max(lista)
print(f'Maior valor dentro da fila: {maior_valor}')
menor_valor = min(lista)
print(f'Menor valor dentro da fila: {menor_valor}')

valor_total = 0
for i in lista:
    valor_total += i

quantidade = len(lista)
media = int(valor_total) / int(quantidade)

print(f'A média é {media}')
print(f'Com a diferença de {maior_valor - media}')    