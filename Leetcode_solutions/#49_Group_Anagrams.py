'''
Given an array of strings(strs), we need to group the anagrams together. You can return the answer in any order
'''
#test cases
strs0 = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output0 = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs1 = [""]
Output1 = [[""]]

strs2 = ["a"]
Output2 = [["a"]]

strs3 = ["bat","nat","tea"]
Output3 = [["bat"],["nat"],["tea"]]

strs4 = ["stop","tops","pots","spot"]

'''
we can sort each word in the array and whichever word matches one another we can group them together.
we can use a loop and sort every word in the array. and use another loopto check which mathches its sorted word. 
then use list comprehension to group them together
'''
def group_anagram(strs):
    result = [] 
    discovered = False * len(strs)
    for i in range(len(strs)):
        var = [strs[i]]
        if strs[i] not in result:
            result.append(var)  
        for j in range(i+1,len(strs)):
            if str[j] is not discovered and sorted(strs[i]) == sorted(strs[j]):
                var.append(strs[j])
                discovered[j] = True

    return result

print(group_anagram(strs0))

