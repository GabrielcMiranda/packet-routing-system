from app.graph import Graph

def create_dijkstra_network():
    network = Graph(directed=False)

    network.add_edge("Nucleo-A", "Nucleo-B", 100)
    network.add_edge("Nucleo-B", "Nucleo-C", 100)
    network.add_edge("Nucleo-C", "Nucleo-A", 100)

    network.add_edge("Nucleo-A", "Dist-Norte", 1000)
    network.add_edge("Nucleo-B", "Dist-Leste", 1000)
    network.add_edge("Nucleo-B", "Dist-Sul", 1000)
    network.add_edge("Nucleo-C", "Dist-Oeste", 1000)
    network.add_edge("Dist-Norte", "Dist-Leste", 1000)
    network.add_edge("Dist-Sul", "Dist-Oeste", 1000)
    network.add_edge("Dist-Oeste", "Dist-Norte", 1000)

    network.add_edge("Dist-Norte", "Escritorio-Remoto1", 64000)
    network.add_edge("Dist-Norte", "Escritorio-Remoto2", 64000)
    network.add_edge("Dist-Leste", "Escritorio-Remoto3", 64000)
    network.add_edge("Dist-Sul", "Escritorio-Remoto4", 64000)

    network.add_edge("Dist-Oeste", "Acesso-Bairro1", 1000)
    network.add_edge("Dist-Leste", "Acesso-Bairro2", 1000)
    network.add_edge("Dist-Sul", "Acesso-Bairro3", 1000)
    network.add_edge("Dist-Norte", "Acesso-Bairro4", 1000)

    network.add_edge("Escritorio-Remoto1", "Escritorio-Remoto2", 200000)
    network.add_edge("Escritorio-Remoto2", "Escritorio-Remoto3", 200000)
    network.add_edge("Escritorio-Remoto3", "Escritorio-Remoto4", 200000)

    network.add_edge("Acesso-Bairro1", "Escritorio-Remoto1", 200000)
    network.add_edge("Acesso-Bairro2", "Escritorio-Remoto3", 200000)
    network.add_edge("Acesso-Bairro3", "Escritorio-Remoto4", 200000)
    network.add_edge("Acesso-Bairro4", "Escritorio-Remoto2", 200000)

    network.add_edge("Gateway-Perimetral", "Nucleo-C", 1000)
    network.add_edge("Gateway-Perimetral", "Acesso-Bairro1", 200000)

    return network

def create_simple_comparison_network():
    network = Graph(directed=False)
    
    network.add_edge("A", "B", 10)
    network.add_edge("B", "D", 10)
    network.add_edge("A", "C", 100)
    network.add_edge("C", "D", 10)
    
    return network
