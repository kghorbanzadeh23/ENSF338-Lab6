import timeit
import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
    
    def insert(data, root=None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        newnode = Node(data, parent)    
        if root is None:
            root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode

        return newnode

def generate_sorted_vector(size):
    return sorted(random.sample(range(1000000), size))

def shuffle_vector(vector):
    random.shuffle(vector)

def measure_search_performance(shuffled_vector, root):
    search_times = []
    for data in shuffled_vector:
        search_time = timeit.timeit(lambda: search(data, root), number=10) / 10
        search_times.append(search_time)
    avg_search_time = sum(search_times) / len(search_times)
    total_search_time = sum(search_times)
    return avg_search_time, total_search_time

def search(data, root):
    current = root
    while current is not None and current.data != data:
        if data < current.data:
            current = current.left
        else:
            current = current.right
    return current

# Generate sorted vector
sorted_vector = generate_sorted_vector(10000)

# Build binary search tree
root = None
for data in sorted_vector:
    root = Node.insert(data, root)

# Shuffle the vector
shuffled_vector = sorted_vector[:]
shuffle_vector(shuffled_vector)

# Measure search performance
avg_search_time, total_search_time = measure_search_performance(shuffled_vector, root)

print("Average search time after shuffling:", avg_search_time)
print("Total search time after shuffling:", total_search_time)

"""
4)
In summary, the approach of using a binary search tree might be faster in this scenario,
especially if the tree remains balanced after shuffling. However, the actual performance may vary depending
on factors such as the balance of the tree and the distribution of data. Conducting empirical tests on different
datasets can provide more insights into the relative performance of both approaches.
"""