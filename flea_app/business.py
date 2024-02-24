# business_logic.py
from .store_db import Database
class ECommerce:
    def __init__(self, db):
        self.db = db

    def display_categories(self):
        # Display available categories
        print("Available Categories:")
        print("1. Electronics")
        print("2. Clothing")
        print("3. Books")
        # Add more categories as needed

    # def display_products_by_category(self, category_id):
    #     # Retrieve and display products based on the selected category
    #     select_query = "SELECT id, name, price FROM products WHERE category_id = %s"
    #     self.db.cursor.execute(select_query, (category_id,))
    #     products = self.db.cursor.fetchall()
    #     print("Products in this category:")
    #     for product in products:
    #         print(f"{product[0]}. {product[1]} - ${product[2]:.2f}")
    def display_products_by_category(self, category_id):
        # Retrieve and display products based on the selected category
        select_query = "SELECT id, name, price FROM products WHERE category_id = %s"
        self.db.cursor.execute(select_query, (category_id,))
        products = self.db.cursor.fetchall()
        print("Products in this category:")
        for product in products:
            print(f"{product[0]}. {product[1]} - ${product[2]:.2f}")
            
    def add_to_cart(self, user_id, product_id):
        # Add a product to the user's cart
        insert_query = "INSERT INTO cart (user_id, product_id) VALUES (%s, %s)"
        self.db.cursor.execute(insert_query, (user_id, product_id))
        self.db.conn.commit()
        print("Product added to cart successfully!")

    def remove_from_cart(self, user_id, product_id):
        # Remove a product from the user's cart
        delete_query = "DELETE FROM cart WHERE user_id = %s AND product_id = %s"
        self.db.cursor.execute(delete_query, (user_id, product_id))
        self.db.conn.commit()
        print("Product removed from cart successfully!")

    def calculate_order_total(self, user_id):
        # Calculate the total price of items in the user's cart
        select_query = """
            SELECT SUM(p.price)
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = %s
        """
        self.db.cursor.execute(select_query, (user_id,))
        total_price = self.db.cursor.fetchone()[0]
        return total_price

    def view_cart(self, user_id):
        # Retrieve and display products in the user's cart
        select_query = """
            SELECT p.id, p.name, p.price
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = %s
        """
        self.db.cursor.execute(select_query, (user_id,))
        cart_items = self.db.cursor.fetchall()

        if not cart_items:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in cart_items:
                print(f"{item[0]}. {item[1]} - ${item[2]:.2f}")
    # def checkout(self, user_id):
    #     # Simulate the checkout process
    #     total_price = self.calculate_order_total(user_id)
    #     print(f"Total order amount: ${total_price:.2f}")
    #     # Implement other checkout steps (e.g., payment, order confirmation)
    def checkout(self, user_id):
        # Simulate the checkout process
        total_price = self.calculate_order_total(user_id)
        if total_price == 0:
            print("Your cart is empty. Nothing to checkout.")
        else:
            print(f"Total order amount: ${total_price:.2f}")
            # Implement other checkout steps (e.g., payment, order confirmation)
            print("Checkout successful! Thank you for your purchase.")
            # Clear the user's cart after checkout
            self.clear_cart(user_id)

    def clear_cart(self, user_id):
        # Clear all items from the user's cart
        delete_query = "DELETE FROM cart WHERE user_id = %s"
        self.db.cursor.execute(delete_query, (user_id,))
        self.db.conn.commit()
# Usage example:
if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="tiger", database="flea")
    ecommerce = ECommerce(db)
    # Assume user is logged in with user_id = 1
    ecommerce.add_to_cart(user_id=1, product_id=2)  # Example: Adding product with ID 2 to the cart
    ecommerce.remove_from_cart(user_id=1, product_id=3)  # Example: Removing product with ID 3 from the cart
    total_order = ecommerce.calculate_order_total(user_id=1)
    print(f"Total order amount: ${total_order:.2f}")
    # Add other business logic-related code here
    db.close_connection()
