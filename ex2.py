import random
import timeit

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def build_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

def measure_bst_performance(elements):
    random.shuffle(elements)
    total_time = 0
    num_trials = 10

    for _ in range(num_trials):
        tree_root = build_tree(elements)
        start_time = timeit.default_timer()
        for element in elements:
            search(tree_root, element)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)

    average_time = total_time / num_trials
    return average_time, total_time

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def measure_binary_search_performance(elements):
    random.shuffle(elements)
    total_time = 0
    num_trials = 10

    for _ in range(num_trials):
        sorted_elements = sorted(elements)
        start_time = timeit.default_timer()
        for element in elements:
            binary_search(sorted_elements, element)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)

    average_time = total_time / num_trials
    return average_time, total_time

# Generate 10000-element sorted vector
sorted_vector = list(range(10000))

# Measure BST performance
bst_average_time, bst_total_time = measure_bst_performance(sorted_vector)
print("Binary Search Tree:")
print("Average Time:", bst_average_time)
print("Total Time:", bst_total_time)

# Measure Binary Search in Arrays performance
binary_search_average_time, binary_search_total_time = measure_binary_search_performance(sorted_vector)
print("\nBinary Search in Arrays:")
print("Average Time:", binary_search_average_time)
print("Total Time:", binary_search_total_time)

    


#4.Discuss: which approach is faster? Why do you think is that?
#the binary search in arrays is faster than the binary search in trees
#because the binary search in arrays has a time complexity of  O(log n), the avarage time complexity for binary search remains O(logn), regardless of the number of trails. 
#In a balanced BST, the average time complexity of the search operation is O(log n), similar to binary search in arrays
#The search operation in an unbalanced BST can become slower, especially when each search has to traverse a long path down the tree.
