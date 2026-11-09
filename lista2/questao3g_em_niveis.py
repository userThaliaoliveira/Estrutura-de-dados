"""
Lista 2 — Estruturas de Dados e Algoritmos
3.g) Percurso em níveis (usa uma fila encadeada).
"""
from estrutura import arvore_exemplo


class NoFila:                                            # (g) fila auxiliar
    __slots__ = ("arv", "prox")

    def __init__(self, arv):
        self.arv = arv
        self.prox = None


def em_niveis(no):                                       # (g)
    if no is None:
        return
    inicio = fim = NoFila(no)
    while inicio is not None:
        atual = inicio.arv
        print(atual.valor, end=" ")
        if atual.esq is not None:
            fim.prox = NoFila(atual.esq)
            fim = fim.prox
        if atual.dir is not None:
            fim.prox = NoFila(atual.dir)
            fim = fim.prox
        inicio = inicio.prox
    print()


if __name__ == "__main__":
    em_niveis(arvore_exemplo().raiz)
