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

    def create_cycle(self, data):
        if not self.head:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, self.head)

def detect_cycle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while True:
        try:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        except:
            return False

cycle_list = LinkedList()
for i in range(99):
    cycle_list.append(i + 1)
cycle_list.create_cycle(100)

non_cycle_list = LinkedList()
for i in range(100):
    non_cycle_list.append(i + 1)

is_cycle_1 = detect_cycle(cycle_list)
if is_cycle_1:
    print("cycle_list is cycle list")
else:
    print("cycle_list is non-cycle list")

is_cycle_2 = detect_cycle(non_cycle_list)
if is_cycle_2:
    print("non_cycle_list is cycle list")
else:
    print("non_cycle_list is non-cycle list")