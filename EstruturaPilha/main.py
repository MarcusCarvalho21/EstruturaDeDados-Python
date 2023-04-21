from Pilha import Pilha

minhaPilha = Pilha(5)
minhaPilha.inserir(2)
minhaPilha.inserir(6)
minhaPilha.inserir(3)
minhaPilha.inserir(10)
minhaPilha.inserir(11)
#minhaPilha.retornaValor()
minhaPilha.remove()
minhaPilha.inserir(12)
#minhaPilha.retornaValor()

for x in range(5):
    minhaPilha.retornaValor()
    minhaPilha.remove()