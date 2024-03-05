def crop_predict(N,P,K,temperature,humidity,ph,rainfall):
    import joblib
    model="/home/harsh/HARSH/projects/vcet hackathon 2k22 takshak farmer assistant/functions/croprec.pkl"
    model = joblib.load(model)
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    return prediction

#yieldPredict(90,42,43,20.87974371,82.00274423,6.502985292000001,202.9355362,model)