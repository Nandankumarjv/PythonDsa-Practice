class User:
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email

    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"

    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users=[]

    def insert(self,user):
        i=0
        while i<len(self.users):
            if self.users[i].username>user.username:
                break
            i+=1
        self.users.insert(i,user)

    
    def find(self,username):
        for user in self.users:
            if user.username==username:
                return user

    def update(self,user):
        toUpdate=self.find(user.username)
        if toUpdate is not None:
            toUpdate.name=user.name
            toUpdate.email=user.email
        
    def list(self):
        return self.users


user1=User("Alice","alice","aice@gmail.com")
user2=User("Bob","bob","bob@gmail.co.")
user3=User("Cherry","cherry","c@gmail.com")
user4=User("Chi","che","che@mail.com")
user5=User("Abhay","abhay","a@gmail.com")
db=UserDatabase()
db.insert(user1)
db.insert(user2)
db.insert(user3)
db.insert(user4)
db.insert(user5)
print(db.list())
print(db.find('abhay'))
db.update(User(username='abhay',name='Abhayyy',email='abhayy@gmail.com'))
find_user=db.find('abhay')
print(find_user)