"""
Estrutura usada em todas as questões da Lista 3 (struct NoBin) e função
auxiliar para montar árvores de teste por inserção em ABB.
"""


class NoBin:
    __slots__ = ("chave", "esq", "dir")

    def __init__(self, chave, esq=None, dir=None):
        self.chave = chave
        self.esq = esq
        self.dir = dir


def insere(chave, no):               # pre: no existe (árvore não vazia)
    if chave <= no.chave:
        if no.esq is not None:
            insere(chave, no.esq)
        else:
            no.esq = NoBin(chave)
    else:
        if no.dir is not None:
            insere(chave, no.dir)
        else:
            no.dir = NoBin(chave)


def monta(chaves):
    raiz = NoBin(chaves[0])
    for i in range(1, len(chaves)):
        insere(chaves[i], raiz)
    return raiz
