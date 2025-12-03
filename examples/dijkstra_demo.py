from app.algorithms import DijkstraRouter, BFSRouter, format_dijkstra_result, format_dijkstra_routing_table, format_bfs_result
from app.scenarios.dijkstra_scenario import create_dijkstra_network, create_simple_comparison_network

def print_network_info():
    print("Tipos de Links na Rede")
    print("Formula de custo: Custo Dijkstra = 10^8 / largura_de_banda_em_bps\n")
    
    print('Gigabit Ethernet | Banda: 1 Gbps   | Custo: 100    | Uso: Backbone central')
    print('Fast Ethernet    | Banda: 100 Mbps | Custo: 1000   | Uso: Camada de distribuicao')
    print('T1 WAN           | Banda: 1.5 Mbps | Custo: 64000  | Uso: Escritorios remotos')
    print('Satellite Backup | Banda: 256 Kbps | Custo: 200000 | Uso: Backup emergencial')

def compare_bfs_vs_dijkstra(network, source, dest, description):
    print(f"Cenario: {description}")
    print(f"Rota: {source} -> {dest}\n")
    
    bfs_router = BFSRouter()
    dijkstra_router = DijkstraRouter()
    
    bfs_result = bfs_router.find_shortest_path(network, source, dest)
    
    dijkstra_result = dijkstra_router.find_shortest_path(network, source, dest)
    
    if bfs_result and dijkstra_result:
        bfs_path = " -> ".join(bfs_result['path'])
        dijkstra_path = " -> ".join(dijkstra_result['path'])
        
        print(f"BFS (Menor numero de saltos):")
        print(f"Caminho: {bfs_path}")
        print(f"Saltos: {bfs_result['saltos']}\n")
        
        print(f"Dijkstra (Menor custo):")
        print(f"Caminho: {dijkstra_path}")
        print(f"Custo: {dijkstra_result['cost']}")
        print(f"Saltos: {dijkstra_result['saltos']}\n")
    
        if bfs_result['path'] != dijkstra_result['path']:
            print(f"ALGORITMOS ESCOLHERAM CAMINHOS DIFERENTES!")
            print(f"- BFS priorizou: MENOS SALTOS ({bfs_result['saltos']} saltos)")
            print(f"- Dijkstra priorizou: MENOR CUSTO (custo {dijkstra_result['cost']})")
            print(f"- Dijkstra e mais eficiente em redes com links de custos variados")
        else:
            print(f"Ambos os algoritmos escolheram o mesmo caminho")
            print(f"(Neste caso, o caminho de menor custo também tem menos saltos)")
    elif bfs_result:
        print(format_bfs_result(bfs_result, source, dest))
    elif dijkstra_result:
        print(format_dijkstra_result(dijkstra_result, source, dest))
    else:
        print(f"Nao ha caminho entre {source} e {dest}\n")
    
    print("---------------------------------------------------------------")


def demonstrate_simple_comparison():
    print("DEMONSTRACAO: POR QUE DIJKSTRA E MELHOR?")
    
    print("Rede simplificada:")
    print("""
          A ----10---- B
          |            |
         100          10
          |            |
          C ----10---- D
    """)
    
    network = create_simple_comparison_network()
    source = "A"
    dest = "D"
    desc = "Demonstracao: BFS escolhe menos saltos, Dijkstra escolhe menor custo"
    
    compare_bfs_vs_dijkstra(network, source, dest, desc)
    
    print("Conclusao:")
    print("- BFS encontra o caminho com MENOS SALTOS (mas pode ter custo maior)")
    print("- Dijkstra encontra o caminho com MENOR CUSTO (mais eficiente)")
    print("- Em redes reais, considerar custos leva a melhores decisoes de roteamento!\n")

def main():
    print("Algoritmo de Dijkstra - Encontrando Caminhos de Menor Custo")
    print("Comparacao com BFS (menor numero de saltos)")
    
    print_network_info()
    
    demonstrate_simple_comparison()
    
    print("REDE DE 16 VERTICES")
    
    network = create_dijkstra_network()
    print("Rede criada com 16 vertices!")
    print("- 3 roteadores Core (links Gigabit - custo baixo)")
    print("- 4 roteadores Distribution (Fast Ethernet - custo medio)")
    print("- 4 escritorios remotos (WAN T1 - custo alto)")
    print("- 4 sites de acesso (Fast Ethernet)")
    print("- 1 gateway perimetral")
    print("- Links de backup via satelite (custo muito alto)\n")
    
    print("COMPARACAO: BFS vs Dijkstra")
    
    scenarios = [
        ("Nucleo-A", "Nucleo-C", "Rota dentro do nucleo"),
        ("Nucleo-A", "Escritorio-Remoto1", "Nucleo ate escritorio remoto via WAN"),
        ("Escritorio-Remoto1", "Escritorio-Remoto3", "Entre escritorios remotos"),
        ("Dist-Norte", "Dist-Leste", "Entre roteadores de distribuicao"),
        ("Acesso-Bairro1", "Acesso-Bairro3", "Entre sites de acesso"),
        ("Gateway-Perimetral", "Escritorio-Remoto4", "Gateway perimetral ate remoto"),
    ]
    
    for source, dest, desc in scenarios:
        compare_bfs_vs_dijkstra(network, source, dest, desc)
    
    print("TABELAS DE ROTEAMENTO")
    
    dijkstra_router = DijkstraRouter()
    
    core_router = "Nucleo-A"
    routing_table = dijkstra_router.calculate_routing_table(network, core_router)
    print(format_dijkstra_routing_table(routing_table, core_router))
    
    dist_router = "Dist-Norte"
    routing_table = dijkstra_router.calculate_routing_table(network, dist_router)
    print(format_dijkstra_routing_table(routing_table, dist_router))
    
    remote_router = "Escritorio-Remoto1"
    routing_table = dijkstra_router.calculate_routing_table(network, remote_router)
    print(format_dijkstra_routing_table(routing_table, remote_router))
    
    print("DEMONSTRACAO CONCLUIDA!")
    print("\nPrincipais aprendizados:")
    print("1. Dijkstra encontra o caminho de MENOR CUSTO (nao apenas menor contagem de saltos)")
    print("2. BFS encontra caminhos com menos saltos, mas pode ignorar custos")
    print("3. Em redes com links heterogeneos, Dijkstra toma decisoes mais eficientes")
    print("4. Links de menor custo levam a rotas mais eficientes")


if __name__ == "__main__":
    main()
