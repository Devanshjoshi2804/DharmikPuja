import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def analyze_sorting_algorithm(algorithm, sizes):
    print(f"Analyzing {algorithm.__name__} algorithm:")
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        start_time = time.time()
        algorithm(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Sorted {size} elements in {execution_time:.6f} seconds.")

# Example usage:
sizes = [100, 500, 1000, 5000]
analyze_sorting_algorithm(bubble_sort, sizes)
analyze_sorting_algorithm(insertion_sort, sizes)
analyze_sorting_algorithm(selection_sort, sizes)
