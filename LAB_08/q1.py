class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insertAtPos(self, data, index):
        if index == 0:
            self.insertHead(data)
            return
        pos = 0
        curr = self.head
        while curr is not None and pos + 1 != index:
            pos += 1
            curr = curr.next
        if curr is not None:
            new = Node(data)
            new.next = curr.next
            curr.next = new
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new

    def deleteHead(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.deleteHead()
            return
        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def displayLL(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

llist = LinkedList()

n = int(input("Enter number of nodes: "))
for _ in range(n):
    data = input("Enter node data: ")
    llist.insertAtEnd(data)

print("\nLinked List:")
llist.displayLL()

print("\nRemove First Node:")
llist.deleteHead()
llist.displayLL()

print("\nRemove Last Node:")
llist.deleteAtEnd()
llist.displayLL()

index = int(input("\nEnter index to remove node: "))
print(f"\nRemove Node at Index {index}:")
llist.remove_at_index(index)
llist.displayLL()
