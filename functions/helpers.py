def crop_predict(N,P,K,temperature,humidity,ph,rainfall):
    import joblib
    import sklearn
    model="/home/devmurari/HARSH/PROJECT_OPS/takshak_farmer_assistant_vcet_hackathon_2022/takshak/functions/crop_predict.pkl"
    model = joblib.load(model)
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    return prediction

def yield_predict(state,crop_year,season,crop,area):
    import joblib
    import json
    model="/home/harsh/HARSH/projects/vcet hackathon 2k22 takshak farmer assistant/functions/yieldpred.pkl"
    model = joblib.load(model)
    mydict= json.load(open("/home/harsh/HARSH/projects/vcet hackathon 2k22 takshak farmer assistant/functions/yieldpred.txt"))
    state=mydict[state]
    season=mydict[season]
    crop=mydict[crop]
    prediction=model.predict([[state,crop_year,season,crop,area]])
    return(print(prediction))

# //////////////////////uncomment below to test///////////////////////////

# state='NICOBARS'	
# crop_year=2000.0	
# season='Kharif'	
# crop='Arecanut'	
# area=1254.0	
# yieldPredict(state,crop_year,season,crop,area,model,mydict)
