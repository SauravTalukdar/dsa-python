# HashMap - Python dict-like interface using hash table
# Uses Python's built-in hash() function
# Dunder methods: __setitem__, __getitem__, __iter__, __len__, __repr__, __str__
# Collision handling: linear probing
# Time Complexity: O(1) average for insert and find
# Space Complexity: O(n)

max_hash_size = 4096
class HashMap:
    def __init__(self,max_size = max_hash_size):
        self.data_list = [None] * max_size

    def get_valid_index(self,key):
        index = hash(key) % len(self.data_list)
        while True:
            kv = self.data_list[index]
            if kv is None:
                return index
            k,v = kv
            if k == key:
                return index
            index +=1
            if index == len(self.data_list):
                index = 0        

    def __setitem__(self,key,value):
        index = self.get_valid_index(key)
        self.data_list[index] = key,value

    def __getitem__(self,key):
        index = self.get_valid_index(key)
        kv = self.data_list[index]
        if kv is None:
            return None
        else:
            k,v = kv
            return v

    def __iter__(self):
        return (x for x in self.data_list if x is not None) #iterate through all non None values

    def __len__(self):
        return len([x for x in self])     

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format('\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)

table = HashMap() #creating the object

#inserting(setting)
table['Saurav'] = '9395307918'
table['Tanushka'] = '9864013559'
table['Bhanita'] = '9445015469'
table['Bibek'] = '8475123655'

#finding(getting)
print(table['Bhanita']) 
print(table['Raktim']) #will return none

#length
print(len(table))

#dictionary like output(repr)
print(table)



                