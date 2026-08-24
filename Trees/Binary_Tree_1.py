class User: #created a user class to store of users 
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Username {self.username}, name {self.name}, email {self.email}"

    def __str__(self):
        return self.__repr__()

                