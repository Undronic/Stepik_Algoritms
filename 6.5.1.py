import bisect
import random


def Partition(A, l, r):
    j = l
    x = A[l]
    for i in range(l + 1, r + 1):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def QuickSort(A, l, r):
    if l >= r:
        return
    x = Partition(A, l, r)
    QuickSort(A, l, x - 1)
    QuickSort(A, x + 1, r)


def Partition3(A, l, r):
    pivot_idx = random.randint(l, r)
    A[l], A[pivot_idx] = A[pivot_idx], A[l]
    j = l
    k = l
    x = A[l]
    for i in range(l + 1, r + 1):
        if A[i] < x:
            j += 1
            k += 1
            A[i], A[k] = A[k], A[i]
            A[k], A[j] = A[j], A[k]
        elif A[i] == x:
            k += 1
            A[i], A[k] = A[k], A[i]
    A[l], A[j] = A[j], A[l]
    return j, k


def QuickSort3(A, l, r):

    while l < r:
        x, z = Partition3(A, l, r)
        if x - l < r - z:
            QuickSort3(A, l, x - 1)
            l = z + 1
        else:
            QuickSort3(A, z + 1, r)
            r = x - 1


m, n = map(int, input().split())

segmentsStart, segmentsEnd = map(list, zip(*(map(int, input().split()) for _ in range(m))))

QuickSort3(segmentsStart, 0, m - 1)
#segmentsStart.sort()
QuickSort3(segmentsEnd, 0, m - 1)
#segmentsEnd.sort()

for _ in map(int, input().split()):
    i = bisect.bisect_right(segmentsStart, _)
    j = bisect.bisect_left(segmentsEnd, _)
    print(i - j, end=' ')
