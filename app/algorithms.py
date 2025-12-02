from app.graph import Graph

def bfs_shortest_path(graph, source, destination):
   
    if not graph.has_vertex(source) or not graph.has_vertex(destination):
        return None
    
    if source == destination:
        return {
            'path': [source],
            'distance': 0,
            'visited_order': [source]
        }
    
    queue = [(source, [source])]
    visited = {source}
    visited_order = [source]
    
    while queue:
        current, path = queue.pop(0)
        
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


def bfs_all_paths(graph, source):
    
    if not graph.has_vertex(source):
        return {}
    
    paths = {}
    queue = [(source, [source])]
    visited = {source}
    
    while queue:
        current, path = queue.pop(0)
        
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


def bfs_reachable(graph, source):
   
    if not graph.has_vertex(source):
        return set()
    
    queue = [source]
    reachable = {source}
    
    while queue:
        current = queue.pop(0)
        
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    
    return reachable


def bfs_unreachable(graph, source):
   
    reachable = bfs_reachable(graph, source)
    all_vertices = graph.get_vertices()
    return all_vertices - reachable

class BFSRouter:
    
    def find_shortest_path(self, graph, source, destination):
        
        result = bfs_shortest_path(graph, source, destination)
        
        if result is None:
            return None
        
        return {
            'path': result['path'],
            'saltos': result['distance'],
            'visited_order': result['visited_order']
        }
    
    def find_all_paths_from_source(self, graph, source):
        
        paths = bfs_all_paths(graph, source)
        
        routing_table = {}
        for destination, info in paths.items():
            routing_table[destination] = {
                'path': info['path'],
                'saltos': info['distance'],
                'next_hop': info['path'][1] if len(info['path']) > 1 else destination
            }
        
        return routing_table
    
    def detect_unreachable_nodes(self, graph, source):
        
        unreachable = bfs_unreachable(graph, source)
        return sorted(list(unreachable))


# ============================================================================
# ALGORITMO DFS (Depth-First Search) - IMPLEMENTAÇÃO PURA
# ============================================================================

def dfs_path(graph, source, destination):
   
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
    
    def dfs_recursive(current):

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


def dfs_traverse(graph, source):
 
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
    
    def dfs_visit(vertex, parent=None):
        
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


def dfs_detect_cycles(graph):
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph.get_vertices()}
    parent = {}
    cycles = []
    
    def dfs_visit(vertex):
        
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


def dfs_connected_components(graph):
    
    visited = set()
    components = []
    
    def dfs_component(vertex, component):
        
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
    
    def discover_topology(self, graph, source):
        
        result = dfs_traverse(graph, source)
        
        return {
            'discovery_order': result['visited_order'],
            'discovery_time': result['discovery_time'],
            'finish_time': result['finish_time'],
            'topology_tree': result['predecessors']
        }
    
    def detect_loops(self, graph):
        
        result = dfs_detect_cycles(graph)
        
        return {
            'has_loops': result['has_cycle'],
            'loop_links': result['cycles']
        }
    
    def find_network_segments(self, graph):
       
        components = dfs_connected_components(graph)
        return components


def format_bfs_result(result, source, destination):
   
    if result is None:
        return f"\n❌ Não há caminho de {source} para {destination}\n"
    
    path_str = " -> ".join(result['path'])
    output = []
    output.append(f"\n✅ Rota encontrada (BFS - Menor número de saltos):")
    output.append(f"   Origem: {source}")
    output.append(f"   Destino: {destination}")
    output.append(f"   Caminho: {path_str}")
    output.append(f"   Número de saltos: {result['saltos']}")
    output.append(f"   Nós explorados: {' -> '.join(result['visited_order'])}")
    
    return "\n".join(output) + "\n"


def format_routing_table(routing_table, source):
    
    if not routing_table:
        return f"\n📋 Tabela de Roteamento de {source}: Vazia\n"
    
    output = []
    output.append(f"\n📋 Tabela de Roteamento RIP - Roteador {source}")
    output.append("=" * 70)
    output.append(f"{'Destino':<15} {'Saltos':<8} {'Próximo Salto':<20} {'Caminho Completo'}")
    output.append("-" * 70)
    
    sorted_table = sorted(routing_table.items(), key=lambda x: (x[1]['saltos'], x[0]))
    
    for destination, info in sorted_table:
        path_str = " -> ".join(info['path'])
        output.append(f"{destination:<15} {info['saltos']:<8} {info['next_hop']:<20} {path_str}")
    
    output.append("=" * 70)
    
    return "\n".join(output) + "\n"


# ==================
# ALGORITMO DIJKSTRA
# ==================

def dijkstra_shortest_path(graph, source, destination):
    if not graph.has_vertex(source) or not graph.has_vertex(destination):
        return None
    
    if source == destination:
        return {
            'path': [source],
            'cost': 0,
            'visited_order': [source]
        }
    
    vertices = graph.get_vertices()
    distances = {v: float('inf') for v in vertices}
    distances[source] = 0
    predecessors = {source: None}
    visited = set()
    visited_order = []
    unvisited = set(vertices)
    
    while unvisited:
        current = None
        min_distance = float('inf')
        
        for vertex in unvisited:
            if distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current = vertex
        
        if current is None or distances[current] == float('inf'):
            break
        
        unvisited.remove(current)
        visited.add(current)
        visited_order.append(current)
        
        if current == destination:
            path = []
            node = destination
            while node is not None:
                path.insert(0, node)
                node = predecessors.get(node)
            
            return {
                'path': path,
                'cost': distances[destination],
                'visited_order': visited_order
            }
        
        for neighbor, weight in graph.get_neighbors(current):
            if neighbor not in visited:
                new_distance = distances[current] + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current
    
    return None

class DijkstraRouter:
    def find_shortest_path(self, graph, source, destination):
        result = dijkstra_shortest_path(graph, source, destination)
        
        if result is None:
            return None
        
        return {
            'path': result['path'],
            'cost': result['cost'],
            'saltos': len(result['path']) - 1,
            'visited_order': result['visited_order']
        }
    
    def calculate_routing_table(self, graph, source):
        routing_table = {}
        
        for destination in graph.get_vertices():
            if destination == source:
                continue
            
            result = dijkstra_shortest_path(graph, source, destination)
            if result:
                routing_table[destination] = {
                    'path': result['path'],
                    'cost': result['cost'],
                    'saltos': len(result['path']) - 1,
                    'next_hop': result['path'][1] if len(result['path']) > 1 else destination
                }
        
        return routing_table

def format_dijkstra_result(result, source, destination):
    if result is None:
        return f"\nNão há caminho de {source} para {destination}\n"
    
    path_str = " -> ".join(result['path'])
    output = []
    output.append(f"\nRota encontrada (Dijkstra - Menor custo):")
    output.append(f"Origem: {source}")
    output.append(f"Destino: {destination}")
    output.append(f"Caminho: {path_str}")
    output.append(f"Custo total: {result['cost']}")
    output.append(f"Número de saltos: {result['saltos']}")
    output.append(f"Nós explorados: {' -> '.join(result['visited_order'])}")
    
    return "\n".join(output) + "\n"

def format_dijkstra_routing_table(routing_table, source):
    if not routing_table:
        return f"\nTabela de Roteamento de {source}: Vazia\n"
    
    output = []
    output.append(f"\nTabela de Roteamento (Dijkstra) - Origem: {source}")
    output.append("=================================================================")
    output.append(f"{'Destino':<15} {'Custo':<10} {'Saltos':<8} {'Próximo Salto':<20} {'Caminho'}")
    output.append("-----------------------------------------------------------------")
    
    sorted_table = sorted(routing_table.items(), key=lambda x: (x[1]['cost'], x[0]))
    
    for destination, info in sorted_table:
        path_str = " -> ".join(info['path'])
        output.append(f"{destination:<15} {info['cost']:<10} {info['saltos']:<8} {info['next_hop']:<20} {path_str}")
    
    output.append("=================================================================")
    
    return "\n".join(output) + "\n"

# ======================
# ALGORITMO BELLMAN-FORD 
# ======================

def bellman_ford_shortest_path(graph, source, destination):
    if not graph.has_vertex(source) or not graph.has_vertex(destination):
        return None
    
    if source == destination:
        return {
            'path': [source],
            'cost': 0,
            'iterations': 0,
            'has_negative_cycle': False
        }
    
    vertices = graph.get_vertices()
    distances = {v: float('inf') for v in vertices}
    distances[source] = 0
    predecessors = {v: None for v in vertices}
    
    num_vertices = len(vertices)
    iterations_log = []
    
    for iteration in range(num_vertices - 1):
        updated = False
        iteration_updates = []
        
        for vertex in vertices:
            if distances[vertex] != float('inf'):
                for neighbor, weight in graph.get_neighbors(vertex):
                    new_distance = distances[vertex] + weight
                    
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = vertex
                        updated = True
                        iteration_updates.append({
                            'edge': (vertex, neighbor),
                            'new_distance': new_distance
                        })
        
        if iteration_updates:
            iterations_log.append({
                'iteration': iteration + 1,
                'updates': iteration_updates
            })
        
        if not updated:
            break
    
    has_negative_cycle = False
    for vertex in vertices:
        if distances[vertex] != float('inf'):
            for neighbor, weight in graph.get_neighbors(vertex):
                if distances[vertex] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    if distances[destination] == float('inf'):
        return None
    
    path = []
    current = destination
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    
    return {
        'path': path,
        'cost': distances[destination],
        'iterations': len(iterations_log),
        'iterations_log': iterations_log,
        'has_negative_cycle': has_negative_cycle
    }


class BellmanFordRouter:
    def find_shortest_path(self, graph, source, destination):
        result = bellman_ford_shortest_path(graph, source, destination)
        
        if result is None:
            return None
        
        return {
            'path': result['path'],
            'cost': result['cost'],
            'saltos': len(result['path']) - 1,
            'iterations': result['iterations'],
            'has_negative_cycle': result['has_negative_cycle']
        }
    
    def calculate_routing_table(self, graph, source):
        routing_table = {}
        vertices = graph.get_vertices()
        
        distances = {v: float('inf') for v in vertices}
        distances[source] = 0
        predecessors = {v: None for v in vertices}
        
        num_vertices = len(vertices)
        
        for _ in range(num_vertices - 1):
            updated = False
            
            for vertex in vertices:
                if distances[vertex] != float('inf'):
                    for neighbor, weight in graph.get_neighbors(vertex):
                        new_distance = distances[vertex] + weight
                        
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
                            predecessors[neighbor] = vertex
                            updated = True
            
            if not updated:
                break
        
        has_negative_cycle = False
        for vertex in vertices:
            if distances[vertex] != float('inf'):
                for neighbor, weight in graph.get_neighbors(vertex):
                    if distances[vertex] + weight < distances[neighbor]:
                        has_negative_cycle = True
                        break
        
        for destination in vertices:
            if destination == source:
                continue
            
            if distances[destination] != float('inf'):
                path = []
                current = destination
                while current is not None:
                    path.insert(0, current)
                    current = predecessors[current]
                
                routing_table[destination] = {
                    'path': path,
                    'cost': distances[destination],
                    'saltos': len(path) - 1,
                    'next_hop': path[1] if len(path) > 1 else destination
                }
        
        return routing_table
    
    def detect_negative_cycle(self, graph):
        vertices = graph.get_vertices()
        if not vertices:
            return {'has_negative_cycle': False, 'cycle': None}
        
        for source in vertices:
            distances = {v: float('inf') for v in vertices}
            distances[source] = 0
            predecessors = {v: None for v in vertices}
            
            num_vertices = len(vertices)
            for _ in range(num_vertices - 1):
                for vertex in vertices:
                    if distances[vertex] != float('inf'):
                        for neighbor, weight in graph.get_neighbors(vertex):
                            if distances[vertex] + weight < distances[neighbor]:
                                distances[neighbor] = distances[vertex] + weight
                                predecessors[neighbor] = vertex
            
            for vertex in vertices:
                if distances[vertex] != float('inf'):
                    for neighbor, weight in graph.get_neighbors(vertex):
                        if distances[vertex] + weight < distances[neighbor]:
                            cycle_vertex = neighbor
                            
                            for _ in range(num_vertices):
                                cycle_vertex = predecessors[cycle_vertex]
                            
                            cycle = []
                            current = cycle_vertex
                            while True:
                                cycle.append(current)
                                current = predecessors[current]
                                if current == cycle_vertex:
                                    cycle.append(current)
                                    break
                                if len(cycle) > num_vertices:
                                    break
                            
                            cycle.reverse()
                            return {'has_negative_cycle': True, 'cycle': cycle}
        
        return {'has_negative_cycle': False, 'cycle': None}


def format_bellman_ford_result(result, source, destination):
    if result is None:
        return f"\nNão há caminho de {source} para {destination}\n"
    
    path_str = " -> ".join(result['path'])
    output = []
    output.append(f"\nRota encontrada (Bellman-Ford - Menor custo):")
    output.append(f"Origem: {source}")
    output.append(f"Destino: {destination}")
    output.append(f"Caminho: {path_str}")
    output.append(f"Custo total: {result['cost']}")
    output.append(f"Número de saltos: {result['saltos']}")
    output.append(f"Iterações necessárias: {result['iterations']}")
    
    if result['has_negative_cycle']:
        output.append(f"AVISO: Ciclo negativo detectado no grafo!")
    
    return "\n".join(output) + "\n"

def format_bellman_ford_routing_table(routing_table, source):
    if not routing_table:
        return f"\nTabela de Roteamento de {source}: Vazia\n"
    
    output = []
    output.append(f"\nTabela de Roteamento (Bellman-Ford) - Origem: {source}")
    output.append("=================================================================")
    output.append(f"{'Destino':<15} {'Custo':<10} {'Saltos':<8} {'Próximo Salto':<20} {'Caminho'}")
    output.append("-----------------------------------------------------------------")
    
    sorted_table = sorted(routing_table.items(), key=lambda x: (x[1]['cost'], x[0]))
    
    for destination, info in sorted_table:
        path_str = " -> ".join(info['path'])
        output.append(f"{destination:<15} {info['cost']:<10} {info['saltos']:<8} {info['next_hop']:<20} {path_str}")
    
    output.append("=================================================================")
    
    return "\n".join(output) + "\n"
