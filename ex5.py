import random
import timeit
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None 

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None or self.head.value >= value:

            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            min_value = self.head.value
            self.head = self.head.next
            return min_value
        
class HeapPriorityQueue:
    def __init__(self):
        self.array = []

    def heapify(self, arr):
        self.array = arr[:]
        n = len(self.array)
        # Start from the last and move up
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i, n)

    def enqueue(self, value):
        self.array.append(value)
        self._heapify_up(len(self.array) - 1)

    def dequeue(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop()
        # Swap root with last element
        root = self.array[0]
        self.array[0] = self.array.pop()
        self._heapify_down(0, len(self.array))
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.array[index] > self.array[parent]:
            self.array[index], self.array[parent] = self.array[parent], self.array[index]
            self._heapify_up(parent)

    def _heapify_down(self, index, size):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < size and self.array[left] > self.array[largest]:
            largest = left
        if right < size and self.array[right] > self.array[largest]:
            largest = right

        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self._heapify_down(largest, size)

def generate_tasks(n=1000, enqueue_prob=0.7):
    return ["enqueue" if random.random() < enqueue_prob else "dequeue" for _ in range(n)]


tasks = generate_tasks()
listTimes = []
heapTimes = []

heapQueue = HeapPriorityQueue()
listQueue = ListPriorityQueue()

for i in tasks:
    if i == "enqueue":
        heapTimes.append(timeit.timeit(lambda: heapQueue.enqueue(1), number=1))
        listTimes.append(timeit.timeit(lambda: listQueue.enqueue(1), number=1))
    else:
        heapTimes.append(timeit.timeit(lambda: heapQueue.dequeue, number=1))
        listTimes.append(timeit.timeit(lambda: listQueue.dequeue, number=1))

print("Overall time for heap:", sum(heapTimes))
print("Overall time for list:", sum(listTimes), "\n")

print("Average time for Heap:", sum(heapTimes)/len(heapTimes))
print("Average time for List:", sum(listTimes)/len(listTimes))


#4
#It looks like the linked list is faster than the using a heap.
#The extra work on heapifying each time we enqueue and dequeue may be adding extra time when compared to the 
#linked list implementation.