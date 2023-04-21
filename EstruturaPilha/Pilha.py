class Pilha():
    def __init__(self, tamanhoPilha):
        """Inicializa os atributos que descrevem a pila"""
        self.tamanhoPilha = tamanhoPilha
        self.pilha = [0]*tamanhoPilha
        self.ponteiro = -1
    
    def inserir(self, valor):
        """Função para inserir um dado no topo da pilha"""
        if(self.ponteiro < self.tamanhoPilha-1):
            self.ponteiro += 1
            self.pilha[self.ponteiro] = valor
        else:
            print("Fila cheia!")

    def remove(self):
        """Função que remove um dado do topo da pilha"""
        if(self.ponteiro != -1):
            self.ponteiro-=1
        else:
            print("Pilha vazia!")
        
    def retornaValor(self):
        """Função que retorna o valor que está no topo da piilha"""
        if(self.ponteiro != -1):
            print(self.pilha[self.ponteiro])
        else:
            print("Pilha vazia!")
    