# In src/tools.py

def get_dummy_weather(location: str) -> str:
    """A dummy tool that returns a fixed weather forecast."""
    print(f"--- Getting dummy weather for {location} ---")
    return "The forecast for Rajkot is sunny with no rain for the next 5 days."

def get_dummy_price(crop: str) -> str:
    """A dummy tool that returns a fixed price."""
    print(f"--- Getting dummy price for {crop} ---")
    return "Today's cotton price is Rs. 7,500 per quintal."