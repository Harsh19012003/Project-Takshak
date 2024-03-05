def yieldPredict(state,Crop_Year,season,crop,area,model,mydict):
	model="/home/harsh/HARSH/projects/vcet hackathon 2k22 takshak farmer assistant/functions/yieldpred.pkl"
    model = joblib.load(model)
    mydict= json.load(open("/home/harsh/HARSH/projects/vcet hackathon 2k22 takshak farmer assistant/functions/yieldpred.txt"))
    state=mydict[state]
    season=mydict[season]
    crop=mydict[crop]
    prediction=model.predict([[state,Crop_Year,season,crop,area]])
    return(print(prediction))

# //////////////////////uncomment below to test///////////////////////////

# state='NICOBARS'	
# crop_year=2000.0	
# season='Kharif'	
# crop='Arecanut'	
# area=1254.0	
# yieldPredict(state,crop_year,season,crop,area,model,mydict)
