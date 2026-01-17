reader = Reader(rating_scale=(1, 5))

dataset = Dataset.load_from_df(
    data[['user_id', 'product_id', 'rating']],
    reader
)
