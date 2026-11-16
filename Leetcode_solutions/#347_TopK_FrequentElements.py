# Problem: Top K Frequent Elements
# LeetCode: #347
# Difficulty: Medium
# Approach1: count with a dictionary, sort the keys by count, take the first k
# Time: O(n log n) | Space: O(n)

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
    count = {} #create an empty dictionary, keys will be every numbers from nums and value will be how many times they appear
    for i in nums: #go through every number
        count[i] = count.get(i,0) + 1 #count.get() returns its current count,0 if its not been seen yet,we add one to it if we see another
        #For [1,1,1,2,2,3], after the loop:
        # count = {1: 3, 2: 2, 3: 1}
        #         key: value
    new_list = sorted(count,key = count.get,reverse=True) #sorted(count,..) sorts the list with through their keys
    #What decides the order is the values. key=lambda num: count[num] tells Python: for each number, look up its count and rank it by that.
    #number 1 → count[1] = 3
    # number 2 → count[2] = 2
    # number 3 → count[3] = 1  
    # With reverse=True, the biggest count comes first, so the result is [1, 2, 3]. 
    # The returned list holds the keys (the numbers), arranged by their values (the counts).
    # This is what we want, because the question asks for the elements, not their counts. 
    # If we sorted count.values() we’d get [3, 2, 1], the counts, and we’d lose track of which number each belongs to.   
    result = new_list[:k] #in new list the number are ordered from most to least frequent, so when we slice it till k we get the elements till k
    return result

#bucket sort solution
def topKfrequent1(nums,k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n,0) + 1
    for n,c in count.items():
        freq[c].append(n)

    result = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result        

for i, t in enumerate(tests):
    result = topKfrequent1(**t['input'])
    print(i, "PASSED" if sorted(result) == sorted(t['output']) else "FAILED")
    
