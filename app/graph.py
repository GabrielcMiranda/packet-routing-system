from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict


class Graph:
    """
    Grafo representado por lista de adjacências com pesos.
    Cada vértice (roteador) mapeia para uma lista de tuplas (vizinho, peso).
    """
    
    def __init__(self, directed: bool = False):
        """
        Inicializa o grafo.
        
        Args:
            directed: Se True, cria grafo direcionado; se False, não-direcionado
        """
        self.adjacency_list: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        self.directed = directed
        self._vertices: Set[str] = set()
    
    def add_vertex(self, vertex: str) -> None:
        """
        Adiciona um vértice (roteador) ao grafo.
        
        Args:
            vertex: Nome do vértice/roteador
        """
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = []
    
    def add_edge(self, source: str, destination: str, weight: float = 1.0) -> None:
        """
        Adiciona uma aresta (link) entre dois roteadores.
        
        Args:
            source: Roteador de origem
            destination: Roteador de destino
            weight: Peso da aresta (latência, custo, etc.)
        """
        # Adiciona os vértices se não existirem
        self.add_vertex(source)
        self.add_vertex(destination)
        
        # Adiciona a aresta
        self.adjacency_list[source].append((destination, weight))
        
        # Se não-direcionado, adiciona aresta reversa
        if not self.directed:
            self.adjacency_list[destination].append((source, weight))
    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """
        Retorna os vizinhos de um vértice com seus respectivos pesos.
        
        Args:
            vertex: Nome do vértice
            
        Returns:
            Lista de tuplas (vizinho, peso)
        """
        return self.adjacency_list.get(vertex, [])
    
    def get_vertices(self) -> Set[str]:
        """
        Retorna o conjunto de todos os vértices do grafo.
        
        Returns:
            Conjunto com nomes dos vértices
        """
        return self._vertices.copy()
    
    def get_edges(self) -> List[Tuple[str, str, float]]:
        """
        Retorna todas as arestas do grafo.
        
        Returns:
            Lista de tuplas (origem, destino, peso)
        """
        edges = []
        seen = set()
        
        for source in self.adjacency_list:
            for destination, weight in self.adjacency_list[source]:
                if self.directed:
                    edges.append((source, destination, weight))
                else:
                    # Para grafos não-direcionados, evita duplicatas
                    edge = tuple(sorted([source, destination])) + (weight,)
                    if edge not in seen:
                        seen.add(edge)
                        edges.append((source, destination, weight))
        
        return edges
    
    def has_vertex(self, vertex: str) -> bool:
        """
        Verifica se um vértice existe no grafo.
        
        Args:
            vertex: Nome do vértice
            
        Returns:
            True se o vértice existe, False caso contrário
        """
        return vertex in self._vertices
    
    def has_edge(self, source: str, destination: str) -> bool:
        """
        Verifica se existe uma aresta entre dois vértices.
        
        Args:
            source: Vértice de origem
            destination: Vértice de destino
            
        Returns:
            True se a aresta existe, False caso contrário
        """
        if source not in self.adjacency_list:
            return False
        return any(dest == destination for dest, _ in self.adjacency_list[source])
    
    def get_weight(self, source: str, destination: str) -> Optional[float]:
        """
        Retorna o peso de uma aresta específica.
        
        Args:
            source: Vértice de origem
            destination: Vértice de destino
            
        Returns:
            Peso da aresta ou None se a aresta não existe
        """
        if source not in self.adjacency_list:
            return None
        
        for dest, weight in self.adjacency_list[source]:
            if dest == destination:
                return weight
        
        return None
    
    def remove_edge(self, source: str, destination: str) -> bool:
        """
        Remove uma aresta do grafo.
        
        Args:
            source: Vértice de origem
            destination: Vértice de destino
            
        Returns:
            True se a aresta foi removida, False se não existia
        """
        if source not in self.adjacency_list:
            return False
        
        # Remove a aresta na direção source -> destination
        original_len = len(self.adjacency_list[source])
        self.adjacency_list[source] = [
            (dest, weight) for dest, weight in self.adjacency_list[source]
            if dest != destination
        ]
        removed = len(self.adjacency_list[source]) < original_len
        
        # Se não-direcionado, remove também a aresta reversa
        if not self.directed and destination in self.adjacency_list:
            self.adjacency_list[destination] = [
                (dest, weight) for dest, weight in self.adjacency_list[destination]
                if dest != source
            ]
        
        return removed
    
    def vertex_count(self) -> int:
        """Retorna o número de vértices no grafo."""
        return len(self._vertices)
    
    def edge_count(self) -> int:
        """Retorna o número de arestas no grafo."""
        return len(self.get_edges())
    
    def __str__(self) -> str:
        """Representação em string do grafo."""
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
