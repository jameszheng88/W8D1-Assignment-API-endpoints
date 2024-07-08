import requests

# Function for getting weather info
def get_current_weather(my_city):
    
    # API endpoint
    url = "http://api.weatherapi.com/v1/current.json"
    api_key  = '27be6b2de5a74c0d9bd185026240107'
    city = my_city

    # Additional parameters required by weatherapi.com
    params = {
    "key": api_key,
    "q": city,
    }

    # Fetching the request from weather API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        
        # Parsing the data 
        weather_data = {
            "City": f'{data["location"]["name"]}, {data["location"]["region"]}',
            "Current temperature": f'{data["current"]["temp_f"]} F',
            "Current Weather condition": f'{data["current"]["condition"]['text']}',
            "Icon": f'{data["current"]["condition"]['icon']}',
            "Current Humidity": f'{data["current"]["humidity"]}%',
            "Current Wind Speed": f'{data["current"]["wind_mph"]} MPH'
        }

        return weather_data

    else:
        # Prints if a non-valid city was entered
        print("Please enter a valid City")
