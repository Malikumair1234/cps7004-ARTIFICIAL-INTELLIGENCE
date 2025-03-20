class Node:
    def __init__(self, name):
        """
        Initializes a Node with the provided name.
        The 'parents' list is empty at first, and 'cpt' is an empty dictionary.
        """
        self.name = name
        self.parents = []  # List of parent Node objects
        self.cpt = {}      # Conditional probability table as a dictionary

    def add_parent(self, parent_node):
        """
        Adds a parent Node to the 'parents' list if it's not already a parent.
        
        Args:
            parent_node (Node): The parent node to be added.
        """
        if parent_node not in self.parents:
            self.parents.append(parent_node)

    def remove_parent(self, parent_node):
        """
        Removes a parent Node from the 'parents' list if it exists.
        
        Args:
            parent_node (Node): The parent node to be removed.
        """
        if parent_node in self.parents:
            self.parents.remove(parent_node)

    def add_cpt_entry(self, parent_states, probability):
        """
        Adds an entry to the conditional probability table (cpt) for the given parent states.
        
        Args:
            parent_states (tuple of bools): The states of the parent nodes.
            probability (float): The probability for the given parent states.
        """
        self.cpt[parent_states] = probability

    def __repr__(self):
        """
        Provides a string representation of the node for easier debugging.
        """
        return f"Node(name={self.name}, parents={self.parents}, cpt={self.cpt})"

# Example usage:
node1 = Node("Node1")
node2 = Node("Node2")
node3 = Node("Node3")

node1.add_parent(node2)
node1.add_parent(node3)

node1.add_cpt_entry((True, True), 0.9)
node1.add_cpt_entry((False, True), 0.5)

print(node1)
