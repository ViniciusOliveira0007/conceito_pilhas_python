'''
fazer usando pilha um sistema que pegue um número e tranforme em binário
o usuário escreve um número e então o número é tranformado em binário
'''
valor = int(input('Digite um valor que será transformado em Binário:\n'))
numero_digitado = valor

lista_binario = []

if valor == 0:
    lista_binario.append(0)

while valor > 0:
    resto = valor % 2  
           
    lista_binario.append(resto) 
    print(lista_binario)
    valor = valor // 2        

lista_binario.reverse()
print(f"O número {numero_digitado} em binário é: {lista_binario}")

