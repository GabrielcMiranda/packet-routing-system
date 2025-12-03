
from app.algorithms import BFSRouter, format_bfs_result, format_routing_table
from app.scenarios.bfs_scenario import create_metropolitan_network

def main():

    print("BFS aplicado ao Protocolo RIP - Rede Metropolitana")
    print("="*80 + "\n")
 
    network = create_metropolitan_network()
    print(f"Rede criada: {len(network.get_vertices())} roteadores\n")
    
    router = BFSRouter()
    
    print("║" + " "*20 + "TESTE 1: ROTA ENTRE EXTREMOS (BFS)" + " "*23 + "║")
    
    print("   Cenário: Cliente de um extremo a outro da cidade")
    print("   Demonstra BFS encontrando o caminho com MENOR número de hops")
    print("   atravessando múltiplas camadas (Access → Dist → Core → Dist → Access)\n")
    
    result = router.find_shortest_path(network, "Access-Bairro1", "Access-Bairro4")
    print(format_bfs_result(result, "Access-Bairro1", "Access-Bairro4"))
    
    print("\n\n")
    print("   TESTE 2: TABELA DE ROTEAMENTO COMPLETA (RIP)")
    print("\n")
    
    print("   Aplicação prática: Protocolo RIP gerando tabela de roteamento")
    print("   com menor número de hops para TODOS os destinos alcançáveis.\n")
    
    core_router = "Core-Central"
    routing_table = router.find_all_paths_from_source(network, core_router)
    print(format_routing_table(routing_table, core_router))
    
    print("\n" + "="*80)
    print("Demonstração concluída! Consulte docs/BFS_teoria_e_cenario.md")
    print("="*80)

if __name__ == "__main__":
    main()
