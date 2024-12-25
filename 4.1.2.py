
count, size = [int(_) for _ in input().split()]
cursize = size
curcost = 0
items = sorted([(int(cost), int(volume), int(cost)/int(volume)) for _ in range(count) for cost, volume in [input().split()]], key=lambda x: x[2], reverse=True)

for i in range(count):
    curcost += min(cursize, items[i][1]) * items[i][2]
    cursize = max(cursize - items[i][1], 0)
    if cursize == 0:
        break

print(round(curcost, 3))


