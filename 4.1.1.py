def dots_on_segments(number: int) -> list:
    segments = [[int(a) for a in input().split()] for _ in range(number)]
    segments = sorted(segments, key=lambda x: x[1])

    dots = [segments[0][1]]
    for i in range(1, number):
        curdot = dots[-1]
        if segments[i][1] > curdot and segments[i][0] > curdot:
            dots += [segments[i][1]]
            continue
    return dots


res = dots_on_segments(int(input()))
print(len(res))
print(*res)
#c = sorted([a,b], key=lambda x:x[1])


