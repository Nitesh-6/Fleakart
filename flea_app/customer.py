from store_db import ECommerceSystem


class ECommerce:
    def __init__(self):

        self.ecommerce_system = ECommerceSystem("localhost", "root", "tiger", "fleakart")
        self.products = self.ecommerce_system.get_product_list()
        self.product_catalog = []
        self.categories = {'Hats': [], 'Sneakers': [], 'Jackets': [], 'Women': [], 'Men': []}
        self.cart = []
        self.cart_value = []
        self.options = {1: 'Hats', 2: 'Sneakers', 3: 'Jackets', 4: 'Women', 5: 'Men', 6: 'proceed to cart'}
        self.stop = 0

    def populate_categories(self):
        for product in self.products:
            keys_product = ('pdt_id', 'pdt_name', 'pdt_price', 'pdt_qty', 'pdt_desc')
            res = dict(zip(keys_product, product))
            self.product_catalog.append(res)

        for product in self.product_catalog:
            for category in self.categories.keys():
                if product['pdt_desc'] == category:
                    self.categories[category].append(product)

    def shop(self):
        while self.stop < 1:
            print(self.options)
            try:
                choose_a_category = int(input("choose an option: "))
                if choose_a_category in self.options.keys():
                    sel_category = self.options.get(choose_a_category)
                    if choose_a_category <= 5:
                        [print(item) for item in self.categories[sel_category]]
                        sel_item = int(input("Select a item using pdt_id: "))
                        for item in self.categories[sel_category]:
                            try:
                                if sel_item == item['pdt_id']:
                                    print(item)
                                    self.cart.append(item['pdt_name'])
                                    self.cart_value.append(item['pdt_price'])
                            except Exception as e:
                                print(f"An error occurred: {e}")
                    else:
                        self.stop += 1
                else:
                    print("select a valid option")
            except ValueError:
                print("Please enter a valid integer.")
        print('cart items', self.cart, "\n", 'cart value', self.cart_value)


ecommerce = ECommerce()
ecommerce.populate_categories()
ecommerce.shop()
