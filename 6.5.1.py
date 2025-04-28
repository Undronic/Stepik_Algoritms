import bisect

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


m, n = map(int, input().split())

segmentsStart, segmentsEnd = map(list, zip(*(map(int, input().split()) for _ in range(m))))

#dots = list(map(int, input().split()))

QuickSort(segmentsStart, 0, m - 1)
#segmentsStart.sort()
QuickSort(segmentsEnd, 0, m - 1)
#segmentsEnd.sort()

for _ in map(int, input().split()):
    i = bisect.bisect_right(segmentsStart, _)
    j = bisect.bisect_left(segmentsEnd, _)
    print(i - j, end=' ')

