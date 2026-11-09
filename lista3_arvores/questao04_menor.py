"""
Lista Teórica 3 — Árvores
4) Menor valor da árvore (versão geral e versão ABB).
"""
from estrutura import NoBin, monta


def menor(no):
    if no is None:
        return "Z"                   # maior valor possível
    return min(no.chave, menor(no.esq), menor(no.dir))


def menorABB(no):
    if no is None:
        return "Z"
    while no.esq is not None:
        no = no.esq
    return no.chave


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print(menor(raiz), menorABB(raiz), repr(menor(None)))
