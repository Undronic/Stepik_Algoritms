class CommonHeap:
    def __init__(self):
        self.heap = list()

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap)
        while i > 1 and self.heap[i - 1] > self.heap[int(i/2) - 1]: #change ">" to "<" for min heap
            self.heap[i - 1], self.heap[int(i/2) - 1] = self.heap[int(i/2) - 1], self.heap[i - 1]
            i = int(i/2)

    def pop(self):
        cur_max = self.heap[0]
        self.heap[0] = self.heap[-1]
        del(self.heap[-1])
        self.rebuild_after_pop()
        return cur_max

    def rebuild_after_pop(self):
        i = 1
        while 2*i + 1 <= len(self.heap):
            change_index = [2 * i, 2 * i + 1][self.heap[2 * i - 1] < self.heap[2 * i]]
            if self.heap[i - 1] < self.heap[change_index - 1]:
                self.heap[i - 1], self.heap[change_index - 1] = self.heap[change_index - 1], self.heap[i - 1]
            i = change_index
        if 2*i <= len(self.heap) and self.heap[i-1] < self.heap[2*i-1]: #change "<" to ">" for min heap
            self.heap[i-1], self.heap[2*i-1] = self.heap[2*i-1], self.heap[i-1]

priorityQ = CommonHeap()
for i in range(int(input())):
    command = input()
    if command == "ExtractMax":
        print(priorityQ.pop())
    else:
        priorityQ.push(int(command.split()[1]))
