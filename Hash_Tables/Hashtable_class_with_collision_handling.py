# Hash Table with Linear Probing — Complete Implementation
# Handles collisions using get_valid_index (linear probing)
# Operations: insert, find, update, list_all — all O(1) ,average
# Note: infinite loop risk if table(list) completely full

class HashTable:
    def __init__(self,max_size):
        self.data_list = [None] * max_size #creating a datalist 

    def get_index(self,data_list,a_string): #getting the index(hash function)
        result = 0
        for a_character in a_string:
            a_number = ord (a_character)
            result += a_number
        list_index = result % len(data_list)
        return list_index 

    def get_valid_index(self,data_list,key):
        idx = self.get_index(data_list,key) 

        while True:
            kv = data_list[idx] 

            if kv is None: 
                return idx

            k,v = kv
            if k == key:
                return idx 
            idx +=1 

            if idx ==len(data_list):
                idx = 0    

    def insert(self,key,value): #inserting value
        idx = self.get_valid_index(self.data_list,key)
        self.data_list[idx] = key,value

    def find(self,key): #finding value
        idx = self.get_valid_index(self.data_list,key)
        kv= self.data_list[idx]
        if kv is None: #if none return node
            return None
        else:
            key,value  = kv
            return value    

    def update(self,key,value): #updating value
        self.data_list[self.get_valid_index(self.data_list,key)] = key,value

    def list_all(self): #listing all the values(or key,values)
        return [item for item in self.data_list if item is not None]

hashtable = HashTable(4000) #created a hashtable class with list size 400

#inserting some key,values
hashtable.insert('saurav','8471855733')
hashtable.insert('ausrav','8471855733')
hashtable.insert('Tanushka','9231325312')
hashtable.insert ('silent','9489484949')
hashtable.insert('listen', '9595949494')

#finding a key
print(hashtable.find('Tanushka'))
print(hashtable.find('Bibek')) #will give None as output(as the key is not in the list)

#updating
hashtable.insert('silent', '9489484949')
print(hashtable.find('silent'))  #original number
hashtable.update('silent', '1111111111')
print(hashtable.find('silent'))  #should show updated number

#list_all
print(hashtable.list_all()) 

#getting the hash value(checking the value)
print(hashtable.get_valid_index(hashtable.data_list,'silent'))
print(hashtable.get_valid_index(hashtable.data_list,'listen'))
print(hashtable.get_valid_index(hashtable.data_list,'saurav'))
print(hashtable.get_valid_index(hashtable.data_list,'ausrav'))
        