# In src/agents.py
from crewai import Agent
from src.tools import get_dummy_weather # Import the tool

# Define the ClimaScout Agent
clima_scout = Agent(
    role='Weather Specialist',
    goal='Provide accurate, hyper-local weather forecasts for a given location.',
    backstory='An expert meteorologist dedicated to helping farmers by providing crucial weather data.',
    tools=[get_dummy_weather], # Assign the dummy tool
    allow_delegation=False,
    verbose=True
)

# TODO: Define the other 4 agents (TerraMoist, PestPredict, MarketPulse, ProfitPilot)
# TODO: Define the EcoAdvisor (leader) agent