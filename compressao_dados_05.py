'''
Literalmente o que eu fiz no execercício 4, mas com uma questão que não importa a sequência


'''

pilha = [21,22,23,24,25,26,26,26,26,28,28,28,28,28,29,30,31,31]
print('Pilha original:')
print(pilha)

pilha_verificada = []

for i in pilha:
   
    if i not in pilha_verificada:
        quantidade = pilha.count(i)
        
       
        if quantidade > 1:
            pilha_verificada.append('&&')
            pilha_verificada.append(i)
            pilha_verificada.append(quantidade)
        else:
            pilha_verificada.append(i)

print('\nDados limpos com suas sequência:')
print(*pilha_verificada)



