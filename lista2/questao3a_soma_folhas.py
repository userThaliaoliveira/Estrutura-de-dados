"""
Lista 2 — Estruturas de Dados e Algoritmos
3.a) Soma das folhas.
"""
from estrutura import arvore_exemplo


def soma_folhas(no):                                     # (a)
    if no is None:
        return 0
    if no.esq is None and no.dir is None:
        return no.valor
    return soma_folhas(no.esq) + soma_folhas(no.dir)


if __name__ == "__main__":
    print(soma_folhas(arvore_exemplo().raiz))
