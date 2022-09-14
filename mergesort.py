def mergesort(A, lb=0, ub=None):
    if ub is None:
        ub = len(A)-1
    if lb < ub:
        m = (lb+ub)//2
        mergesort(A, lb, m)
        mergesort(A, m+1, ub)
        L = A[lb:m+1]
        R = A[m+1:ub+1]
        merge(A, lb, ub, L, R)

def merge(A, lb, ub, L, R):
    i = 0
    j = 0
    k = lb
    while i in range(0, len(L)) and j in range(0, len(R)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    if i >= len(L):
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    if j >= len(R):
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

