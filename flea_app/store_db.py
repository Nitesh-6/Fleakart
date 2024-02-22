import mysql.connector

class ECommerceSystem:
    """A class representing an E-commerce system for connecting to MySQL databases."""

    def __init__(self, host, user, password, database):
        """Initialize the ECommerceSystem with database connection parameters.

        Args:
            host (str): The hostname or IP address of the MySQL server.
            user (str): The MySQL user.
            password (str): The password for the MySQL user.
            database (str): The name of the MySQL database.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Establish a connection to the MySQL database."""
        self.db_connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db_connection.cursor()

    def disconnect(self):
        """Close the database connection and cursor."""
        self.cursor.close()
        self.db_connection.close()

    def authenticate_user(self, username, password):
        """Authenticate a user based on the provided username and password.

        Args:
            username (str): The email ID of the user.
            password (str): The password for authentication.

        Returns:
            tuple or None: A tuple containing user data if authentication is successful, else None.
        """
        self.connect()
        query = "SELECT * FROM Users WHERE email_id = %s AND passkey = %s"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def get_product_list(self):
        """Fetch the list of products from the database.

        Returns:
            list: A list of tuples representing product data.
        """
        self.connect()
        query = "SELECT * FROM Products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        self.disconnect()
        return products

    def main(self):
        """Main method to run the E-commerce system."""
        while True:
            username = input("Enter your email id: ")
            password = input("Enter your password: ")
            user = self.authenticate_user(username, password)

            if user:
                print("Login successful.")
                # Uncomment the following lines to fetch and display the product list
                # products = self.get_product_list()
                # print("Product List:")
                # for product in products:
                #     print(product)
                break  # Break the loop if authentication is successful
            else:
                print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    ecommerce_system = ECommerceSystem("localhost", "root", "tiger", "fleakart")
    ecommerce_system.main()
