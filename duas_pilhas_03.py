'''
Tem uma pilha com 10 elementos inteiros e tenho que fazer uma segunda que não tenha elementos repetidos da primeira pilha

'''


print('-'* 10 +'\tDigite 10 elementos para a pilha 1\t'+10*'-')
contador = 0
lista_pilha_01 = []
lista_pilha_02 = []



while contador < 10:
    contador += 1
    valor = input(f'Digite o {contador}ª valor da pilha:\n')
    lista_pilha_01.append(valor)


for i in lista_pilha_01:
    if i in lista_pilha_01 and i in lista_pilha_02:       
        pass
    else:
        lista_pilha_02.append(i)
        
lista_pilha_02.sort()
print('A lista sem números repetidos:')
print(lista_pilha_02)