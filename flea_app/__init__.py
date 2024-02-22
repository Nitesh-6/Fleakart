# from store_db import ECommerceSystem
#
# ecommerce_system = ECommerceSystem("localhost", "root", "Anumula@123$", "ecomm_db")
#
# products = ecommerce_system.get_product_list()
# product_catalog = []
# hats_category = []
# sneakers_category = []
# jackets_category = []
# women_category = []
# men_category = []
# cart = []
# stop = 0
# options = {1: 'Hats', 2: 'Sneakers', 3: 'Jackets', 4: 'Women', 5: 'Men', 6: 'proceed to cart'}
# for product in products:
#     keys_product = ('pdt_id', 'pdt_name', 'pdt_price', 'pdt_qty', 'pdt_desc')
#     res = dict(zip(keys_product, product))
#     product_catalog.append(res)
#
#
# for hat in product_catalog:
#     if hat['pdt_desc'] == 'Hats':
#         hats_category.append(hat)
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
#     if man['pdt_desc'] == 'Men':
#         men_category.append(man)
# while stop < 1:
#     print(options)
#     choose_a_category = int(input("choose an option: "))
#     if choose_a_category in options.keys():
#         sel_category = options.get(choose_a_category)
#         if choose_a_category == 1:
#             [print(hat) for hat in hats_category]
#             sel_item = int(input("Select a item using pdt_id: "))
#             for hat in hats_category:
#                 if sel_item == hat['pdt_id']:
#                     print(hat)
#                     cart.append(hat)
#         elif choose_a_category == 2:
#             [print(sneaker) for sneaker in sneakers_category]
#             sel_item = int(input("Select a item using pdt_id: "))
#             for sneaker in sneakers_category:
#                 if sel_item == sneaker['pdt_id']:
#                     print(sneaker)
#                     cart.append(sneaker)
#         elif choose_a_category == 3:
#             [print(jacket) for jacket in jackets_category]
#             sel_item = int(input("Select a item using pdt_id: "))
#             for jacket in jackets_category:
#                 if sel_item == jacket['pdt_id']:
#                     print(jacket)
#                     cart.append(jacket)
#         elif choose_a_category == 4:
#             [print(women) for women in women_category]
#             sel_item = int(input("Select a item using pdt_id: "))
#             for women in women_category:
#                 if sel_item == women['pdt_id']:
#                     print(women)
#                     cart.append(women)
#         elif choose_a_category == 5:
#             [print(men) for men in men_category]
#             sel_item = int(input("Select a item using pdt_id: "))
#             for men in men_category:
#                 if sel_item == men['pdt_id']:
#                     print(men)
#                     cart.append(men)
#         else:
#             stop += 1
#     else:
#         print("select a valid option")
# for i in cart:
#     print(i)
