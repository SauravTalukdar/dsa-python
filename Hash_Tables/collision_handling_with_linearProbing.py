def get_index(data_list,a_string): 
    result = 0
    for a_character in a_string:
        a_number = ord (a_character) 
        result += a_number
    list_index = result % len(data_list) 
    return list_index 

def get_valid_index(data_list,key):
    idx = get_index(data_list,key) #we get the index from get index

    while True: #runs till it finds an empty slot(insert here) or the same key(update here)
        kv = data_list[idx] #get the key value pair at that index and store it 

        if kv is None: #if there are no key,value at the position we return the index
            return idx

        k,v = kv #store key,and value in k and v respectively
        if k == key: #check if the k(key) is equal to the given key
            return idx #return the index
        idx +=1 #and increase it by one(next index), we keep doing this until we find a empty space

        if idx ==len(data_list): #if we have reached the end of the list,go back to the start
            idx = 0 #made index 0(start)

data_list = [None] * 4096

#inserting values
#the hash value of both listen and silent is 655(causing collison)
data_list[get_valid_index(data_list,'listen')] = 'listen','9489484949' #we insert this at 655
data_list[get_valid_index(data_list,'silent')] = 'silent','9231325312' #we insert this at 656(which is the next index,cause 655 is occupied)  

print(get_valid_index(data_list,'listen')) #655
print(get_valid_index(data_list,'silent')) #656(if there was no key in 655 it would have shown 655)