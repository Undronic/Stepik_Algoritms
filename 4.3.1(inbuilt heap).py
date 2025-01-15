import heapq

heap = []
for i in range(int(input())):
    command = input()
    if command == "ExtractMax":
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -int(command.split()[1]))
