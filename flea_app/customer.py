from store_db import get_product_list, connect_to_database
connect = connect_to_database()


def populate_categories(products, product_catalog, categories):
    for product in products:
        keys_product = ('pdt_id', 'pdt_name', 'pdt_price', 'pdt_qty', 'pdt_desc')
        res = dict(zip(keys_product, product))
        product_catalog.append(res)

    for product in product_catalog:
        for category in categories.keys():
            if category.lower() in product['pdt_desc'].lower():
                categories[category].append(product)


def shop(options, categories, cart, cart_value, products):
    stop = 0
    while stop < 1:
        print(options)
        try:
            choose_a_category = int(input("choose an option: "))
            if choose_a_category in options.keys():
                sel_category = options.get(choose_a_category)
                if choose_a_category <= 5:
                    [print(item) for item in categories[sel_category]]
                    sel_item = int(input("Select an item using pdt_id: "))
                    for item in categories[sel_category]:
                        try:
                            if sel_item == item['pdt_id']:
                                print(item)
                                cart.append(item['pdt_name'])
                                cart_value.append(item['pdt_price'])
                        except Exception as e:
                            print(f"An error occurred: {e}")
                else:
                    stop += 1
            else:
                print("select a valid option")
        except ValueError:
            print("Please enter a valid integer.")
    print("cart", '\t', '\t', 'value')
    for i in range(len(cart)):
        print(cart[i], '\t', cart_value[i])


def exe():
    products = get_product_list(connect)
    product_catalog = []
    categories = {'Hats': [], 'Sneakers': [], 'Jackets': [], 'Women': [], 'Men': []}
    cart = []
    cart_value = []
    options = {1: 'Hats', 2: 'Sneakers', 3: 'Jackets', 4: 'Women', 5: 'Men', 6: 'proceed to cart'}

    populate_categories(products, product_catalog, categories)
    shop(options, categories, cart, cart_value, products)


# exe()
