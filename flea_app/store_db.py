import mysql.connector  # Import the mysql.connector module to connect to MySQL databases


class ECommerceSystem:  # Define a class named ECommerceSystem to encapsulate the functionality
    def __init__(self, host, user, password, database):  # Constructor method to initialize class attributes
        self.host = host  # Set the host attribute
        self.user = user  # Set the user attribute
        self.password = password  # Set the password attribute
        self.database = database  # Set the database attribute

    def connect(self):  # Method to establish a connection to the MySQL database
        self.db_connection = mysql.connector.connect(  # Connect to the database using the provided credentials
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db_connection.cursor()  # Create a cursor object to execute SQL queries

    def disconnect(self):  # Method to close the database connection
        self.cursor.close()  # Close the cursor object
        self.db_connection.close()  # Close the database connection

    def authenticate_user(self, username, password):  # Method to authenticate a user
        self.connect()  # Establish a connection to the database
        query = "SELECT * FROM Users WHERE email_id = %s AND passkey = %s"  # SQL query to fetch user data
        self.cursor.execute(query, (username, password))  # Execute the query with username and password parameters
        user = self.cursor.fetchone()  # Fetch the first row of the result set
        self.disconnect()  # Close the database connection
        return user  # Return the user data, if found

    def get_product_list(self):  # Method to fetch the list of products from the database
        self.connect()  # Establish a connection to the database
        query = "SELECT * FROM Products"  # SQL query to fetch all products
        self.cursor.execute(query)  # Execute the query
        products = self.cursor.fetchall()  # Fetch all rows of the result set
        self.disconnect()  # Close the database connection
        return products  # Return the list of products

    def main(self):  # Main method to handle user interaction
        username = input("Enter your emailid: ")  # Prompt the user to enter their username
        password = input("Enter your password: ")  # Prompt the user to enter their password
        user = self.authenticate_user(username, password)  # Authenticate the user

        if user:  # If authentication is successful
            print("Login successful.")  # Print a success message
            # products = self.get_product_list()  # Fetch the list of products
            # print("Product List:")  # Print a header for the product list
            # for product in products:  # Iterate over the list of products
            #     print(product)  # Print each product (modify this to display product details in a user-friendly format)
        else:  # If authentication fails
            print("Invalid username or password.")  # Print an error message


if __name__ == "__main__":  # Check if the script is being run directly
    ecommerce_system = ECommerceSystem("localhost", "root", "Anumula@123$",
                                       "ecomm_db")  # Create an instance of the ECommerceSystem class with database credentials
    ecommerce_system.main()  # Call the main method to start the program
