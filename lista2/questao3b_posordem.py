"""
Lista 2 — Estruturas de Dados e Algoritmos
3.b) Percurso em pós-ordem.
"""
from estrutura import arvore_exemplo


def posordem(no):                                        # (b)
    if no is not None:
        posordem(no.esq)
        posordem(no.dir)
        print(no.valor, end=" ")


if __name__ == "__main__":
    posordem(arvore_exemplo().raiz)
    print()
