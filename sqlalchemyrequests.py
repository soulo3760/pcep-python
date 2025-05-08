import requests
import os
from dotenv import load_dotenv 
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

api_key = os.getenv("api_key")
url = f"https://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid={api_key}"

response = requests.get(url)
data = response.json()

data
# city name, description, humidity,temp
if response.status_code == 200:
   city = data.get('name')
   temperature = data['main']['temp']
   humidity = data['main']['humidity']
   description = data['weather'][0]['description']

   weather_data = {
       'City' : [city],
       'Temperature(k)' : [temperature],
       'Humidity(%)' : [humidity],
       'Description' : [description]
   }

   df = pd.DataFrame(weather_data)
   print(df)
else:
    print(f"Error! : {response.status_code}")


host = os.getenv("host")
password = os.getenv("password")
user = os.getenv("user")
name = os.getenv("database_name")
port = os.getenv("port")

# Creating the sqlachemy engine
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}") 


df.to_sql("nairobi_weather", engine, if_exists="replace", index=False)
