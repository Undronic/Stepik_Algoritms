def mergesort(array: list):
    merging_array = [[_] for _ in array]
    inv = 0
    while len(merging_array) > 1:
        merged = []
        for _ in range(0, len(merging_array), 2):
            first_part = merging_array[_]
            second_part = merging_array[_ + 1] if _ + 1 < len(merging_array) else []
            i, j = 0, 0
            buf = []
            while i < len(first_part) and j < len(second_part):
                if first_part[i] <= second_part[j]:
                    buf.append(first_part[i])
                    i += 1
                else:
                    buf.append(second_part[j])
                    j += 1
                    inv += len(first_part) - i
            buf.extend(first_part[i:])
            buf.extend(second_part[j:])
            merged.append(buf)
        merging_array = merged
    merging_array.append([inv])
    return merging_array


n = input()
print(*mergesort(list(map(int, input().split())))[1])
