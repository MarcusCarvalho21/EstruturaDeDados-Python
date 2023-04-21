class Pilha():
    def __init__(self, tamanhoPilha):
        """Inicializa os atributos que descrevem a fila"""
        self.tamanhoPilha = tamanhoPilha
        self.pilha = [0]*tamanhoPilha
        self.ponteiro = -1
    
    def inserir(self, valor):
        if(self.ponteiro < self.tamanhoPilha-1):
            self.ponteiro += 1
            self.pilha[self.ponteiro] = valor
        else:
            print("Fila cheia!")

    def remove(self):
        if(self.ponteiro != -1):
            self.ponteiro-=1
        else:
            print("Pilha vazia!")
        
    def retornaValor(self):
        if(self.ponteiro != -1):
            print(self.pilha[self.ponteiro])
        else:
            print("Pilha vazia!")
    