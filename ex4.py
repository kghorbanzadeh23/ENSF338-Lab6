class Heap:
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


# Tests
def test_sorted_heap():
    h = Heap()
    input_array = [10, 20, 30, 40, 50]
    h.heapify(input_array)
    expected = [50, 40, 30, 10, 20]
    assert h.array == expected, f"Expected: {expected}, Got: {h.array}"

def test_empty_heap():
    h = Heap()
    input_array = []
    h.heapify(input_array)
    expected = []
    assert h.array == expected, f"Expected: {expected}, Got: {h.array}"

def test_random_heap():
    import random
    h = Heap()
    input_array = random.sample(range(1, 100), 20)
    h.heapify(input_array)
    input_array.sort(reverse=True)
    expected = input_array
    assert h.array == expected, f"Expected: {expected}, Got: {h.array}"

# Run tests
test_sorted_heap()
test_empty_heap()
test_random_heap()
print("All tests passed!")
