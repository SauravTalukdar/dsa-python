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
        'nums': [],'k' : 1,
    }, 'output' : []
}
test4 = {
    'input' : {
        'nums': [1,2,3,4,5],'k' : 5,
    }, 'output' : [1,2,3,4,5]
}
test5 = {
    'input' : {
        'nums': [3,3,3,3,3],'k' : 1,
    }, 'output' : [3]
}
test6 = {
    'input' : {
        'nums': [-3,-3,-1,-1,2],'k' : 2,
    }, 'output' : [-3,-1]
}

tests = [test0,test1,test2,test3,test4,test5,test6]

def topKfrequent(nums,k):
    count = {}
    for i in nums:    
        count[i] = count.get(i,0) + 1
    new_list = sorted(count,key = lambda num: count[num],reverse=True)      
    result = new_list[:k]
    return result

for i, t in enumerate(tests):
    result = topKfrequent(**t['input'])
    print(i, "PASSED" if sorted(result) == sorted(t['output']) else "FAILED")
    

