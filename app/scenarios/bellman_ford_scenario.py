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
    
    network.add_edge("A", "J", 25)
    network.add_edge("J", "K", -8)
    network.add_edge("K", "L", 6)
    network.add_edge("L", "D", 7)
    
    network.add_edge("A", "M", 18)
    network.add_edge("M", "N", -6)
    network.add_edge("N", "O", 10)
    network.add_edge("O", "D", 5)
    
    network.add_edge("A", "P", 35)
    network.add_edge("P", "D", 40)
    
    network.add_edge("E", "G", 12)
    network.add_edge("F", "I", 8)
    network.add_edge("H", "K", 9)
    network.add_edge("J", "M", 15)
    network.add_edge("N", "L", 7)
    network.add_edge("K", "O", 11)
    network.add_edge("M", "P", 20)
    
    network.add_edge("G", "L", -2)
    network.add_edge("J", "O", -7)
    
    return network

def create_distributed_network():
    network = Graph(directed=False)
    
    network.add_edge("R1", "R2", 5)
    network.add_edge("R2", "R3", 5)
    network.add_edge("R3", "R4", 5)
    network.add_edge("R4", "R1", 5)
    
    network.add_edge("R1", "R5", 10)
    network.add_edge("R1", "R6", 12)
    network.add_edge("R2", "R7", 8)
    network.add_edge("R2", "R8", 11)
    network.add_edge("R3", "R9", 9)
    network.add_edge("R4", "R10", 10)
    
    network.add_edge("R5", "R6", 6)
    network.add_edge("R7", "R8", 7)
    network.add_edge("R8", "R9", 8)
    network.add_edge("R9", "R10", 6)
    network.add_edge("R10", "R5", 9)
    
    network.add_edge("R5", "R11", 15)
    network.add_edge("R6", "R12", 14)
    network.add_edge("R7", "R13", 16)
    network.add_edge("R8", "R14", 13)
    network.add_edge("R9", "R15", 17)
    network.add_edge("R10", "R16", 15)
    
    network.add_edge("R11", "R12", 20)
    network.add_edge("R12", "R13", 22)
    network.add_edge("R13", "R14", 18)
    network.add_edge("R14", "R15", 21)
    network.add_edge("R15", "R16", 19)
    network.add_edge("R16", "R11", 23)
    
    network.add_edge("R5", "R8", 12)
    network.add_edge("R6", "R9", 14)
    network.add_edge("R7", "R10", 13)
    network.add_edge("R11", "R14", 25)
    network.add_edge("R12", "R15", 24)
    network.add_edge("R13", "R16", 26)
    
    return network
