"""
Single Responsibility Priciple
"""

# Bad Example


class User:

    """This class has multiple responsibility to take care."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def login(self, email, password):
        pass

    def user_profile(self, email):
        pass

    def change_password(self, email):
        pass

    def change_email(self, email, new_email):
        pass


# Good Example


class User:

    """Each class has it's own responsibility to take the task."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Login(User):

    """This class takes care of logging function."""

    def login(self):
        pass


class UserProfile(User):

    """This class takes case of getting user profile."""

    def get_user_profile(self):
        pass


class UpdateProfile(UserProfile):

    """This class takes care of updating user profile."""

    def update(self):
        pass

