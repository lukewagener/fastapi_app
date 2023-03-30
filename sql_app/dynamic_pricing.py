import pickle
import sklearn
import joblib as jb
import pandas as pd

def dynamic_pricing(features):
  
  #Converting 1D Json dictionary into 2D Json dictionary
  features = {'0': features}

  #Converting 2D Json Dictionary into pandas dataframe
  data = pd.DataFrame.from_dict(features, orient = 'index')
  

  #Loading the trained model
  loaded_model = jb.load("C:\Users\Xam\Documents\ACE_Space\GRYD\GrydBackend\sql_app\gryd_model.pkl")

  #making predictions from trained model
  hourly = loaded_model.predict([data])

  #defining ratios
  daily_ratio = 4.8
  weekly_ratio = 4.8*5
  monthly_ratio = 4.8*25

  #Computing prices
  daily = daily_ratio * hourly
  weekly = weekly_ratio * hourly
  monthly = monthly_ratio * hourly

  #returning predicted 
  return(hourly,daily,weekly,monthly)

#calling the function to predict price
# predicted_price = dynamic_pricing(data)

#printing the predicted price
# print(predicted_price)