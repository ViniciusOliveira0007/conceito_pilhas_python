'''
tenho que fazer uma lista e depois analisar os valores que se repetem,
escolher um caractere especial para indicar o tal de 'run-lenght'  ||  caractere escolhido: "&&"
e colocar ele antes de uma sequência de valor, depois colocar o valor que está sendo repetido
e em sequência a quantidade de vezes que se repete.
'''
pilha = [21,31, 22, 23, 24, 25, 26, 26, 26, 26, 28, 28, 28, 28, 28, 29, 30, 31, 31]
print('Pilha original:')
print(pilha)

pilha_verificada = []

# Variáveis para rastrear a sequência atual
numero_atual = None
quantidade = 0

for i in pilha:
    # Se for o primeiro número ou o mesmo número da sequência atual
    if i == numero_atual:
        quantidade += 1
    else:
        # Se mudou de número e já tínhamos uma sequência acumulada, salvamos a anterior
        if numero_atual is not None:
            if quantidade > 1:
                pilha_verificada.extend(['&&', numero_atual, quantidade])
            else:
                pilha_verificada.append(numero_atual)
        
        # Reseta para o novo número encontrado
        numero_atual = i
        quantidade = 1

# Não esquecer de salvar o último número/sequência da lista após o loop terminar
if numero_atual is not None:
    if quantidade > 1:
        pilha_verificada.extend(['&&', numero_atual, quantidade])
    else:
        pilha_verificada.append(numero_atual)

print('\nDados limpos com suas sequência consecutiva:')
print(*pilha_verificada)
