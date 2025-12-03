from app.algorithms import DFSRouter
from app.scenarios.dfs_scenario import create_corporate_network

def print_discovery_result(result, source):
  
    print(f"Descoberta iniciada de: {source}\n")
    
    print(f"Dispositivos descobertos: {len(result['discovery_order'])}")
    print(f"Ordem: {' -> '.join(result['discovery_order'])}\n")
    
    print("Árvore de Descoberta (hierarquia parent-child):")
    for device, parent in result['topology_tree'].items():
        if parent:
            print(f"{parent} -> {device}")
        else:
            print(f"{device} (raiz)")

def main():
    print("=" * 80)
    print("DFS - DESCOBERTA DE TOPOLOGIA DE REDE")
    print("Aplicação: Protocolo LLDP/CDP - Link Layer Discovery Protocol")
    print("=" * 80)
    print()
    
    # Criar rede corporativa
    network = create_corporate_network()
    print(f"Rede Corporativa criada: {len(network.get_vertices())} dispositivos")
    print("- Headquarters: 6 dispositivos")
    print("- Data Center: 2 dispositivos")
    print("- Branch Office 1: 5 dispositivos")
    print("- Branch Office 2: 5 dispositivos")
    print()
    
    # Descoberta de topologia a partir do Core do HQ
    print("=" * 80)
    print("DESCOBERTA DE TOPOLOGIA")
    print("=" * 80)
    print()
    
    dfs = DFSRouter()
    result = dfs.discover_topology(network, "HQ-Core-SW1")
    print_discovery_result(result, "HQ-Core-SW1")
    
    print()
    print("=" * 80)
    print("Conceito Demonstrado:")
    print("- DFS explora em profundidade, seguindo um caminho até o fim")
    print("- Usado em protocolos LLDP/CDP para mapear topologia de rede")
    print("- Identifica hierarquia e ordem de descoberta dos dispositivos")
    print("=" * 80)

if __name__ == "__main__":
    main()
