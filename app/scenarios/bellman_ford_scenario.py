from app.graph import Graph

def create_network_with_negative_weights():
    network = Graph(directed=True)
    
    network.add_edge("A", "B", 10)
    network.add_edge("B", "C", 10)
    network.add_edge("C", "D", 10)
    
    network.add_edge("A", "E", 20)
    network.add_edge("E", "F", -5)
    network.add_edge("F", "D", 5)
    
    network.add_edge("A", "G", 15)
    network.add_edge("G", "H", -3)
    network.add_edge("H", "I", -4)
    network.add_edge("I", "D", 8)
    
    return network

def create_distributed_network():
    network = Graph(directed=False)
    
    network.add_edge("R1", "R2", 5)
    network.add_edge("R1", "R3", 10)
    network.add_edge("R2", "R3", 3)
    network.add_edge("R2", "R4", 8)
    network.add_edge("R3", "R4", 2)
    network.add_edge("R3", "R5", 6)
    network.add_edge("R4", "R5", 4)
    network.add_edge("R4", "R6", 7)
    network.add_edge("R5", "R6", 5)
    
    return network

def create_network_with_penalty_links():
    network = Graph(directed=True)
    
    network.add_edge("DC1", "DC2", 50)
    network.add_edge("DC2", "DC3", 50)
    
    network.add_edge("DC1", "DC3", 120)
    
    network.add_edge("DC1", "Edge1", 30)
    network.add_edge("Edge1", "Edge2", -10)
    network.add_edge("Edge2", "DC3", 30)
    
    network.add_edge("DC1", "Premium", 40)
    network.add_edge("Premium", "DC3", -20)
    
    return network

def create_negative_cycle_network():
    network = Graph(directed=True)
    
    network.add_edge("A", "B", 5)
    network.add_edge("B", "C", 5)
    network.add_edge("C", "D", 5)
    
    network.add_edge("B", "E", 2)
    network.add_edge("E", "F", 3)
    network.add_edge("F", "B", -10)
    
    return network
