"""
Lista Teórica 3 — Árvores
10) Indica qual rotação AVL deve ser aplicada no nó.
"""
from estrutura import NoBin, monta
from questao09_fator import fator


def qualRotacao(no):
    f = fator(no)
    if f > 1:
        if fator(no.esq) >= 0:
            print("rotação simples à direita")
        else:
            print("rotação dupla à direita (esquerda no filho esq., direita no nó)")
    elif f < -1:
        if fator(no.dir) <= 0:
            print("rotação simples à esquerda")
        else:
            print("rotação dupla à esquerda (direita no filho dir., esquerda no nó)")
    else:
        print("nenhuma: o nó está regulado")


if __name__ == "__main__":
    for cs in ("CBA", "ABC", "CAB", "ACB", "BAC"):
        print(cs, end=": ")
        qualRotacao(monta(cs))
