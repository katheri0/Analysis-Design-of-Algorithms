A = [0, 53, 8976, 22, 4, 9, 4, 2, 1, 8, 5]

n = len(A)

def selectionsort(A, n):
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if A[j] < A[imin]:
                imin = j
        if imin != i:
            temp = A[i]
            A[i] = A[imin]
            A[imin] = temp

selectionsort(A, n)
print(A)

