def stairs(arr: list) -> int:
    arr_len = len(arr)
    if arr_len == 1:
        return arr[0]
    step_max = [0] * (arr_len + 1)
    step_max[1] = arr[0]
    for i in range(1, arr_len):
        step_max[i+1] = max(step_max[i] + arr[i], step_max[i-1] + arr[i])
    return step_max[-1]


input()
a = [int(_) for _ in input().split()]
