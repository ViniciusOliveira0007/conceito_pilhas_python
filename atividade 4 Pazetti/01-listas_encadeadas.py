'''
OBJETIVO: listas encadeadas
tem uma lista com 6 espaços, mas o sexto lugar não tem nada
cada elemento aponta para o seu próximo, fazendo assim uma corrente


'''


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:

    def __init__(self):
        self.cabeca = None  # primeiro nó da lista



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


    def __str__(self):
        valores = []
        atual = self.cabeca

        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(valores) + " -> None" if valores else "Lista vazia"


if __name__ == "__main__":
    lista = ListaEncadeada()
    
    lista.inserir_inicio('PREA')
    lista.inserir_inicio('COTIA')
    lista.inserir_inicio('TATU')
    lista.inserir_inicio('PACA')
    lista.inserir_inicio('ANTA')
    
    print('Lista completa:')
    print(lista)   
    print('')      

    print('***REMOVENDO ANTA***')
    lista.remover('ANTA')
    print(lista)
    print('')     

    print('***ADICIONANDO LEÃO***')
    lista.inserir_inicio('LEÃO')   
    print(lista)
    print('')     

    print('***REMOVENDO O REGISTRO DA POSIÇÃO 5***')
    lista.remover('PREA')
    print(lista) 
    print('')    


    print('***REMOVENDO TATU***')
    lista.remover('TATU')
    print(lista)