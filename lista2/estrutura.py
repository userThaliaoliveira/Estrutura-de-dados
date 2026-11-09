"""
Estrutura da questão 3 (classes No e Arvore) e função auxiliar que monta a
árvore da questão 1 a partir da representação sequencial.
"""


class No:
    __slots__ = ("valor", "esq", "dir")

    def __init__(self, valor, esq=None, dir=None):
        self.valor = valor
        self.esq = esq
        self.dir = dir


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz


def vetor_para_arvore(v, n, i=0):
    if i >= n:
        return None
    return No(v[i], vetor_para_arvore(v, n, 2 * i + 1), vetor_para_arvore(v, n, 2 * i + 2))


from array import array

VETOR_Q1 = array("i", (10, 20, 15, 12, 8, 5, 7, 1, 2))


def arvore_exemplo():
    return Arvore(vetor_para_arvore(VETOR_Q1, len(VETOR_Q1)))
