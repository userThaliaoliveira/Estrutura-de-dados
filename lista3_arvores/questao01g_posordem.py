"""
Lista Teórica 3 — Árvores
1.g) Percurso em pós-ordem.
"""
from estrutura import NoBin, monta


def posordem(no):
    if no is not None:
        posordem(no.esq)
        posordem(no.dir)
        print(no.chave, end=" ")


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    posordem(raiz)
    print()
