class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following +=1

timmy = User("001","timmy1")
jimmy = User("002","timmy1")
print(timmy)

timmy.follow(jimmy)
print(timmy.following)
print(jimmy.following)
print(timmy.followers)
print(jimmy.followers)