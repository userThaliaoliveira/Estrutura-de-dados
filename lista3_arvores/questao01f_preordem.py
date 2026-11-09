"""
Lista Teórica 3 — Árvores
1.f) Percurso em pré-ordem.
"""
from estrutura import NoBin, monta


def preordem(no):
    if no is not None:
        print(no.chave, end=" ")
        preordem(no.esq)
        preordem(no.dir)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    preordem(raiz)
    print()
