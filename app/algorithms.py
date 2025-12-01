
from collections import deque
from typing import Dict, List, Optional, Tuple, Set
from app.graph import Graph

def bfs_shortest_path(graph: Graph, source: str, destination: str) -> Optional[Dict]:
   
    if not graph.has_vertex(source) or not graph.has_vertex(destination):
        return None
    
    if source == destination:
        return {
            'path': [source],
            'distance': 0,
            'visited_order': [source]
        }
    
    queue = deque([(source, [source])]) 
    visited = {source}
    visited_order = [source]
    
    while queue:
        current, path = queue.popleft()
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                visited_order.append(neighbor)
                new_path = path + [neighbor]
                
                if neighbor == destination:
                    return {
                        'path': new_path,
                        'distance': len(new_path) - 1,
                        'visited_order': visited_order
                    }
    
                queue.append((neighbor, new_path))
    
    return None


def bfs_all_paths(graph: Graph, source: str) -> Dict[str, Dict]:
    
    if not graph.has_vertex(source):
        return {}
    
    paths = {}
    queue = deque([(source, [source])])
    visited = {source}
    
    while queue:
        current, path = queue.popleft()
        
        if current != source:
            paths[current] = {
                'path': path,
                'distance': len(path) - 1,
                'parent': path[-2] if len(path) > 1 else None
            }
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return paths


def bfs_reachable(graph: Graph, source: str) -> Set[str]:
   
    if not graph.has_vertex(source):
        return set()
    
    queue = deque([source])
    reachable = {source}
    
    while queue:
        current = queue.popleft()
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    
    return reachable


def bfs_unreachable(graph: Graph, source: str) -> Set[str]:
   
    reachable = bfs_reachable(graph, source)
    all_vertices = graph.get_vertices()
    return all_vertices - reachable

class BFSRouter:
    
    @staticmethod
    def find_shortest_path(graph: Graph, source: str, destination: str) -> Optional[Dict]:
        
        result = bfs_shortest_path(graph, source, destination)
        
        if result is None:
            return None
        
        return {
            'path': result['path'],
            'hops': result['distance'],
            'visited_order': result['visited_order']
        }
    
    @staticmethod
    def find_all_paths_from_source(graph: Graph, source: str) -> Dict[str, Dict]:
        
        paths = bfs_all_paths(graph, source)
        
        routing_table = {}
        for destination, info in paths.items():
            routing_table[destination] = {
                'path': info['path'],
                'hops': info['distance'],
                'next_hop': info['path'][1] if len(info['path']) > 1 else destination
            }
        
        return routing_table
    
    @staticmethod
    def detect_unreachable_nodes(graph: Graph, source: str) -> List[str]:
        
        unreachable = bfs_unreachable(graph, source)
        return sorted(list(unreachable))


# ============================================================================
# ALGORITMO DFS (Depth-First Search) - IMPLEMENTAÇÃO PURA
# ============================================================================

def dfs_path(graph: Graph, source: str, destination: str) -> Optional[Dict]:
   
    if not graph.has_vertex(source) or not graph.has_vertex(destination):
        return None
    
    if source == destination:
        return {
            'path': [source],
            'visited_order': [source]
        }
    
    visited = set()
    visited_order = []
    path = []
    
    def dfs_recursive(current: str) -> bool:

        visited.add(current)
        visited_order.append(current)
        path.append(current)
        
        if current == destination:
            return True
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                if dfs_recursive(neighbor):
                    return True
        
        path.pop()
        return False
    
    if dfs_recursive(source):
        return {
            'path': path,
            'visited_order': visited_order
        }
    
    return None


def dfs_traverse(graph: Graph, source: str) -> Dict[str, any]:
 
    if not graph.has_vertex(source):
        return {
            'visited_order': [],
            'discovery_time': {},
            'finish_time': {},
            'predecessors': {}
        }
    
    visited = set()
    visited_order = []
    discovery_time = {}
    finish_time = {}
    predecessors = {}
    time = [0]  
    
    def dfs_visit(vertex: str, parent: Optional[str] = None):
        
        visited.add(vertex)
        visited_order.append(vertex)
        time[0] += 1
        discovery_time[vertex] = time[0]
        predecessors[vertex] = parent
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_visit(neighbor, vertex)
        
        time[0] += 1
        finish_time[vertex] = time[0]
    
    dfs_visit(source)
    
    return {
        'visited_order': visited_order,
        'discovery_time': discovery_time,
        'finish_time': finish_time,
        'predecessors': predecessors
    }


def dfs_detect_cycles(graph: Graph) -> Dict[str, any]:
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph.get_vertices()}
    parent = {}
    cycles = []
    
    def dfs_visit(vertex: str):
        
        color[vertex] = GRAY
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if color[neighbor] == WHITE:
                parent[neighbor] = vertex
                dfs_visit(neighbor)
            elif color[neighbor] == GRAY:
                cycles.append((vertex, neighbor))
        
        color[vertex] = BLACK
    
    for vertex in graph.get_vertices():
        if color[vertex] == WHITE:
            parent[vertex] = None
            dfs_visit(vertex)
    
    return {
        'has_cycle': len(cycles) > 0,
        'cycles': cycles
    }


def dfs_connected_components(graph: Graph) -> List[Set[str]]:
    
    visited = set()
    components = []
    
    def dfs_component(vertex: str, component: Set[str]):
        
        visited.add(vertex)
        component.add(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_component(neighbor, component)
    
    for vertex in graph.get_vertices():
        if vertex not in visited:
            component = set()
            dfs_component(vertex, component)
            components.append(component)
    
    return components


class DFSNetworkDiscovery:
    
    @staticmethod
    def discover_topology(graph: Graph, source: str) -> Dict[str, any]:
        
        result = dfs_traverse(graph, source)
        
        return {
            'discovery_order': result['visited_order'],
            'discovery_time': result['discovery_time'],
            'finish_time': result['finish_time'],
            'topology_tree': result['predecessors']
        }
    
    @staticmethod
    def detect_loops(graph: Graph) -> Dict[str, any]:
        
        result = dfs_detect_cycles(graph)
        
        return {
            'has_loops': result['has_cycle'],
            'loop_links': result['cycles']
        }
    
    @staticmethod
    def find_network_segments(graph: Graph) -> List[Set[str]]:
       
        components = dfs_connected_components(graph)
        return components


def format_bfs_result(result: Optional[Dict], source: str, destination: str) -> str:
   
    if result is None:
        return f"\n❌ Não há caminho de {source} para {destination}\n"
    
    path_str = " -> ".join(result['path'])
    output = []
    output.append(f"\n✅ Rota encontrada (BFS - Menor número de hops):")
    output.append(f"   Origem: {source}")
    output.append(f"   Destino: {destination}")
    output.append(f"   Caminho: {path_str}")
    output.append(f"   Número de hops: {result['hops']}")
    output.append(f"   Nós explorados: {' -> '.join(result['visited_order'])}")
    
    return "\n".join(output) + "\n"


def format_routing_table(routing_table: Dict[str, Dict], source: str) -> str:
    
    if not routing_table:
        return f"\n📋 Tabela de Roteamento de {source}: Vazia\n"
    
    output = []
    output.append(f"\n📋 Tabela de Roteamento RIP - Roteador {source}")
    output.append("=" * 70)
    output.append(f"{'Destino':<15} {'Hops':<8} {'Próximo Salto':<20} {'Caminho Completo'}")
    output.append("-" * 70)
    
    sorted_table = sorted(routing_table.items(), key=lambda x: (x[1]['hops'], x[0]))
    
    for destination, info in sorted_table:
        path_str = " -> ".join(info['path'])
        output.append(f"{destination:<15} {info['hops']:<8} {info['next_hop']:<20} {path_str}")
    
    output.append("=" * 70)
    
    return "\n".join(output) + "\n"
