

from flea_app.store_db import Database
from flea_app.user import User
from flea_app.business import ECommerce

def main():
    db = Database(host="localhost", user="root", password="tiger", database="flea")
    user = User(db)
    ecommerce = ECommerce(db)

    user_authenticated = False
    user_id = None

    while not user_authenticated:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user_authenticated, user_id = user.authenticate_user(username, password)

        if not user_authenticated:
            print("Invalid username or password. Please try again.")



    while True:
        print("\nWelcome to E-Commerce Console!")
        print("1. Display Categories")
        print("2. Select Category and View Products")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ecommerce.display_categories()
        elif choice == 2:
            selected_category = int(input("Select a category (1/2/3): "))
            ecommerce.display_products_by_category(selected_category)
            product_id = int(input("Enter product ID to add to cart: "))
            ecommerce.add_to_cart(user_id, product_id)
        elif choice == 3:
            # View Cart
            ecommerce.view_cart(user_id)
        elif choice == 4:
            # Checkout
            ecommerce.checkout(user_id)
        elif choice == 5:
            print("Thank you for using our e-commerce system!")
            break
        else:
            print("Invalid choice. Please try again.")

    db.close_connection()

if __name__ == "__main__":
    main()
