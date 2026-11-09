"""
Lista 2 — Estruturas de Dados e Algoritmos
3.h) Produto dos nós.
"""
from estrutura import arvore_exemplo


def produto(no):                                         # (h)
    if no is None:
        return 1                    # elemento neutro da multiplicação
    return no.valor * produto(no.esq) * produto(no.dir)


if __name__ == "__main__":
    print(produto(arvore_exemplo().raiz))
