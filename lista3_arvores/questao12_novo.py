"""
Lista Teórica 3 — Árvores
12) Insere um novo elemento no heap (retorna o novo N).
"""
from array import array
from questao11_ehHeap import ehHeap


def novo(elemento, heap, N):
    heap[N] = elemento
    pos = N
    while pos > 0:
        pai = (pos - 1) // 2
        if heap[pai] <= heap[pos]:
            break
        heap[pai], heap[pos] = heap[pos], heap[pai]
        pos = pai
    return N + 1


if __name__ == "__main__":
    h = array("i")
    for _ in range(20):
        h.append(0)
    N = 0
    for x in array("i", (20, 10, 30, 5, 25, 1)):
        N = novo(x, h, N)
    for i in range(N):
        print(h[i], end=" ")
    print("| ehHeap:", ehHeap(h, N))
