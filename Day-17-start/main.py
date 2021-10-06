class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0
        print("New user being created...")

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = User("001", "JamesNine")
user2 = User("002", "NakedOrca")

print(user1.username)

user1.follow(user2)


