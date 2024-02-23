# admin_module.py
from .store_db import Database
class Admin:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, price):
        # Add a new product to the 'products' table
        insert_query = "INSERT INTO products (name, price) VALUES (%s, %s)"
        self.db.cursor.execute(insert_query, (name, price))
        self.db.conn.commit()

    def update_product(self, product_id, new_name, new_price):
        # Update product details
        update_query = "UPDATE products SET name = %s, price = %s WHERE id = %s"
        self.db.cursor.execute(update_query, (new_name, new_price, product_id))
        self.db.conn.commit()

    def delete_product(self, product_id):
        # Delete a product by ID
        delete_query = "DELETE FROM products WHERE id = %s"
        self.db.cursor.execute(delete_query, (product_id,))
        self.db.conn.commit()



# Usage example:
if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="your_password", database="ecommerce")
    admin = Admin(db)
    admin.add_product("Laptop", 999.99)
    admin.update_product(1, "New Laptop", 1099.99)
    admin.delete_product(1)
    db.close_connection()
