from app.graph import Graph


def create_metropolitan_network() -> Graph:
    
    network = Graph(directed=False)
    
    network.add_edge("Core-Central", "Core-Norte", 2)
    network.add_edge("Core-Norte", "Core-Leste", 2)
    network.add_edge("Core-Leste", "Core-Sul", 2)
    network.add_edge("Core-Sul", "Core-Central", 2)
    
    network.add_edge("Core-Central", "Core-Leste", 3)
    network.add_edge("Core-Norte", "Core-Sul", 3)
    
    network.add_edge("Core-Norte", "Dist-ZonaNorte1", 5)
    network.add_edge("Core-Norte", "Dist-ZonaNorte2", 6)
    network.add_edge("Dist-ZonaNorte1", "Dist-ZonaNorte2", 8)
    
    network.add_edge("Core-Sul", "Dist-ZonaSul1", 5)
    network.add_edge("Core-Sul", "Dist-ZonaSul2", 7)
    network.add_edge("Dist-ZonaSul1", "Dist-ZonaSul2", 9)
    
    network.add_edge("Core-Leste", "Dist-ZonaLeste", 4)
    
    network.add_edge("Core-Central", "Dist-ZonaCentral", 3)
    
    network.add_edge("Dist-ZonaNorte1", "Access-Bairro1", 10)
    network.add_edge("Dist-ZonaNorte2", "Access-Bairro2", 12)
    network.add_edge("Dist-ZonaSul1", "Access-Bairro3", 11)
    network.add_edge("Dist-ZonaSul2", "Access-Bairro4", 10)
    network.add_edge("Dist-ZonaLeste", "Access-Bairro5", 15)
    network.add_edge("Dist-ZonaCentral", "Access-Centro", 8)

    network.add_edge("Access-Bairro1", "Dist-ZonaNorte2", 13)
    network.add_edge("Access-Bairro3", "Dist-ZonaSul2", 14)
    
    return network
