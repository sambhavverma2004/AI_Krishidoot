import requests

# Your actual API key from openweathermap.org
API_KEY = "b1e6b35205dc4102e12a861e549c56f4"
# This is the correct API endpoint for current weather data.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_hyperlocal_weather(location: str) -> str:
    """
    Fetches hyper-local weather data from the OpenWeatherMap API.
    This function acts as the ClimaScout Agent.

    Args:
        location: The city name (e.g., 'Rajkot', 'Jamnagar').

    Returns:
        A string describing the current weather conditions or an error message.
    """
    # Set up the parameters for the API request
    params = {
        'q': f"{location},IN",  # Specify city and country code for accuracy
        'appid': API_KEY,
        'units': 'metric'      # Request temperature in Celsius
    }

    try:
        # Make the GET request to the API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        # Extract the useful information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Format the output into a clear, human-readable string
        return (f"Weather in {location.title()}: "
                f"{weather_description.title()}, {temperature}°C, "
                f"{humidity}% humidity, and wind at {wind_speed} m/s.")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return f"Error: Could not find weather for '{location}'. Please check the spelling."
        elif response.status_code == 401:
             return (f"Error: API key is inactive or invalid (HTTP 401). "
                     f"New keys may take a few hours to activate on OpenWeatherMap.")
        else:
            return f"Error: An HTTP error occurred: {http_err}"
    except requests.exceptions.JSONDecodeError:
        return f"Error: Failed to decode server response. The API URL or endpoint may be incorrect."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Example of how to use the ClimaScout agent for the Saurashtra region ---
if __name__ == "__main__":
    # A list of major cities in the Saurashtra region
    saurashtra_cities = [
        "Rajkot",
        "Jamnagar",
        "Bhavnagar",
        "Junagadh",
        "Porbandar",
        "Amreli",
        "Surendranagar"
    ]

    print("--- Fetching Weather for Key Cities in Saurashtra ---")
    for city in saurashtra_cities:
        weather_report = get_hyperlocal_weather(city)
        print(weather_report)