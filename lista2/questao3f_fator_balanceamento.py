"""
Lista 2 — Estruturas de Dados e Algoritmos
3.f) Fator de balanceamento de um nó.
"""
from estrutura import arvore_exemplo
from questao3e_altura import altura


def fator_balanceamento(no):                             # (f)
    return altura(no.esq) - altura(no.dir)


if __name__ == "__main__":
    print(fator_balanceamento(arvore_exemplo().raiz))
