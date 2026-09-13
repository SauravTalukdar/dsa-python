# Hash Table Implementation
# Operations: insert, find, update, list_all
# Uses hash function: sum of ASCII values % list size
# Time Complexity: O(1)
# Space Complexity: O(n)
# Note: current version doesn't handle collisions

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

    def insert(self,key,value): #inserting value
        idx = self.get_index(self.data_list,key)
        self.data_list[idx] = key,value

    def find(self,key): #finding value
        idx = self.get_index(self.data_list,key)
        kv= self.data_list[idx]
        if kv is None: #if none return node
            return None
        else:
            key,value  = kv
            return value    

    def update(self,key,value): #updating value
        self.data_list[self.get_index(self.data_list,key)] = key,value

    def list_all(self): #listing all the values(or key,values)
        phone_number = [item for item in self.data_list if item is not None]
        return phone_number


hashtable = HashTable(400) #created a hashtable class with list size 400

#inserting some key,values
hashtable.insert('Saurav','8471855733')
hashtable.insert('Tanushka','9231325312')
hashtable.insert ('Aakash','9489484949')
hashtable.insert('Hemanth', '9595949494')

#finding a key
print(hashtable.find('Tanushka'))
print(hashtable.find('Bibek')) #will give None as output(as the key is not in the list)

#updating
hashtable.update('Hemanth','455454')

#list_all
print(hashtable.list_all())

