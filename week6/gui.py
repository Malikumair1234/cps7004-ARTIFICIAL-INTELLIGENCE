# gui.py

import tkinter as tk
from tkinter import messagebox
from typing import Optional


class OceanSimulatorGUI:
    """
    A simple GUI class for the Ocean Simulator.

    This class creates a basic GUI to interact with the ocean simulation.
    """

    def __init__(self, simulation_name: str, ocean_size: int) -> None:
        """
        Initializes the OceanSimulatorGUI with the provided simulation name and ocean size.

        Args:
            simulation_name (str): The name of the simulation.
            ocean_size (int): The size of the ocean grid (assumed to be square).
        """
        self.simulation_name = simulation_name
        self.ocean_size = ocean_size
        self.window: Optional[tk.Tk] = None

    def create_window(self) -> None:
        """
        Creates the main window for the simulation GUI.
        """
        self.window = tk.Tk()
        self.window.title(self.simulation_name)

        # Add a label to display the simulation name
        label = tk.Label(self.window, text=f"Welcome to {self.simulation_name}!", font=("Arial", 16))
        label.pack(pady=10)

        # Add a button to start the simulation
        start_button = tk.Button(self.window, text="Start Simulation", command=self.start_simulation)
        start_button.pack(pady=10)

        # Add a button to exit the simulation
        exit_button = tk.Button(self.window, text="Exit", command=self.window.quit)
        exit_button.pack(pady=10)

        # Add a label for ocean size
        ocean_size_label = tk.Label(self.window, text=f"Ocean Size: {self.ocean_size}x{self.ocean_size}", font=("Arial", 12))
        ocean_size_label.pack(pady=10)

        self.window.mainloop()

    def start_simulation(self) -> None:
        """
        Starts the simulation. This method could be extended to handle the logic of running the simulation.
        For now, it will just show a message box.

        """
        messagebox.showinfo("Simulation Started", f"The {self.simulation_name} simulation has started!")
        # This could be the place to trigger the simulation logic

    def display_error(self, error_message: str) -> None:
        """
        Displays an error message in the GUI.

        Args:
            error_message (str): The error message to display.
        """
        messagebox.showerror("Error", error_message)


# Example usage:
if __name__ == "__main__":
    gui = OceanSimulatorGUI(simulation_name="OceanSim", ocean_size=20)
    gui.create_window()
