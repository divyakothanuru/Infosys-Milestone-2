user_id = 1
recommended_products = recommend_products(user_id)

print("Top Recommendations for User", user_id)
for product in recommended_products:
    print(product)
