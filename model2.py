predictions = model.test(testset)

rmse = np.sqrt(mean_squared_error(
    [pred.r_ui for pred in predictions],
    [pred.est for pred in predictions]
))

print("RMSE of Recommendation Model:", rmse)
