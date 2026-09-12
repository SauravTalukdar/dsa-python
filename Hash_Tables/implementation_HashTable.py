# class HashTable:
#     max_hash_table_size = 4096
#     def insert(self,key,value):
#         pass
#     def find(self,key):
#         pass
#     def update(self,key,value):
#         pass
#     def list_all(self):
#         pass
       
data_list = [None] * 4096 #creating a list of fixed size(4096) with all None values

#implementing a small hashing function(to convert strings into numeric list indices)
def get_index(data_list,a_string): #takes a list an a key(which is a string here)
        result = 0 #store the result(value of indice) updated after each iteration
        for a_character in a_string: #iterate through every character of the string
            a_number = ord (a_character) #convert the charater to a number(using ord)
            result += a_number #update result by adding the number
        list_index = result % len(data_list) #take the remainder of the result with the size of the data list
        #(always lower than the max size )
        return list_index 

print(get_index(data_list, 'Hemanth'))
print(get_index(data_list, 'Saurav'))

# Now try this — what do you notice?
print(get_index(data_list, 'Aakash'))
print(get_index(data_list, 'hsaakA')) #these two give the same indice value but they are different(just changed the order of letters)