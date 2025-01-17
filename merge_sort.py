def Merge(A, p, q, r):
    n_L = q - p
    n_R = r - q
    L = A[p:q].copy()
    R = A[q:r].copy()
    i = 0
    j = 0
    k = p

    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k = k + 1
    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1

def Merge_sort(A, p, r):
    if p >= r-1:
        return
    q = int((p+r)/2)
    Merge_sort(A, p, q)
    Merge_sort(A, q, r)
    Merge(A, p, q, r)