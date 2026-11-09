"""
Lista Teórica 3 — Árvores
1.c) Verifica se a árvore é perfeita (n = 2^h - 1).
"""
from estrutura import NoBin, monta
from questao01e_altura import altura


def conta(no):
    if no is None:
        return 0
    return 1 + conta(no.esq) + conta(no.dir)


def ehPerfeita(no):
    return conta(no) == 2 ** altura(no) - 1


if __name__ == "__main__":
    print("DBFACEG:", ehPerfeita(monta("DBFACEG")))
    print("DBFAC:", ehPerfeita(monta("DBFAC")))
