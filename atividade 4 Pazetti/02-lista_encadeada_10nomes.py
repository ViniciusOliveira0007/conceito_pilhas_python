

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:

    def __init__(self):
        self.cabeca = None  



    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no


    def inserir_fim(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            return

        
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def remover(self, valor):
        atual = self.cabeca
        anterior = None


        while atual:
            if atual.valor == valor:

                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False


    def substituir(self, valor_antigo, valor_novo):
        
        atual = self.cabeca
        anterior = None
 
        while atual:
            if atual.valor == valor_antigo:
                novo_no = No(valor_novo)
                novo_no.proximo = atual.proximo  
                if anterior is None:
                    self.cabeca = novo_no       
                else:
                    anterior.proximo = novo_no  
 
                return True
            anterior = atual
            atual = atual.proximo
        return False


    def __str__(self):
        valores = []
        atual = self.cabeca

        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores) + " -> None" if valores else "Lista vazia"


if __name__ == "__main__":
    lista = ListaEncadeada()
       

    contador = 0
    while contador < 10:
        contador += 1
        valor = input(f'digite o {contador}ª nome:\n')
        lista.inserir_inicio(valor)
    print(lista)
    print('')

    nome_deletar = input('Digite o nome que deseja deletar: \n')
    novo_nome = input('Digite o nome que vai entrar no lugar dele: \n')
 
    sucesso = lista.substituir(nome_deletar, novo_nome)
    if sucesso:
        print(f'"{nome_deletar}" foi substituido por "{novo_nome}"')
    else:
        print(f'"{nome_deletar}" nao foi encontrado na lista')
 
    print(lista)


    