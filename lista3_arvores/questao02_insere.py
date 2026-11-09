"""
Lista Teórica 3 — Árvores
2) Inserção em árvore binária de busca.
"""
from estrutura import NoBin
from questao01h_inorder import inorder


def insere(chave, no):               # pre: no existe (árvore não vazia)
    if chave <= no.chave:
        if no.esq is not None:
            insere(chave, no.esq)
        else:
            no.esq = NoBin(chave)
    else:
        if no.dir is not None:
            insere(chave, no.dir)
        else:
            no.dir = NoBin(chave)


if __name__ == "__main__":
    raiz = NoBin("M")
    for c in "DOBFNSEL":
        insere(c, raiz)
    inorder(raiz)
    print()
