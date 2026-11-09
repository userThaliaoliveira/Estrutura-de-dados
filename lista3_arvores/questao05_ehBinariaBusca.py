"""
Lista Teórica 3 — Árvores
5) Verifica se a árvore é uma árvore binária de busca.
"""
from estrutura import NoBin, monta


def ehBinariaBusca(no):
    return _ehABB(no, "A", "Z")


def _ehABB(no, lo, hi):
    if no is None:
        return True
    if not (lo < no.chave < hi):
        return False
    return _ehABB(no.esq, lo, no.chave) and _ehABB(no.dir, no.chave, hi)


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print("A3:", ehBinariaBusca(raiz))
    errada = NoBin("M", NoBin("D", None, NoBin("Q")))
    print("Q à esquerda de M:", ehBinariaBusca(errada))
