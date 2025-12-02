from app.graph import Graph

def create_dijkstra_network():
    network = Graph(directed=False)
    
    network.add_edge("Core-A", "Core-B", 100)
    network.add_edge("Core-B", "Core-C", 100)
    network.add_edge("Core-C", "Core-A", 100)
    
    network.add_edge("Core-A", "Dist-North", 1000)
    network.add_edge("Core-B", "Dist-South", 1000)
    network.add_edge("Core-C", "Dist-East", 1000)
    network.add_edge("Core-A", "Dist-West", 1000)
    
    network.add_edge("Dist-North", "Remote-Office1", 64000)
    network.add_edge("Dist-South", "Remote-Office2", 64000)
    network.add_edge("Dist-East", "Remote-Office3", 64000)
    
    network.add_edge("Remote-Office1", "Remote-Office2", 200000)
    network.add_edge("Remote-Office2", "Remote-Office3", 200000)
    
    network.add_edge("Dist-North", "Dist-South", 1000)
    network.add_edge("Dist-South", "Dist-East", 1000)
    
    return network

def create_simple_comparison_network():
    network = Graph(directed=False)
    
    network.add_edge("A", "B", 10)
    network.add_edge("B", "D", 10)
    network.add_edge("A", "C", 100)
    network.add_edge("C", "D", 10)
    
    return network
