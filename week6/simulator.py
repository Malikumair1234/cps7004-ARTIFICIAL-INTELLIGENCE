# simulator.py

from typing import List
from random import random
from view.gui import OceanSimulatorGUI
from config import OCEAN_SIZE, AGENT_COLORS, BREEDING_PROBABILITIES


class Simulator:
    """
    Simulator class to manage the ocean simulation.
    
    This class handles the main simulation logic, including managing agents,
    grid setup, and updating agent states.
    """

    def __init__(self, ocean_size: int = OCEAN_SIZE) -> None:
        """
        Initializes the simulator with a given ocean size and creates the simulation grid.
        
        Args:
            ocean_size (int): The size of the ocean grid (default is 20x20).
        """
        self.ocean_size = ocean_size
        self.grid = self.create_ocean_grid()

    def create_ocean_grid(self) -> List[List[str]]:
        """
        Creates the ocean grid, initially filled with empty spaces.
        
        Returns:
            List[List[str]]: A 2D list representing the ocean grid with empty cells.
        """
        return [[" " for _ in range(self.ocean_size)] for _ in range(self.ocean_size)]

    def place_agents(self) -> None:
        """
        Places agents (sharks, fish, and seaweed) randomly in the ocean grid.
        
        Each agent type is assigned a random position on the grid based on the breeding probabilities.
        """
        # Placeholder: Actual agent placement would involve more logic
        for row in range(self.ocean_size):
            for col in range(self.ocean_size):
                rand = random()
                if rand < BREEDING_PROBABILITIES['shark']:
                    self.grid[row][col] = "shark"
                elif rand < BREEDING_PROBABILITIES['fish'] + BREEDING_PROBABILITIES['shark']:
                    self.grid[row][col] = "fish"
                elif rand < BREEDING_PROBABILITIES['seaweed'] + BREEDING_PROBABILITIES['fish'] + BREEDING_PROBABILITIES['shark']:
                    self.grid[row][col] = "seaweed"

    def run_simulation_step(self) -> None:
        """
        Runs one step of the simulation, updating the state of the ocean grid.
        
        This could involve moving agents, breeding, and other behaviors.
        """
        # Placeholder: Actual simulation logic would involve updating the agents' states
        pass

    def display_ocean(self) -> None:
        """
        Displays the current state of the ocean grid in the console.
        """
        for row in self.grid:
            print(" ".join(row))

    def start_gui(self) -> None:
        """
        Starts the GUI to display the simulation.
        """
        gui = OceanSimulatorGUI(simulation_name="OceanSim", ocean_size=self.ocean_size)
        gui.create_window()


# Example usage:
if __name__ == "__main__":
    simulator = Simulator()
    simulator.place_agents()
    simulator.display_ocean()
    simulator.start_gui()
