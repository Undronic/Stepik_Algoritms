def count_sort(array: list) -> list:
    sorted_array = array.copy()
    max_num = max(array)
    nums_array = [0] * max_num
    for el in array:
        nums_array[el - 1] += 1
    for i in range(1, max_num):
        nums_array[i] += nums_array[i - 1]
    for i in range(len(array) - 1, -1, -1):
        sorted_array[nums_array[array[i] - 1] - 1] = array[i]
        nums_array[array[i] - 1] -= 1
    return sorted_array


n = input()
a = list(map(int, input().split()))
print(*count_sort(a))

