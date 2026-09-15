# Problem: Contains Duplicate
# LeetCode: #217
# Difficulty: Easy
# Time Complexity: O(n) — set approach
# Space Complexity: O(n)

#given an integer array. return True if any value appears twice in the array, or return false if every value is distict.
#input = interger array
#output = true or false

#test cases:
#1. [1,2,3,4] no duplicates , output = false
#2. [1,2,3,1] one number repeats , output = true
#3. [1,2,3,1,5,2] multiple number repeats , output = true
#4. [] no elements, output = false
#5. [1,1,1,1,1] only one element and it repeats, output = true
#6. [2] only one element in the list, output = false

#approach : we can have a list and keep adding elements of nums in it.(brute force)
# when we encounter a number that is already in the new list we return true and end the loop
#time complexity is O(n^2)
def contains_duplicate(nums):
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
        else:
            return True
    return False

#using a set(hash) to do the problem in O(n) time complexity
def contains_duplicate1(nums):
    saw = set()
    for num in nums:
        if num in saw:
            return True
        saw.add(num)
    return False             

print(contains_duplicate1([1,2,3,4]))                
print(contains_duplicate1([1,2,3,1]))                
print(contains_duplicate1([1,2,3,1,5,2]))                
print(contains_duplicate1([]))                
print(contains_duplicate1([1,1,1,1,1]))                
print(contains_duplicate1([2]))                
               