
from app.algorithms import BFSRouter, format_bfs_result, format_routing_table
from app.scenarios.bfs_scenario import create_metropolitan_network, get_test_scenarios


def main():
   
    print("=" * 80)
    print("BFS aplicado ao Protocolo RIP - Rede Metropolitana")
    print("Consulte docs/BFS_teoria_e_cenario.md para teoria completa")
    print("=" * 80 + "\n")
 
    network = create_metropolitan_network()
    print("✅ Rede criada!\n")
    
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "TESTE 1: ROTAS ESPECÍFICAS (BFS)" + " " * 27 + "║")
    print("╚" + "=" * 78 + "╝\n")
    
    scenarios = get_test_scenarios()
    
    for i, (source, destination, description) in enumerate(scenarios, 1):
        print(f"📍 Cenário {i}: {description}")
        result = BFSRouter.find_shortest_path(network, source, destination)
        print(format_bfs_result(result, source, destination))
    
    print("\n" + "╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "TESTE 2: TABELA DE ROTEAMENTO COMPLETA (RIP)" + " " * 18 + "║")
    print("╚" + "=" * 78 + "╝\n")
    
    core_router = "Core-Central"
    routing_table = BFSRouter.find_all_paths_from_source(network, core_router)
    print(format_routing_table(routing_table, core_router))
    
    access_router = "Access-Bairro1"
    routing_table = BFSRouter.find_all_paths_from_source(network, access_router)
    print(format_routing_table(routing_table, access_router))
    
    print("\n" + "╔" + "=" * 78 + "╗")
    print("║" + " " * 18 + "TESTE 3: DETECÇÃO DE FALHAS NA REDE" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝\n")
    
    test_router = "Core-Norte"
    unreachable = BFSRouter.detect_unreachable_nodes(network, test_router)
    
    if unreachable:
        print(f"⚠️  Roteadores inalcançáveis a partir de {test_router}:")
        for node in unreachable:
            print(f"   • {node}")
    else:
        print(f"✅ Todos os roteadores são alcançáveis a partir de {test_router}")
    
    print("\n" + "=" * 80)
    print("✅ Demonstração concluída! Consulte docs/BFS_teoria_e_cenario.md")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
