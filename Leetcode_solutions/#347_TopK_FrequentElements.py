# Problem: Top K Frequent Elements
# LeetCode: #347
# Difficulty: Medium
# Approach 1: count with a dictionary, sort the keys by count, take the first k. O(n log n)
# Approach 2: bucket sort, count used as an index. O(n)

'''
Given an integer array, nums, and an integer k, return the K most frequent elements. You may return the answer in any order.
For example if k = 2, we need to return the two most frequent(repeated elements from the array)

'''

#test cases
test0 = {
    'input' : {
        'nums' : [1,1,1,2,2,3], 'k' : 2,
    }, 'output' : [1,2]
}
test1 = {
    'input' : {
        'nums': [1],'k' : 1,
    }, 'output' : [1]
}
test2 = {
    'input' : {
        'nums': [1,2,1,2,1,2,3,1,3,2],'k' : 2,
    }, 'output' : [1,2]
}

test3 = {
    'input' : {
        'nums': [1,2,3,4,5],'k' : 5,
    }, 'output' : [1,2,3,4,5]
}
test4 = {
    'input' : {
        'nums': [3,3,3,3,3],'k' : 1,
    }, 'output' : [3]
}
test5 = {
    'input' : {
        'nums': [-3,-3,-1,-1,2],'k' : 2,
    }, 'output' : [-3,-1]
}

tests = [test0,test1,test2,test3,test4,test5]

def topKfrequent(nums,k):
    count = {} #create an empty dictionary
    for i in nums: #go through every number
        count[i] = count.get(i,0) + 1 
        #For [1,1,1,2,2,3], after the loop:
        # count = {1: 3, 2: 2, 3: 1}
        #         key: value
    new_list = sorted(count,key = count.get,reverse=True) #sorted(count,..) sorts the list with through their keys
    #What decides the order is the values. key= count.get tells Python: for each number, look up its count and rank it by that.   
    result = new_list[:k] #in new list the number are ordered from most to least frequent, so when we slice it till k we get the elements till k
    return result

# Approach 2: bucket sort by frequency
# Time: O(n) | Space: O(n)
# Idea: use the count as a list index. freq[c] holds every number that appears c times.
#       Read the buckets from the highest count down and stop once k numbers are collected.
# Why O(n): counting, filling the buckets and reading them are each one pass, and no sort is needed.

def topKfrequent1(nums,k):
    count = {}  #dict for counts
    freq = [[] for i in range(len(nums) + 1)] #create list of lists where index is the count and value is the numbers(or list of numbers)

    for n in nums:
        count[n] = count.get(n,0) + 1  #count the frequency of every number

    for n,c in count.items(): #(number,count) pairs for each n,c
        freq[c].append(n) #go to box number c(count) and put n(number) in it

    result = [] #an empty list for the answers
    for i in range(len(freq)-1,0,-1): #traverse from the last of the freq list to the 1th index(example - 7 indexes , it goes like 6,5,4,3,2,1)
        for n in freq[i]: #look inside box i . every number in it appears i times 
            result.append(n) #add each one to the result
            if len(result) == k: #when the result is equal to k elements
                return result #return it
    return result            


for i, t in enumerate(tests):
    result = topKfrequent1(**t['input'])
    print(i, "PASSED" if sorted(result) == sorted(t['output']) else "FAILED")
    
