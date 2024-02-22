from store_db import ECommerceSystem

ecommerce_system = ECommerceSystem("localhost", "root", "Anumula@123$", "ecomm_db")

products = ecommerce_system.get_product_list()
updated_products = []
product_catalog = []
hats_category = []
sneakers_category = []
jackets_category = []
women_category = []
men_category = []
stop = 0
options = {1: 'Hats', 2: 'Sneakers', 3: 'Jackets', 4: 'Women', 5: 'Men'}
# print(products)
# for product in products:
#     keys_product = ('pdt_id', 'pdt_name', 'pdt_price', 'pdt_qty', 'pdt_desc')
#     res = dict(zip(keys_product, product))
#     product_catalog.append(res)
for product in products:
    product = list(product)
    updated_products.append(product)
print(updated_products)


for hat in updated_products:
    print(hat)
    if hat == 'Hats':
        hats_category.append(hat)
print(hats_category)
#
# for sneaker in product_catalog:
#     if sneaker['pdt_desc'] == 'Sneakers':
#         sneakers_category.append(sneaker)
#
# for jacket in product_catalog:
#     if jacket['pdt_desc'] == 'Jackets':
#         jackets_category.append(jacket)
#
# for woman in product_catalog:
#     if woman['pdt_desc'] == 'Women':
#         women_category.append(woman)
#
# for man in product_catalog:
#     if man['pdt_desc'] == 'men':
#         men_category.append(man)
#
# while stop < 1:
#     print(options)
#     choose_a_category = int(input("choose an option: "))
#     if choose_a_category in options.keys():
#         sel_category = options.get(choose_a_category)
#         if choose_a_category == 1:
#             print("Select a Category")
#             [print(hat) for hat in hats_category]
#     else:
#         pass
#     stop += 1
