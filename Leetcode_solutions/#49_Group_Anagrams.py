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
Output4 = [["stop"],["tops"],["pots"],["spot"]]

#brute force solution
def group_anagram(strs):
    result = [] #create a resulting list (which will contain list of lists)
    discovered = [False] * len(strs) #create a way to mark the positions as discovered(to handle duplication)
    for i in range(len(strs)): #run from position i to len(strs)
        if not discovered[i]: #if we have not discovered i
            group = [strs[i]] #create a group and put the element(i) in it
            result.append(group) #add the group to the result 
            discovered[i] = True #mark i as discovered
            for j in range(i+1,len(strs)): #start another loop(j) from i+1 to len(strs)
                if not discovered[j] and sorted(strs[i]) == sorted(strs[j]): #if j is not discovered and the sorted of i and j are equal
                    group.append(strs[j]) #we add j to the group of this i
                    discovered[j] = True #then mark j as discovered
                    
    #this will create the list of anagrams 
    return result #return the result
print(group_anagram(strs0))

