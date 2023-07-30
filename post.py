class Post:
    def __init__(self, user, content):
        """
        Constructor for the Post class.

        Parameters:
        - user (User): The user who created the post.
        - content (str): The content of the post.
        """
        self.user = user        # Store the user who created the post
        self.content = content  # Store the content of the post
        self.likes = 0          # Initialize the number of likes to 0

    def add_like(self):
        """
        Increment the number of likes for the post by 1.
        """
        self.likes += 1

    def __str__(self):
        """
        String representation of the Post object.

        Returns:
        str: A string containing the username of the post creator and the post content.
        """
        return f"{self.user.username}: {self.content}"
