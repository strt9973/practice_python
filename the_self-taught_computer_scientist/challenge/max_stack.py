class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n > self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]


s = MaxStack()
s.push(1)
s.push(3)
s.push(2)

print(s.get_max())
print(s.pop())
print(s.get_max())
print(s.pop())
print(s.get_max())
print(s.pop())
