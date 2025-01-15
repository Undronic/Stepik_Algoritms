codes = {}
result = ''
letters_count = int(input().split()[0])
for i in range(letters_count):
    letter, code = input().split(': ')
    codes[code] = letter
coded_str = input()
i = 0
if letters_count == 1:
    print(list(codes.values())[0] * len(coded_str))
else:
    while i < len(coded_str):
        j = i + 1
        while coded_str[i:j] not in codes.keys():
            j += 1
        result += codes[coded_str[i:j]]
        i += j - i
    print(result)
