from app.algorithms import BellmanFordRouter, DijkstraRouter, format_bellman_ford_result, format_bellman_ford_routing_table
from app.scenarios.bellman_ford_scenario import create_network_with_negative_weights, create_distributed_network

def print_algorithm_info():
    print("Características do Algoritmo Bellman-Ford")
    print("=========================================")
    
    print('Pesos Negativos        -> SIM     | Suporta links com custos negativos')
    print('Roteamento Distribuído -> SIM     | Modelo usado no RIP')
    print('Complexidade           -> O(V*E)  | Mais lento que Dijkstra')
    
    print("\nCasos de Uso:")
    print('1. Cenários onde links podem ter "descontos" ou penalidades')
    print('2. Roteamento distribuído - Protocolo RIP (Routing Information Protocol)\n')

def demonstrate_negative_weights():
    print("PESOS NEGATIVOS - VANTAGEM DO BELLMAN-FORD")
    
    print("Cenário: Rede com links de cache (pesos negativos)")
    print("1. Rota direta: A -> B -> C -> D (custo 30)")
    print("2. Rota com cache: A -> E -> F(cache) -> D (custo 20)")
    print("3. Rota com múltiplos caches: A -> G -> H(cache) -> I(cache) -> D (custo 16)\n")
    
    network = create_network_with_negative_weights()
    source, dest = "A", "D"
    
    bf_router = BellmanFordRouter()
    bf_result = bf_router.find_shortest_path(network, source, dest)
    print(format_bellman_ford_result(bf_result, source, dest))

def demonstrate_distributed_routing():
    print("ROTEAMENTO DISTRIBUÍDO - SIMULAÇÃO RIP")
    
    network = create_distributed_network()
    
    print("Rede com 16 roteadores (R1 a R16)")
    
    source, dest = "R1", "R16"
    
    bf_router = BellmanFordRouter()
    bf_result = bf_router.find_shortest_path(network, source, dest)
    print(format_bellman_ford_result(bf_result, source, dest))
    
    print("Tabela de Roteamento Completa:")
    routing_table = bf_router.calculate_routing_table(network, source)
    print(format_bellman_ford_routing_table(routing_table, source))

def compare_with_dijkstra():
    print("COMPARAÇÃO: BELLMAN-FORD vs DIJKSTRA")
    
    print(f"Bellman-Ford encontra rota com cache (peso negativo), Dijkstra não suporta\n")
    
    network = create_network_with_negative_weights()
    source = 'A'
    dest = 'D'
    
    bf_router = BellmanFordRouter()
    dijkstra_router = DijkstraRouter()
    
    bf_result = bf_router.find_shortest_path(network, source, dest)
    print(f"Bellman-Ford:")
    if bf_result:
        path = " -> ".join(bf_result['path'])
        print(f"Caminho: {path}")
        print(f"Custo: {bf_result['cost']}")
        print(f"Iterações: {bf_result['iterations']}")
    
    print(f"\nDijkstra:")
    try:
        dijk_result = dijkstra_router.find_shortest_path(network, source, dest)
        if dijk_result:
            path = " -> ".join(dijk_result['path'])
            print(f"Caminho: {path}")
            print(f"Custo: {dijk_result['cost']}")
            print(f"ATENÇÃO: Resultado pode estar INCORRETO com pesos negativos!")
    except Exception as e:
        print(f"Falhou: {str(e)}")

def main():
    print("Algoritmo de Bellman-Ford - Roteamento com Pesos Negativos")
    
    print_algorithm_info()
    
    demonstrate_negative_weights()

if __name__ == "__main__":
    main()
