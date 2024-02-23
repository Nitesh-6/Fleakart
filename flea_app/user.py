# user_module.py
from .store_db import Database
class User:
    def __init__(self, db):
        self.db = db

    def register_user(self, username, password):
        self.db.insert_user(username, password)

    # def authenticate_user(self, username, password):
    #     user = self.db.get_user_by_username(username)
    #     if user and user[2] == password:
    #         return True, user[0]  # Return True and the user ID
    #     return False, None

    def authenticate_user(self, username, password):
        select_query = "SELECT id, password FROM users WHERE username = %s"
        self.db.cursor.execute(select_query, (username,))
        user = self.db.cursor.fetchone()

        if user and user[1] == password:
            return True, user[0]  # Return True and the user ID
        return False, None
    def update_profile(self, user_id, new_username):
        # Update user profile logic
        update_query = "UPDATE users SET username = %s WHERE id = %s"
        self.db.cursor.execute(update_query, (new_username, user_id))
        self.db.conn.commit()

# Usage example:
if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="your_password", database="ecommerce")
    user = User(db)
    user.register_user("bob", "securepass")
    authenticated = user.authenticate_user("bob", "securepass")
    if authenticated:
        user.update_profile(1, "bobby")
    db.close_connection()
