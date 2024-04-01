class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, n):
        self.s1.append(n)

    def deque(self):
        if len(self.s1) == 0:
            print("Cannot dequeue")
        # self.s1.pop(0)
        while len(self.s1):
            self.s2.append(self.s1.pop())
        tmp = self.s2.pop()
        while len(self.s2):
            self.s1.append(self.s2.pop())
        return tmp


q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
print(q.deque())
print(q.deque())
print(q.deque())
