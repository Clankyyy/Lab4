def print_elements(arr):
    for element in arr:
        print(element)
    for element in arr:
        print(element)
    for element in arr:
        print(element)

#merge sort O(n log n)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#O(n!)
import itertools

def generate_permutations(input_list):
    permutations = list(itertools.permutations(input_list))
    return permutations

n = 4  # Change this value to the desired input size
input_list = list(range(n))

permutations = generate_permutations(input_list)

for p in permutations:
    print(p)

#O(n^3)

def cubic_algorithm(numbers):
    n = len(numbers)
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result += numbers[i] * numbers[j] * numbers[k]
    return result

#O(3 log n)

import bisect

def three_log_n_search(arr1, arr2, arr3, target):
    # Perform three binary searches, one for each array
    index1 = bisect.bisect_left(arr1, target)
    index2 = bisect.bisect_left(arr2, target)
    index3 = bisect.bisect_left(arr3, target)
    
    return (index1, index2, index3)

# Example usage
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = three_log_n_search(arr1, arr1, arr1, target)
print("Indices where target is found:", result)
