# We are given two sequences,we need to find the length of the longest common subsequence.
# QUESTION: Write a function to find the length of the longest common subsequence between two sequences.
# E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence 
# is "reipito" and its length is 7.

# A "sequence" is a group of items with a deterministic ordering.
# Lists, tuples and ranges are some common sequence types in Python.
# A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. 
# For example, "edpt" is a subsequence of "serendipitous".

#test cases
# 1.General case (string)
# 2.General case (list)
# 3.No common subsequence
# 4.One is a subsequence of the other
# 5.One sequence is empty
# 6.Both sequences are empty
# 7.Multiple subsequences with same length
# “abcdef” and “badcfe”
T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0 #there are no common subsequence so the empty sequence is a subsequence
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

#recursive solution
#Time complexity - O(2^m+n)
#Space Complexity: O(m+n) — recursion call stack
def len_lcs(seq1,seq2,idx1 = 0,idx2 = 0): #take two sequences and two indexes(idx1 of seq1,idx2 of idx2 both staarting from 0)
    if idx1 == len(seq1) or idx2 == len(seq2): #if any one sequence is exhausted,no more characters to compare
        return 0                               #No common subsequence possible from here. Return 0.
    elif seq1[idx1] == seq2[idx2]: #Current characters match — this character is part of the LCS.
        return 1 + len_lcs(seq1,seq2,idx1 + 1,idx2 + 1) # Count it (+1) and recursively 
        # call the functions and move both pointers forward to find more matches.    
    else: #characters dont match,skip one character from either sequence and try both possibilities.
        option1 = len_lcs(seq1,seq2,idx1 + 1,idx2)  
        option2 = len_lcs(seq1,seq2,idx1,idx2 + 1)   
        return max(option1,option2) #Take the maximum — whichever gives a longer subsequence.  

#solution with memoization(memorization), we track recurring elements with a dictionary
#Time complexity - O(m*n)
#Space Complexity: O(m*n)
def lcs_memo(seq1,seq2):
    memo = {} #we store already computed results for specific pairs(idx1,idx2)
              #because of this we compute every unique pair only once
    def recurse(idx1=0,idx2=0): #we create a helper function with idx1 = 0 and idx2 = 0
        key = (idx1,idx2) #we store the pair
        if key in memo: #if it is in already in memo
            return memo[key] #return the computed result
        elif idx1 == len(seq1) or idx2 == len(seq2): #same as recursion solution
            memo[key] = 0 #the length is 0, store it in the memo
        elif seq1[idx1] == seq2[idx2]: #same as recursion solution
            memo[key] = 1 + recurse(idx1+1,idx2+1) #add one to result and increase both pointers
        else:
            memo[key] = max(recurse(idx1+1,idx2),recurse(idx1,idx2+1)) #check max and store the result in memo[key]
        return memo[key] #return the result which is in memo[key]
    return recurse(0,0) #make the initial call with idx1 = 0 and idx2 = 0

#dynamic programming solution
#we will create a 2D array to store combinations for both positions(i,j) for both sequences(seq1,seq2) together
#Time complexity - O(n1*n2)
#Space Complexity: O(n1*n2)
def lcs_dp(seq1,seq2):
    n1,n2 = len(seq1),len(seq2) #we are storing the lengths of both sequences(to use them for loops and size bounds)
    table = [[0 for x in range(n2+1)]for x in range (n1+1)] #we are creating a row of n2+1 zeros(columns) 
    #and n1+1 rows(this is the table),n1+1 and n2+1 as we want the empty string case to be handled
    # For exaxmple - seq1="abc" (n1=3) and seq2="ac" (n2=2):
    # n1+1 = 4 rows
    # n2+1 = 3 columns
    # table =
    #     [0, 0, 0],   # row 0
    #     [0, 0, 0],   # row 1
    #     [0, 0, 0],   # row 2
    #     [0, 0, 0],   # row 3
    for i in range(n1): #iterate through every pair
        for j in range(n2): 
            if seq1[i] == seq2[j]: #characters match
                table[i+1][j+1] = 1 + table[i][j] #length = 1 (this character) + LCS of everything before both characters
                                                #(table[i][j] = diagonal cell).
            else:#Characters don't match
                table[i+1][j+1] = max(table[i][j+1],table[i+1][j])#table[i][j+1],cell above → skip current seq1 character
            # table[i+1][j] — cell to left → skip current seq2 character, then take max of both(whichever gives longer lcs)
    return table[-1][-1] #last row and last column element(or element at the last of last row), it is the lcs                  
            
#testing
test_cases = [T0,T1,T2,T3,T4,T5,T6,T7]
for i, test in enumerate(test_cases):
    result = lcs_dp(test['input']['seq1'], test['input']['seq2'])
    passed = result == test['output']
    status = "PASSED" if passed else "FAILED"
    print(f"Test {i}: {status} | Expected: {test['output']}, Got: {result}")