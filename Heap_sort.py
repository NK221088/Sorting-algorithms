from Testing_array import test_array

A = test_array
n = len(A)

def parent(i):
    return i // 2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def Max_Heapify(A, i, n):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else: largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A,largest, n)

def Build_Max_Heap(A, n):
    for i in range(n//2-1, -1, -1):
        Max_Heapify(A,i, n)

def HeapSort(A,n):
    size = n
    Build_Max_Heap(A,n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        size -= 1
        Max_Heapify(A,0, size)

print(A)
Build_Max_Heap(A,len(A))

def Max_Heap_Maximum(A):
    if len(A) < 1:
        raise ValueError("heap underflow")
    return A[0]

print(A)
print(Max_Heap_Maximum(A))