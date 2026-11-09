"""
Lista Teórica 3 — Árvores
3) Maior valor da árvore (versão geral e versão ABB).
"""
from estrutura import NoBin, monta


def maior(no):
    if no is None:
        return "A"                   # menor valor possível
    return max(no.chave, maior(no.esq), maior(no.dir))


def maiorABB(no):
    if no is None:
        return "A"
    while no.dir is not None:
        no = no.dir
    return no.chave


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print(maior(raiz), maiorABB(raiz), repr(maior(None)))
