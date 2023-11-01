def print_elements(arr):
    for element in arr:
        print(element)
    for element in arr:
        print(element)
    for element in arr:
        print(element)

#merge sort O(n log n)


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
