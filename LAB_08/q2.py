class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return "Queue is empty!"

    def peek(self):
        return self.queue[0] if not self.isEmpty() else "Queue is empty"

    def size(self):
        return len(self.queue)

q = Queue()
l = list(eval(input("Enter a list: ")))
for i in l:
    q.enqueue(i)

print(q.dequeue())  
print(q.peek())     
print(q.size())  
