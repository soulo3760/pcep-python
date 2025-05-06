import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables from .env file
API_KEY = os.getenv('api_key')
API_URL = os.getenv('api_Url')

# Check if the API key is set
if API_KEY is None:
    raise ValueError("API_KEY is not set in the environment variables.")

# Define the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}   

#request weather for a specific city
city = "Nairobi"
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract relevant information
    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    
    # Print the weather information
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description}")
else:
    # Print an error message if the request failed
    print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
    print(f"Response: {response.text}")
    
# Save the weather data to a file
with open('weather_data.json', 'w') as file:
    json.dump(data, file, indent=4)
    

