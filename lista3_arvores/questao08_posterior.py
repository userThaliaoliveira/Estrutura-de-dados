"""
Lista Teórica 3 — Árvores
8) Menor chave estritamente maior que a dada.
"""
from estrutura import NoBin, monta


def posterior(chave, no):
    resp = "\0"
    while no is not None:
        if no.chave > chave:
            resp = no.chave          # candidato; tenta um menor à esquerda
            no = no.esq
        else:
            no = no.dir
    return resp


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print(posterior("G", raiz), posterior("M", raiz), repr(posterior("S", raiz)))
