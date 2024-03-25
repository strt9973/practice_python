class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
    
    def __str__(self):
        data_list = []
        node = self.head
        while node is not None:
            data_list.append(str(node.data))
            node = node.next
        return "\n".join(data_list)

num_list = LinkedList()
for i in range(100):
    num_list.append(i + 1)

print(num_list)
