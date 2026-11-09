"""
Lista Teórica 3 — Árvores
1.a) Verifica se a árvore é estritamente binária.
"""
from estrutura import NoBin, monta


def estritaBin(no):
    if no is None:
        return True
    if (no.esq is None) != (no.dir is None):     # exatamente 1 filho
        return False
    return estritaBin(no.esq) and estritaBin(no.dir)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print("estritamente binária?", estritaBin(raiz))
    print("DBFAC:", estritaBin(monta("DBFAC")))
