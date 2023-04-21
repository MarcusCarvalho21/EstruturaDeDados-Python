class Fila():
    def __init__(self, tamanhoFila):
        self.tamanhoFila = tamanhoFila
        self.fila = [0]*tamanhoFila
        self.inicioFila = 0
        self.fimFila = -1

    def inserir(self, valor):
        if(self.fimFila==self.tamanhoFila-1):
            print("Fila cheia!")
        else:
            self.fimFila +=1
            self.fila[self.fimFila] = valor
        
    def remover(self):
        if(self.fimFila < self.inicioFila):
            print("Fila vazia!")
        else:
            self.inicioFila+=1

    def retornaValor(self):
        if(self.fimFila < self.inicioFila):
            print("Fila vazia!")
        else:
            return self.fila[self.inicioFila]