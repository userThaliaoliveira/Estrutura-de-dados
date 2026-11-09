"""
Lista 2 — Estruturas de Dados e Algoritmos
3.e) Altura de um nó.
"""
from estrutura import arvore_exemplo


def altura(no):                                          # (e)
    if no is None:
        return 0
    he = altura(no.esq)
    hd = altura(no.dir)
    return 1 + (he if he > hd else hd)


if __name__ == "__main__":
    print(altura(arvore_exemplo().raiz))
