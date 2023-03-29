import pickle
import joblib
import pandas as pd
import json

# data = data.drop(['Unnamed: 0','index','Zone_Name','Postal_Code','Address','Latitude','Longitude','Reservation_Count','Postalcode','Scaling','Bus_Nearby','Hourly_Rate'],axis = 1)


def dynamic_pricing(features):
  
  #Converting 1D Json dictionary into 2D Json dictionary
  features = {'0': features}

  #Converting 2D Json Dictionary into pandas dataframe
  data = pd.DataFrame.from_dict(features, orient = 'index')
  

  #Loading the trained model
  loaded_model = joblib.load(filename)

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
predicted_price = dynamic_pricing(data)

#printing the predicted price
print(predicted_price)