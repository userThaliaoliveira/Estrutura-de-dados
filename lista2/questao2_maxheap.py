"""
Lista 2 — Estruturas de Dados e Algoritmos
2) MAX-heap: remoção do maior e inserção do 16, passo a passo.
"""
from array import array


def imprime_vetor(v, n):
    print("[", end="")
    for i in range(n):
        print(("" if i == 0 else ", ") + str(v[i]), end="")
    print("]")


def desce_max(v, n, pos):
    f = 2 * pos + 1
    while f < n:
        if f + 1 < n and v[f + 1] > v[f]:       # escolhe o MAIOR filho
            f += 1
        if v[f] <= v[pos]:
            break
        print(f"   troca {v[pos]} (pos {pos}) com {v[f]} (pos {f})")
        v[pos], v[f] = v[f], v[pos]
        pos = f
        f = 2 * pos + 1
        print("   ", end=""); imprime_vetor(v, n)


def remove_max(v, n):
    print(f"   troca a raiz {v[0]} com o último {v[n - 1]} e diminui N")
    v[0], v[n - 1] = v[n - 1], v[0]
    n -= 1
    print("   ", end=""); imprime_vetor(v, n)
    desce_max(v, n, 0)
    return n


def insere_max(v, n, x):
    v[n] = x
    n += 1
    print(f"   coloca {x} no fim (pos {n - 1})")
    print("   ", end=""); imprime_vetor(v, n)
    pos = n - 1
    while pos > 0:
        pai = (pos - 1) // 2
        if v[pai] >= v[pos]:
            break
        print(f"   troca {v[pos]} (pos {pos}) com o pai {v[pai]} (pos {pai})")
        v[pai], v[pos] = v[pos], v[pai]
        pos = pai
        print("   ", end=""); imprime_vetor(v, n)
    return n


if __name__ == "__main__":
    print("(a) remoção do maior:")
    h = array("i", (20, 10, 15, 4, 7, 8, 3, 1, 2, 0))
    n = remove_max(h, 9)
    print("   final: ", end=""); imprime_vetor(h, n)
    print("(b) inserção do 16:")
    h = array("i", (20, 10, 15, 4, 7, 8, 3, 1, 2, 0))
    n = insere_max(h, 9, 16)
    print("   final: ", end=""); imprime_vetor(h, n)
