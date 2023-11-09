class User:
    pass
# This keyword allows you to bypass the function or class without having any code under it


user_1 = User()
user_1.id = "001"
user_1.username = input("Please choose a username: ")
print(f"{user_1.username} is available")


class UserCreated:
    def __int__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
# You have already set a default value for followers. Doesn't need to be added in the arguments of function.

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_2 = UserCreated()
user_2.__int__('002','mohana1240')
print(user_2.id)
print(user_2.username)

user_3 = UserCreated()
user_3.__int__('003', 'kirankn')

user_2.follow(user_3)  # User 2 has decided to follow user 3 - user 2 following and user 3 followers increases by 1
print(user_2.following)
print(user_3.followers)

