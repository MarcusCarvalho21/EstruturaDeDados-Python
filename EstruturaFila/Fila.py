class Fila():
    def __init__(self, tamanhoFila):
        """Inicializando os atributos que definem a Fila"""
        self.tamanhoFila = tamanhoFila
        self.fila = [0]*tamanhoFila
        self.inicioFila = 0
        self.fimFila = -1

    def inserir(self, valor):
        """Função para inserir um dado na fila"""
        if(self.fimFila==self.tamanhoFila-1):
            print("Fila cheia!")
        else:
            self.fimFila +=1
            self.fila[self.fimFila] = valor
        
    def remover(self):
        """Função para remover um dado da fila"""
        if(self.fimFila < self.inicioFila):
            print("Fila vazia!")
        else:
            self.inicioFila+=1

    def retornaValor(self):
        """Função que retorna o valor que está no inicio da fila"""
        if(self.fimFila < self.inicioFila):
            print("Fila vazia!")
        else:
            return self.fila[self.inicioFila]