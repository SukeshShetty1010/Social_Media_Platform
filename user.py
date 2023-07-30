from post import Post  # Import the Post class from post.py

class User:
    def __init__(self, name, address, email, username):
        self.name = name  # Set the user's name
        self.address = address  # Set the user's address
        self.email = email  # Set the user's email
        self.username = username  # Set the user's username
        self.posts = []  # Initialize an empty list to store the user's posts
        self.comments = []  # Initialize an empty list to store the user's comments on posts
        self.friends = set()  # Initialize an empty set to store the user's friends

    def post_message(self, message):
        post = Post(self, message)  # Create a Post object with the user and message
        self.posts.append(post)  # Add the post to the user's posts list

    def comment_on_post(self, post, comment):
        self.comments.append((post, comment))  # Add a tuple (post, comment) to the user's comments list

    def follow_user(self, user):
        if user != self:
            self.friends.add(user)  # Add the specified user to the user's friends set, if they are not the user themselves

    def get_friend_suggestions(self):
        friend_suggestions = set()
        for friend in self.friends:
            for suggested_friend in friend.friends:
                if suggested_friend != self and suggested_friend not in self.friends:
                    friend_suggestions.add(suggested_friend)  # Add suggested friends to the friend_suggestions set
        return friend_suggestions

    def like_post(self, post):
        post.add_like()  # Call the add_like method of the specified post to increment its likes count

    def display_posts(self):
        for post in self.posts:
            print(f"{self.username}: {post.content}")  # Display the user's posts along with their username

        if not self.posts:
            print(f"{self.username} has no posts yet.")  # Display a message if the user has no posts

    def display_friends(self):
        for friend in self.friends:
            print(friend.username)  # Display the username of each user in the user's friends set

    def __str__(self):
        return self.username  # Return the user's username when the User object is converted to a string
