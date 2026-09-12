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

#OPERATIONS
#1.inserting key,value in the hash table
key,value = 'Aakash','9489484949'
index = get_index(data_list,key)
data_list[index] = (key,value)

#the same insertion implementation in a single line of code
data_list[get_index(data_list,'Hemanth')] = ('Hemanth', '9595949494')
data_list[get_index(data_list,'Saurav')] = ('Saurav', '8457548856')
data_list[get_index(data_list,'Aakash')] = ('Aakash','9489484949')
data_list[get_index(data_list,'Siddhant')] = ('Siddhant','9231325312')

#2.finding a value
print(data_list[get_index(data_list,'Hemanth')]) #we got the index using the hash function and retrived the key and value
#OR
idx = get_index(data_list,'Saurav') #getting the index and storing it in idx
key,value = data_list[idx] #unpacking the key and tuple at the index
print(value) #getting the value

#3.Updating a value
data_list[get_index(data_list,'Saurav')] = 'Saurav','8471855733'

#List_all
#approach1
for item in data_list:
    if item is not None:
        print(f"Name:{item[0]},Phone:{item[1]}")

#approch2->List comprehension(better)
phone_number = [item for item in data_list if item is not None]
print(phone_number)



