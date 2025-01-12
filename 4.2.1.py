st = input()

letters = [[let, st.count(let)] for let in set(st)]

n = len(letters)
if n == 1:
    print(1, len(st))
    print(f'{letters[0][0]}: 1')
    print('1' * len(st))
else:
    result = ''
    letters_code = {char: '' for char in st}
    for k in range(n + 1, 2*n):
        min1 = min(letters, key=lambda x: x[1])
        letters.remove(min1)
        min2 = min(letters, key=lambda x: x[1])
        letters.remove(min2)
        letters.append([min1[0] + min2[0], min1[1] + min2[1]])
        for el in min1[0]:
            letters_code[el] = '1' + letters_code[el]
        for el in min2[0]:
            letters_code[el] = '0' + letters_code[el]
    for el in st:
        result += letters_code[el]
    print(len(letters_code), len(result))
    for key, value in letters_code.items():
        print(f'{key}: {value}')
    print(result)

