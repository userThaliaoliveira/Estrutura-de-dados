"""
Lista 2 — Estruturas de Dados e Algoritmos
3.c) Percurso em-ordem.
"""
from estrutura import arvore_exemplo


def emordem(no):                                         # (c)
    if no is not None:
        emordem(no.esq)
        print(no.valor, end=" ")
        emordem(no.dir)


if __name__ == "__main__":
    emordem(arvore_exemplo().raiz)
    print()
