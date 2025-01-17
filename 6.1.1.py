def binary_find(array: list, number: int):
    left_border, right_border = 0, len(array) - 1
    while right_border - left_border > 1 and array[(left_border + right_border) // 2] != number:
        if number < array[(left_border + right_border) // 2]:
            right_border = (left_border + right_border) // 2
        else:
            left_border = (left_border + right_border) // 2

    if array[(left_border + right_border) // 2] == number:
        return (left_border + right_border) // 2 + 1
    elif number == array[right_border]:
        return right_border + 1

    return -1


target_len, *target = [int(_) for _ in input().split()]
checking_len, *checking = [int(_) for _ in input().split()]

for i in range(checking_len):
    print(binary_find(target, checking[i]), end=" ")
