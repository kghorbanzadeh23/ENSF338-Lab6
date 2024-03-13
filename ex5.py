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
        self.heap = []

    def enqueue(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._sift_down(0)
        return root

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

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