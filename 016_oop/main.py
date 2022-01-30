class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def to_string(self):
        print(f"ID: {self.id}")
        print(f"User: {self.username}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")


user_1 = User("001", "rafael")

print(user_1.to_string())

user_2 = User("002", "gabriel")

user_2.follow(user_1)

print(user_2.to_string())
print(user_1.to_string())
