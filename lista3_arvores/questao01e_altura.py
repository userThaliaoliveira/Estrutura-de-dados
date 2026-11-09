"""
Lista Teórica 3 — Árvores
1.e) Altura da árvore.
"""
from estrutura import NoBin, monta


def altura(no):
    if no is None:
        return 0
    he = altura(no.esq)
    hd = altura(no.dir)
    return 1 + (he if he > hd else hd)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print("altura:", altura(raiz))
