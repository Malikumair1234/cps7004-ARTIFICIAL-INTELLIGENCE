# config.py

# Simulation name
SIMULATION_NAME = "OceanSim"

# Ocean size (grid dimensions)
OCEAN_SIZE = 20  # 20x20 grid (can be adjusted as needed)

# Colours for each agent
AGENT_COLORS = {
    'shark': "red",      # Shark agent color
    'fish': "blue",      # Fish agent color
    'seaweed': "green"   # Seaweed agent color
}

# Breeding probabilities for each agent (between 0 and 1)
BREEDING_PROBABILITIES = {
    'shark': 0.1,   # Probability of shark breeding
    'fish': 0.3,    # Probability of fish breeding
    'seaweed': 0.05 # Probability of seaweed breeding
}
