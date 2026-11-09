"""
Lista Teórica 3 — Árvores
1.d) Verifica se a árvore é completa (à esquerda).
"""
from estrutura import NoBin, monta
from questao01c_ehPerfeita import conta


def ehCompleta(no):
    return _completa(no, 0, conta(no))


def _completa(no, i, n):
    if no is None:
        return True
    if i >= n:                       # posição "fora" do vetor por níveis
        return False
    return _completa(no.esq, 2 * i + 1, n) and _completa(no.dir, 2 * i + 2, n)


if __name__ == "__main__":
    print("DBFAC:", ehCompleta(monta("DBFAC")))
    print("DBFG:", ehCompleta(monta("DBFG")))
