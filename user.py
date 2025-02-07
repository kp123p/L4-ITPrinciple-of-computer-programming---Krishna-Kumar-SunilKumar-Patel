class User:

    def __init__(self, username, password, email ):
        self.username = username
        self.email = email
        self.password = password

    def register(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        print(f"User {self.username} registered successfully.")
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"User {self.username} logged in successfully.")
            return True
        else:
            print("Login failed. Please check your username and password.")
            return False