import mysql.connector


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anumula@123$",
        database="ecomm_db"
    )


def disconnect_from_database(connection):
    connection.close()


def authenticate_user(username, password, connection):
    # global cursor
    try:
        cursor = connection.cursor()

        # Query to authenticate user
        query = "SELECT * FROM Users WHERE email_id = %s AND passkey = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        return user
    except Exception as e:
        print(e)

    finally:
        # Close cursor
        cursor.close()


def get_product_list(connection):
    # global cursor
    try:
        cursor = connection.cursor()

        # Query to fetch product list
        query = "SELECT * FROM Products"
        cursor.execute(query)
        products = cursor.fetchall()

        return products
    except Exception as e:
        print(e)

    finally:
        # Close cursor (no need to close the connection here)
        cursor.close()


def login():
    while True:
        # Connect to MySQL database
        db_connection = connect_to_database()

        try:
            # User authentication
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = authenticate_user(username, password, db_connection)

            if user:
                print("Login successful.")
                break  # Break the loop if login is successful
            else:
                print("Invalid username or password. Please try again.")

        finally:
            # Close database connection
            disconnect_from_database(db_connection)


login()
