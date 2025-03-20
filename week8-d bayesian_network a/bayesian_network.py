class BayesianNetwork:
    def __init__(self):
        """
        Initializes an empty Bayesian network with a dictionary to store nodes.
        The keys are node names (strings), and the values are instances of the Node class.
        """
        self.nodes = {}  # Dictionary to store nodes, key is the node's name

    def add_node(self, node_name):
        """
        Adds a node to the network.
        
        Args:
            node_name (str): The name of the node to add.
        
        Returns:
            Node: The newly created Node object.
        """
        if node_name not in self.nodes:
            new_node = Node(node_name)
            self.nodes[node_name] = new_node
            return new_node
        else:
            raise ValueError(f"Node with name {node_name} already exists.")

    def add_edge(self, parent_name, child_name):
        """
        Adds an edge from the parent node to the child node in the network.
        
        Args:
            parent_name (str): The name of the parent node.
            child_name (str): The name of the child node.
        
        Raises:
            ValueError: If either the parent or child node does not exist.
        """
        if parent_name in self.nodes and child_name in self.nodes:
            parent_node = self.nodes[parent_name]
            child_node = self.nodes[child_name]
            child_node.add_parent(parent_node)
        else:
            raise ValueError("Both parent and child nodes must exist in the network.")

    def get_node(self, node_name):
        """
        Retrieves a node by its name.
        
        Args:
            node_name (str): The name of the node to retrieve.
        
        Returns:
            Node: The node object associated with the given name.
        """
        return self.nodes.get(node_name, None)

    def __repr__(self):
        """
        Provides a string representation of the entire Bayesian network.
        """
        return f"BayesianNetwork(nodes={self.nodes})"

# Unit Tests

import unittest

class TestBayesianNetwork(unittest.TestCase):

    def test_add_node(self):
        network = BayesianNetwork()
        node1 = network.add_node("Node1")
        self.assertEqual(node1.name, "Node1")
        self.assertIn("Node1", network.nodes)
        self.assertEqual(len(network.nodes), 1)

    def test_add_edge(self):
        network = BayesianNetwork()
        node1 = network.add_node("Node1")
        node2 = network.add_node("Node2")
        network.add_edge("Node1", "Node2")
        
        # Check if Node1 is a parent of Node2
        self.assertIn(node1, node2.parents)

    def test_add_edge_invalid_node(self):
        network = BayesianNetwork()
        network.add_node("Node1")
        with self.assertRaises(ValueError):
            network.add_edge("Node1", "NonExistentNode")

    def test_get_node(self):
        network = BayesianNetwork()
        node1 = network.add_node("Node1")
        node = network.get_node("Node1")
        self.assertEqual(node, node1)
        self.assertIsNone(network.get_node("NonExistentNode"))

    def test_node_creation_check(self):
        network = BayesianNetwork()
        node1 = network.add_node("Node1")
        node2 = network.add_node("Node2")
        self.assertNotEqual(node1, node2)  # Ensure they are distinct objects

if __name__ == "__main__":
    unittest.main()

