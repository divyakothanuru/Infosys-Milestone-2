train_data, test_data = train_test_split(
    data, test_size=0.2, random_state=42
)

testset = [
    (row['user_id'], row['product_id'], row['rating'])
    for _, row in test_data.iterrows()
]
