"""
Lista Teórica 3 — Árvores
1.h) Percurso em-ordem (inorder).
"""
from estrutura import NoBin, monta


def inorder(no):
    if no is not None:
        inorder(no.esq)
        print(no.chave, end=" ")
        inorder(no.dir)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    inorder(raiz)
    print()
