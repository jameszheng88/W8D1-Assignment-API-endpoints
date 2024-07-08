# W8D1-Assignment-API-endpoints

## Overview
This Weather App API allows users to get current weather updates by entering the name of a city. It uses the WeatherAPI to fetch real-time weather data and displays it on a web page.

## Prerequisites
- Python
- Flask
- Requests library

In addition, it is also recommended to use a virtual environment. Instructions for creating a virtual environment as well as installing flask can be found here https://flask.palletsprojects.com/en/3.0.x/installation/

## Set up instructions
1. Clone the repository
2. Install dependencies<br>
    `pip install flask requests`
3. Run the Flask Application  
    `python app.py`<br>

    The application will run on http://127.0.0.1:5000/ by default  
4. Obtain a weatherAPI Key  
    Obtain an API key from [WeatherAPI](https://www.weatherapi.com/signup.aspx) and replace the placeholder API key in `get_current_weather` function. More information about th API can be found here https://www.weatherapi.com/docs/  
   ` api_key = 'your_api_key_here'`

## Code Explanation and Usage
### HTML Template (templates/index.html)
This HTML template is used to create the front-end of the application. It uses Flask's Jinja2 templating engine to display data.

### Flask Application (app.py)
This is the main Flask application file that handles routing and server-side logic.

### Weather API Handler (weather.py)
This file contains the function to fetch weather data from the WeatherAPI.

### Usage
1.  Open the web browser and navigate to http://127.0.0.1:5000/
2.  Enter the name of a city in the input field and click the "Find" button.
3.  The current weather information for the city will be displayed on the page.