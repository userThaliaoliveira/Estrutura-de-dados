"""
Lista Teórica 3 — Árvores
6) Busca de uma chave na ABB (retorna '\0' se não existir).
"""
from estrutura import NoBin, monta


def busca(chave, no):
    while no is not None:
        if chave == no.chave:
            return no.chave
        no = no.esq if chave < no.chave else no.dir
    return "\0"


if __name__ == "__main__":
    raiz = monta("MDOBFNSEL")   # árvore A3 dos slides
    print(busca("F", raiz), repr(busca("G", raiz)))
