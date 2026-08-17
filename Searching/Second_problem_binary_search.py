# applying binary search with list comprehension

def binary_search(numbers,query):
    low = 0
    high = len(numbers) - 1
    while (low<=high):
        mid = (low + high) // 2
        mid_number = numbers[mid]
        if mid_number == query:
            return mid
        elif mid_number < query:
            high = mid - 1
        elif mid_number > query:
            low = mid + 1
    return -1

numbers = [n for n in range(10000000,1000001,-1)]
query = int(input("Enter a perfect square number between 1 and 10 million :"))
print(binary_search(numbers,query))



