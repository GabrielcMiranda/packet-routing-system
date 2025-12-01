from app.algorithms import DFSNetworkDiscovery
from app.scenarios.dfs_scenario import (
    create_corporate_network,
    create_network_with_failures,
    create_network_with_loop
)


def print_section(title: str):

    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def print_discovery_result(result: dict, source: str):

    print(f"🔍 Descoberta iniciada de: {source}\n")
    
    print(f"📊 Dispositivos descobertos: {len(result['discovery_order'])}")
    print(f"   Ordem: {' → '.join(result['discovery_order'])}\n")
    
    print("🌳 Árvore de Descoberta (hierarquia parent-child):")
    for device, parent in result['topology_tree'].items():
        if parent:
            print(f"   {parent} ──> {device}")
        else:
            print(f"   {device} (raiz)")


def print_loop_detection(result: dict, network_name: str):
  
    print(f"🔄 Análise de Loops - {network_name}\n")
    
    if result['has_loops']:
        print(f"⚠️  LOOPS DETECTADOS: {len(result['loop_links'])} back edge(s)")
        print("   Links formando ciclos:")
        for src, dst in result['loop_links']:
            print(f"      • {src} ──> {dst}")
        print("\n💡 Spanning Tree Protocol (STP) deve desabilitar estas portas")
    else:
        print("✅ Nenhum loop detectado - topologia livre de ciclos")


def print_segments(segments: list):
   
    print(f"🗺️  Segmentos de rede identificados: {len(segments)}\n")
    
    for i, segment in enumerate(segments, 1):
        print(f"Segmento {i} ({len(segment)} dispositivos):")
        print(f"   {', '.join(sorted(segment))}")
        print()
    
    if len(segments) > 1:
        print("⚠️  ATENÇÃO: Rede segmentada - múltiplos componentes isolados!")
        print("   Possível falha de link WAN ou partição de rede")
    else:
        print("✅ Rede totalmente conectada - um único componente")


def demo_topology_discovery():
   
    print_section("Demo 1: Descoberta de Topologia Corporativa")
    
    network = create_corporate_network()
    print(f"🏢 Rede: Corporação distribuída com {len(network.get_vertices())} dispositivos")
    print("   • Headquarters (6 dispositivos)")
    print("   • Data Center (2 dispositivos)")
    print("   • Branch Office 1 (5 dispositivos)")
    print("   • Branch Office 2 (5 dispositivos)\n")
    
    result = DFSNetworkDiscovery.discover_topology(network, "HQ-Core-SW1")
    print_discovery_result(result, "HQ-Core-SW1")


def demo_loop_detection():
 
    print_section("Demo 2: Detecção de Loops (Spanning Tree)")
    
    print("📡 Rede Corporativa (com redundância):")
    corporate = create_corporate_network()
    result1 = DFSNetworkDiscovery.detect_loops(corporate)
    print_loop_detection(result1, "Rede Corporativa")
    
    print("\n" + "-"*70 + "\n")
 
    print("📡 Rede de Teste (loop intencional):")
    loop_net = create_network_with_loop()
    result2 = DFSNetworkDiscovery.detect_loops(loop_net)
    print_loop_detection(result2, "Rede de Teste")


def demo_segment_identification():
 
    print_section("Demo 3: Identificação de Segmentos Isolados")
 
    print("📡 Rede Corporativa Normal:\n")
    normal = create_corporate_network()
    segments1 = DFSNetworkDiscovery.find_network_segments(normal)
    print_segments(segments1)
    
    print("\n" + "-"*70 + "\n")

    print("📡 Rede com Falhas de WAN:\n")
    failed = create_network_with_failures()
    segments2 = DFSNetworkDiscovery.find_network_segments(failed)
    print_segments(segments2)


def demo_branch_discovery():
 
    print_section("Demo 4: Descoberta a partir de Filial")
    
    network = create_corporate_network()
    
  
    result = DFSNetworkDiscovery.discover_topology(network, "Branch1-Router")
    print_discovery_result(result, "Branch1-Router")
    
    print("\n💡 Observação: DFS explora em profundidade, seguindo um caminho até o fim")
    print("   antes de retroceder. A ordem depende dos vizinhos de cada dispositivo.")


def demo_connectivity_analysis():
  
    print_section("Demo 5: Análise de Conectividade")
    
    network = create_corporate_network()
    
    print("🔍 Verificando conectividade do HQ para outros sites:\n")
    
    sites = [
        ("DC-Core-SW1", "Data Center"),
        ("Branch1-Router", "Filial 1"),
        ("Branch2-Router", "Filial 2")
    ]
    
    result = DFSNetworkDiscovery.discover_topology(network, "HQ-Core-SW1")
    reachable = result['discovery_order']
    
    for device, site_name in sites:
        if device in reachable:
            print(f"✅ {site_name:20} → ALCANÇÁVEL")
        else:
            print(f"❌ {site_name:20} → ISOLADO")
    
    print(f"\n📊 Total alcançável do HQ: {len(reachable)}/{len(network.get_vertices())} dispositivos")


def main():
    print("\n" + "🚀 "*30)
    print("   DFS - DESCOBERTA DE TOPOLOGIA EM REDES")
    print("🚀 "*30)
    
    demo_topology_discovery()
    demo_loop_detection()
    demo_segment_identification()
    demo_branch_discovery()
    demo_connectivity_analysis()
    
    print("\n" + "="*70)
    print("  ✅ Demonstração Completa!")
    print("="*70)
    print("\n💡 Conceitos demonstrados:")
    print("   • Descoberta de topologia (LLDP/CDP)")
    print("   • Detecção de loops (Spanning Tree Protocol)")
    print("   • Identificação de segmentos isolados")
    print("   • Análise de conectividade\n")


if __name__ == "__main__":
    main()
