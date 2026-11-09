"""
Lista 2 — Estruturas de Dados e Algoritmos
1) Percursos pré, em e pós-ordem na árvore completa em representação sequencial.
"""
from array import array


def preordem_seq(v, n, i=0):
    if i < n:
        print(v[i], end=" ")
        preordem_seq(v, n, 2 * i + 1)
        preordem_seq(v, n, 2 * i + 2)


def emordem_seq(v, n, i=0):
    if i < n:
        emordem_seq(v, n, 2 * i + 1)
        print(v[i], end=" ")
        emordem_seq(v, n, 2 * i + 2)


def posordem_seq(v, n, i=0):
    if i < n:
        posordem_seq(v, n, 2 * i + 1)
        posordem_seq(v, n, 2 * i + 2)
        print(v[i], end=" ")


if __name__ == "__main__":
    v = array("i", (10, 20, 15, 12, 8, 5, 7, 1, 2))
    n = len(v)
    print("(a) pré: ", end=""); preordem_seq(v, n); print()
    print("(b) em:  ", end=""); emordem_seq(v, n); print()
    print("(c) pós: ", end=""); posordem_seq(v, n); print()
