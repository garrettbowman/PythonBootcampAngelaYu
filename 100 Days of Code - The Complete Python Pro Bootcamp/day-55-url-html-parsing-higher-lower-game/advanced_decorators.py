class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].logged_in == True:
            return function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post")

new_user = User("gary")
new_user.logged_in = True
create_blog_post(new_user)