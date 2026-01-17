def recommend_products(user_id, top_n=5):
    product_ids = data['product_id'].unique()
    recommendations = []

    for product_id in product_ids:
        prediction = model.predict(user_id, product_id)
        recommendations.append((product_id, prediction.est))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]
