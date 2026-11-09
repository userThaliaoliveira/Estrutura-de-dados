"""
Lista Teórica 3 — Árvores
1.b) Percurso em níveis (usa uma fila encadeada).
"""
from estrutura import NoBin, monta


class NoFila:
    __slots__ = ("arv", "prox")

    def __init__(self, arv):
        self.arv = arv
        self.prox = None


class FilaEnc:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazia(self):
        return self.inicio is None

    def enfileira(self, arv):
        novo = NoFila(arv)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.prox = novo
        self.fim = novo

    def desenfileira(self):
        no = self.inicio
        self.inicio = no.prox
        if self.inicio is None:
            self.fim = None
        return no.arv


def emNiveis(no):
    if no is None:
        return
    fila = FilaEnc()
    fila.enfileira(no)
    while not fila.vazia():
        atual = fila.desenfileira()
        print(atual.chave, end=" ")
        if atual.esq is not None:
            fila.enfileira(atual.esq)
        if atual.dir is not None:
            fila.enfileira(atual.dir)
    print()


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    emNiveis(raiz)
