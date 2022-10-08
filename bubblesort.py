def bubble_sort(A):
    n = len(A)
    i = 0
    flag = 0
    while i < n-1:
        j = 0
        while j < n-i-1:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = 1
            j += 1
        i += 1
        if flag == 0:
            return A
            break

