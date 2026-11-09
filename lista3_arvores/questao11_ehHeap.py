"""
Lista Teórica 3 — Árvores
11) Verifica se o vetor é um heap (min-heap, como nos slides).
"""
from array import array


def ehHeap(heap, N):
    for i in range(1, N):
        if heap[(i - 1) // 2] > heap[i]:     # pai maior que filho: não é min-heap
            return False
    return True


if __name__ == "__main__":
    print(ehHeap(array("i", (1, 5, 3, 10, 7)), 5))
    print(ehHeap(array("i", (5, 1, 3)), 3))
