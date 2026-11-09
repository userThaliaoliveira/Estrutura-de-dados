"""
Lista Teórica 3 — Árvores
7) Maior chave estritamente menor que a dada.
"""
from estrutura import NoBin, monta


def anterior(chave, no):
    resp = "\0"
    while no is not None:
        if no.chave < chave:
            resp = no.chave          # candidato; tenta um maior à direita
            no = no.dir
        else:
            no = no.esq
    return resp


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print(anterior("G", raiz), anterior("M", raiz), repr(anterior("B", raiz)))
