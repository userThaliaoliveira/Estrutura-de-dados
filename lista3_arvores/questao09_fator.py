"""
Lista Teórica 3 — Árvores
9) Fator de balanceamento de um nó.
"""
from estrutura import NoBin, monta
from questao01e_altura import altura


def fator(no):
    return altura(no.esq) - altura(no.dir)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print("fator da raiz:", fator(raiz))
