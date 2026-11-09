"""
Lista 2 — Estruturas de Dados e Algoritmos
3.d) Percurso em pré-ordem.
"""
from estrutura import arvore_exemplo


def preordem(no):                                        # (d)
    if no is not None:
        print(no.valor, end=" ")
        preordem(no.esq)
        preordem(no.dir)


if __name__ == "__main__":
    preordem(arvore_exemplo().raiz)
    print()
