# Problem: Handling a dtabase of users(inserting,finding,updating,listing)
# Time complexity: O(n)
# Space complexity: O(1)
# Approch: Brute force


class User: #created a user class to store of users (input)
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Username: {self.username}, name: {self.name}, email: {self.email}"

    def __str__(self):
        return self.__repr__()


class UserDatabase: #user database class for methods 
    def __init__(self):
        self.users = []
    def insert(self,user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i,user)    
    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self,user):
        target = self.find(user.username)
        target.name = user.name
        target.email = user.email
    def list_all(self):
        return self.users

#creating some users

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
saurav = User("saurav","sauravtalukdar","saurav@gmail")            
tanushka = User("tanushka","tanushkaroy","tanushka@gmail")            
bibek = User("bibek","bibekroy","bibek@gmail")            
raktim = User("raktim","raktimborah","raktim@gmail")  

users = [aakash,biraj,hemanth,jadhesh,bibek,sonaksh,vishal] #optional for now as we directly insert users in self.users

database = UserDatabase() #created a database object for the use of methods

#1. inserting some users
database.insert(hemanth)
database.insert(bibek)
database.insert(aakash)
database.insert(saurav)
database.insert(tanushka)

#2. Finding a user
found_user = database.find("hemanth")
print(found_user)

#3. Updating a users details
database.update(User("hemanth","hemu","hello@gmail"))
print(hemanth)

#4. Listing all the user details
print(database.list_all())



