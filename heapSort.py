import random

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# generate a list of 10 random numbers
random_list = random.sample(range(-100, 100), 201)
print("Original list:")
print_array(random_list)

heapSort(random_list)
print("Sorted list:")
print_array(random_list)
