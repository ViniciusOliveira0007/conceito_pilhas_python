pilha = [21,22,23,24,25,26,26,26,26,28,28,28,28,28,29,30,31,31, 50,50,50]
print('Pilha original:')
print(pilha)

pilha_verificada = []

for i in pilha:
   
    if i not in pilha_verificada:
        quantidade = pilha.count(i)
        
       
        if quantidade > 1:
            pilha_verificada.extend(['&&', i, quantidade])
            
        else:
            pilha_verificada.append(i)

print('\nDados limpos com suas sequência:')
print(*pilha_verificada)


