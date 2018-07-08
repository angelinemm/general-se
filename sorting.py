import random as rd

SIZE = 100
MAX_VALUE = 200

def heap_sort(A):
    n = len(A)

    _heapify(A)

    end = n - 1
    while end > 0:
        A[0], A[end] = A[end], A[0]
        _sift_down(A, 0, end-2)
        end -= 1

def _sift_down(A, root, end):
    idx_left_child =  2 * root + 1
    idx_right_child = 2 * root + 2
    swap_with = root

    if idx_left_child <= end and A[idx_left_child] > A[swap_with]:
        swap_with = idx_left_child
    if idx_right_child <= end and A[idx_right_child] > A[swap_with]:
        swap_with = idx_right_child
    if swap_with != root:
        A[root], A[swap_with] = A[swap_with], A[root]
        _sift_down(A, swap_with, end)

def _heapify(A):
    n = len(A)
    # start at last parent
    start = (n - 2) // 2

    while start >= 0:
        _sift_down(A, start, n-1)
        start -= 1


if __name__ == '__main__':
    ar = [rd.randint(0, MAX_VALUE) for _ in range(0, SIZE - 1)]
    print(ar)

    heap_sort(ar)

    print('Heap sort:')
    print(ar)
