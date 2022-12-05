class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    
    def follow(self, user):
        user.followers += 1
        user.following += 1
        
        
user_1 = User(5, "user1")
user_2 = User(15, "user2")

print(user_1.id)
print(user_1.username)
print(user_1.followers)
print(user_1.following)

user_2.follow(user_1)

print(user_1.followers)
print(user_2.following)
