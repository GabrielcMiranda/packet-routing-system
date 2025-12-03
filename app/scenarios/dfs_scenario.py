from app.graph import Graph


def create_corporate_network() -> Graph:
   
    network = Graph(directed=False)
    
    network.add_edge("HQ-Core-SW1", "HQ-Core-SW2", 1)
    network.add_edge("HQ-Core-SW1", "HQ-Dist-SW1", 5)
    network.add_edge("HQ-Core-SW1", "HQ-Dist-SW2", 5)
    network.add_edge("HQ-Core-SW2", "HQ-Dist-SW1", 5)
    network.add_edge("HQ-Core-SW2", "HQ-Dist-SW2", 5)
    
    network.add_edge("HQ-Dist-SW1", "HQ-Dist-SW2", 2) 
    network.add_edge("HQ-Dist-SW1", "HQ-Access-SW1", 10)
    network.add_edge("HQ-Dist-SW2", "HQ-Access-SW2", 10)
    
    network.add_edge("DC-Core-SW1", "DC-Core-SW2", 1)
    
    network.add_edge("DC-Core-SW1", "HQ-Core-SW1", 20)
    network.add_edge("DC-Core-SW2", "HQ-Core-SW2", 20)
    
    network.add_edge("Branch1-Router", "Branch1-SW1", 5)
    network.add_edge("Branch1-Router", "Branch1-SW2", 5)
    network.add_edge("Branch1-SW1", "Branch1-SW2", 2)  
    network.add_edge("Branch1-SW1", "Branch1-Access1", 10)
    network.add_edge("Branch1-SW2", "Branch1-Access2", 10)
    
    network.add_edge("Branch1-Router", "HQ-Core-SW1", 50)
    
    network.add_edge("Branch2-Router", "Branch2-SW1", 5)
    network.add_edge("Branch2-Router", "Branch2-SW2", 5)
    network.add_edge("Branch2-SW1", "Branch2-SW2", 2)  
    network.add_edge("Branch2-SW1", "Branch2-Access1", 10)
    network.add_edge("Branch2-SW2", "Branch2-Access2", 10)
    
    network.add_edge("Branch2-Router", "HQ-Core-SW2", 50)
    
    network.add_edge("Branch1-Router", "Branch2-Router", 60)
    
    return network
