"""Authentication logic (no input()/print(), so it works inside Streamlit)."""


class Authentication:
    def __init__(self):
        # username -> {"email": ..., "password": ...}
        self.users = {}

    def sign_up(self, email, username, password):
        """Register a new user. Returns (success, message)."""
        email = email.strip()
        username = username.strip()

        # check if the email is valid
        if "@" not in email or not email.endswith(".com"):
            return False, "Invalid email"
        # check that a username was entered
        if not username:
            return False, "Please enter a username"
        # check if the username is already registered
        if username in self.users:
            return False, "This username is already registered"
        # check if the password is at least 8 characters
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"

        # save new user information
        self.users[username] = {"email": email, "password": password}
        return True, "Registration successful!"

    def validate_user(self, username, password):
        """Check the username and password."""
        user = self.users.get(username.strip())
        return user is not None and user["password"] == password
