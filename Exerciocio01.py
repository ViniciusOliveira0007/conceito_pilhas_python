pilha = []
for i in range(10):
    valor = float(input(f"Valor {i+1}: "))
    pilha.append(valor)


print("\nSaída da pilha:")
while pilha:
    print(pilha.pop())