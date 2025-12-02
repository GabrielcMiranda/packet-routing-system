class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed
        self._vertices = set()
    
    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = []
    
    def add_edge(self, source, destination, weight=1.0):
        self.add_vertex(source)
        self.add_vertex(destination)
        
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append((destination, weight))
        
        if not self.directed:
            if destination not in self.adjacency_list:
                self.adjacency_list[destination] = []
            self.adjacency_list[destination].append((source, weight))
    
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    def get_vertices(self):
        return self._vertices.copy()
    
    def get_edges(self):
        edges = []
        seen = set()
        
        for source in self.adjacency_list:
            for destination, weight in self.adjacency_list[source]:
                if self.directed:
                    edges.append((source, destination, weight))
                else:
                    edge = tuple(sorted([source, destination])) + (weight,)
                    if edge not in seen:
                        seen.add(edge)
                        edges.append((source, destination, weight))
        
        return edges
    
    def has_vertex(self, vertex):
        return vertex in self._vertices
    
    def has_edge(self, source, destination):
        if source not in self.adjacency_list:
            return False
        return any(dest == destination for dest, _ in self.adjacency_list[source])
    
    def get_weight(self, source, destination):
        if source not in self.adjacency_list:
            return None
        
        for dest, weight in self.adjacency_list[source]:
            if dest == destination:
                return weight
        
        return None
    
    def remove_edge(self, source, destination):
        if source not in self.adjacency_list:
            return False
        
        original_len = len(self.adjacency_list[source])
        self.adjacency_list[source] = [
            (dest, weight) for dest, weight in self.adjacency_list[source]
            if dest != destination
        ]
        removed = len(self.adjacency_list[source]) < original_len
        
        if not self.directed and destination in self.adjacency_list:
            self.adjacency_list[destination] = [
                (dest, weight) for dest, weight in self.adjacency_list[destination]
                if dest != source
            ]
        
        return removed
    
    def vertex_count(self):
        return len(self._vertices)
    
    def edge_count(self):
        return len(self.get_edges())
    
    def __str__(self):
        result = []
        result.append(f"Grafo {'Direcionado' if self.directed else 'Não-Direcionado'}")
        result.append(f"Vértices: {self.vertex_count()}, Arestas: {self.edge_count()}")
        result.append("\nLista de Adjacências:")
        
        for vertex in sorted(self._vertices):
            neighbors = self.adjacency_list[vertex]
            if neighbors:
                neighbor_str = ", ".join([f"{dest}({weight})" for dest, weight in neighbors])
                result.append(f"  {vertex} -> {neighbor_str}")
            else:
                result.append(f"  {vertex} -> []")
        
        return "\n".join(result)
