from app.algorithms import BellmanFordRouter, DijkstraRouter, format_bellman_ford_result, format_bellman_ford_routing_table
from app.scenarios.bellman_ford_scenario import create_network_with_negative_weights, create_distributed_network, create_network_with_penalty_links, create_negative_cycle_network

def print_algorithm_info():
    print("Características do Algoritmo Bellman-Ford")
    print("=========================================")
    
    print('Pesos Negativos        -> SIM     | Suporta links com custos negativos')
    print('Ciclos Negativos       -> DETECTA | Identifica loops infinitos')
    print('Roteamento Distribuído -> SIM     | Modelo usado no RIP')
    print('Complexidade           -> O(V*E)  | Mais lento que Dijkstra')
    
    print("\nCasos de Uso:")
    print('1. Protocolo RIP (Routing Information Protocol)')
    print('2. Redes com links assimétricos')
    print('3. Detecção de arbitragem em sistemas financeiros')
    print('4. Cenários onde links podem ter "descontos" ou penalidades')

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
    
    print("Observação:")
    print("- Bellman-Ford encontrou a rota com caches (peso negativo)")
    print("- Iterações mostram o processo de convergência distribuída")
    print("- Dijkstra NÃO suporta pesos negativos!\n")

def demonstrate_distributed_routing():
    print("ROTEAMENTO DISTRIBUÍDO - SIMULAÇÃO RIP")
    
    network = create_distributed_network()
    
    print("Rede mesh com 6 roteadores (R1 a R6)")
    print("Simulação: Cada roteador troca informações com vizinhos\n")
    
    source, dest = "R1", "R6"
    
    bf_router = BellmanFordRouter()
    bf_result = bf_router.find_shortest_path(network, source, dest)
    print(format_bellman_ford_result(bf_result, source, dest))
    
    print("Tabela de Roteamento Completa:")
    routing_table = bf_router.calculate_routing_table(network, source)
    print(format_bellman_ford_routing_table(routing_table, source))

def demonstrate_penalty_links():
    print("LINKS COM PENALIDADES E BENEFÍCIOS")
    
    print("Cenário: Data centers com diferentes qualidades de link")
    print("- Backbone padrão: 50 + 50 = 100")
    print("- Link direto congestionado: 120")
    print("- Link com compressão: 30 + (-10) + 30 = 50")
    print("- Link premium com QoS: 40 + (-20) = 20 (melhor!)\n")
    
    network = create_network_with_penalty_links()
    source, dest = "DC1", "DC3"
    
    bf_router = BellmanFordRouter()
    bf_result = bf_router.find_shortest_path(network, source, dest)
    print(format_bellman_ford_result(bf_result, source, dest))
    
    print("Interpretação:")
    print("- Pesos negativos representam 'descontos' ou 'benefícios'")
    print("- QoS garantido = custo efetivo menor")
    print("- Compressão = economia de recursos = custo negativo\n")

def demonstrate_negative_cycle_detection():
    print("DETECÇÃO DE CICLOS NEGATIVOS")
    
    network = create_negative_cycle_network()
    
    print("Rede com CICLO NEGATIVO detectado!")
    print("- Ciclo: B -> E -> F -> B (custo: 2 + 3 + (-10) = -5)")
    print("- Problema: Passar pelo ciclo reduz custo infinitamente\n")
    
    bf_router = BellmanFordRouter()
    cycle_info = bf_router.detect_negative_cycle(network)
    
    if cycle_info['has_negative_cycle']:
        print("CICLO NEGATIVO DETECTADO!")
        if cycle_info['cycle']:
            cycle_str = " -> ".join(cycle_info['cycle'])
            print(f"   Ciclo encontrado: {cycle_str}")
        print("\nSignificado:")
        print("- Configuração inválida na rede")
        print("- Possível loop de roteamento")
        print("- Bellman-Ford detecta e previne uso\n")
    else:
        print("Nenhum ciclo negativo detectado\n")

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
    print("Suporte a custos negativos e detecção de ciclos")
    
    print_algorithm_info()
    
    demonstrate_negative_weights()
    
    demonstrate_distributed_routing()
    
    demonstrate_penalty_links()
    
    demonstrate_negative_cycle_detection()
    
    compare_with_dijkstra()
    
    print()
    print("DEMONSTRAÇÃO CONCLUÍDA!")
    print("\nPrincipais aprendizados:")
    print("1. Bellman-Ford suporta PESOS NEGATIVOS (Dijkstra não)")
    print("2. Detecta CICLOS NEGATIVOS (loops infinitos)")
    print("3. Simula roteamento DISTRIBUÍDO iterativo (protocolo RIP)")
    print("4. Complexidade O(V*E) - mais lento que Dijkstra, mas mais versátil")
    print("5. Ideal para cenários com 'descontos', 'penalidades' ou assimetria")

if __name__ == "__main__":
    main()
