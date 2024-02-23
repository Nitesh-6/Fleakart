

import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Create users and products tables
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
        """
        self.cursor.execute(create_users_table)
        self.cursor.execute(create_products_table)
        self.conn.commit()

    def insert_user(self, username, password):
        # Insert a new user into the 'users' table
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (username, password))
        self.conn.commit()

    def get_user_by_username(self, username):
        # Retrieve user details by username
        select_query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(select_query, (username,))
        return self.cursor.fetchone()

    # Implement other CRUD operations (select, update, delete)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Usage example:
if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="tiger", database="flea")
    db.create_tables()
    db.insert_user("alice", "password123")
    user = db.get_user_by_username("alice")
    print(user)  # Example: (1, 'alice', 'password123')
    db.close_connection()
