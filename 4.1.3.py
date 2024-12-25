
num = int(input())
curremain, curadd = num, 0
elements = []

while curremain > (curadd + 1) * 2:
    curadd += 1
    elements += [curadd]
    curremain -= curadd

elements += [curremain]

print(len(elements))
print(*elements)
