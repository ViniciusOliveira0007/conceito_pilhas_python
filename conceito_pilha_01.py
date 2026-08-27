''' 
Primeiro jeito:
    preciso que o usuário digite todos os números primeiro e depois as operações
    e então faça as operações em sequência conforme foram digitadas
    igual está no powerpoint do professor.
Segundo jeito:
    Preciso que o usuário escreva duas variaveis primeiro e sua operação em seguida,
    assim acrescentando novas variaveis e operações em seguida se quiser, uma de cada vez
    igual que  foi feito em sala no caderno.
    
'''
'''
limite = int(input("Quantos valores terá sua expressão:\n"))
contador = 0
lista_valores =[]

while contador < limite:
    contador += 1
    valor = int(input(f'digite o {contador}ª valor:\n'))
    lista_valores.append(valor)

print(lista_valores)    
limite_operadores = limite - 1

contador = 0

while contador < limite_operadores:
    contador += 1
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == "+":
        resultado = int(lista_valores[-1]) + int(lista_valores[-2])
        lista_valores.pop()
        lista_valores.pop()
        lista_valores.append(resultado)
       
    elif operador == "-":
        resultado = int(lista_valores[-1]) - int(lista_valores[-2])
        lista_valores.pop()
        lista_valores.pop()
        lista_valores.append(resultado)
        
    elif operador == "*":
        resultado = lista_valores[-1] * lista_valores[-2]
        lista_valores.pop()
        lista_valores.pop()
        lista_valores.append(resultado)
       

    elif operador == "/":
        if lista_valores[-2] != 0:
            resultado = lista_valores[-1] / lista_valores[-2]
            lista_valores.pop()
            lista_valores.pop()
            lista_valores.append(resultado)
           
        else:
            resultado = "Erro: Divisão por zero!"
            print(resultado)
            break
    else:
        resultado = "Operador inválido!"
        print(resultado)
        break

    print(lista_valores)

    '''




# Empilha 10 valores reais
pilha = []
for i in range(10):
    valor = float(input(f"Valor {i+1}: "))
    pilha.append(valor)

# Imprime desempilhando
print("\nSaída da pilha:")
while pilha:
    print(pilha.pop())