param_grid = {
    'n_factors': [20, 50, 100],
    'reg_all': [0.02, 0.05]
}

grid_search = GridSearchCV(
    SVD,
    param_grid,
    measures=['rmse'],
    cv=3
)

grid_search.fit(dataset)

print("Best RMSE:", grid_search.best_score['rmse'])
print("Best Parameters:", grid_search.best_params['rmse'])
