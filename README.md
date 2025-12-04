# Packet Routing System

Sistema de roteamento de pacotes implementando algoritmos de busca e caminhamento em grafos aplicados ao contexto de redes de computadores.

## 📚 Algoritmos Implementados

### ✅ BFS (Breadth-First Search)
- **Contexto**: Protocolo RIP (Routing Information Protocol)
- **Objetivo**: Encontrar rota com menor número de saltos (hops)
- **Cenário**: Rede metropolitana de ISP com 16 roteadores
- **Documentação**: [`docs/BFS_teoria_e_cenario.md`](docs/BFS_teoria_e_cenario.md)
- **Execução**: `python -m examples.bfs_demo`

### ✅ DFS (Depth-First Search)
- **Contexto**: Descoberta de topologia (LLDP/CDP) e Spanning Tree Protocol
- **Objetivo**: Mapear topologia completa da rede
- **Cenário**: Rede corporativa distribuída com 18 dispositivos em múltiplos sites
- **Documentação**: [`docs/DFS_teoria_e_cenario.md`](docs/DFS_teoria_e_cenario.md)
- **Execução**: `python -m examples.dfs_demo`

### ✅ Dijkstra (Shortest Path)
- **Contexto**: Protocolo OSPF (Open Shortest Path First)
- **Objetivo**: Encontrar rota com menor custo (considera pesos/latências)
- **Cenário**: Rede corporativa com links heterogêneos (Gigabit, Fast Ethernet, T1 WAN)
- **Documentação**: [`docs/Dijkstra_teoria_e_cenario.md`](docs/Dijkstra_teoria_e_cenario.md)
- **Execução**: `python -m examples.dijkstra_demo`

### ✅ Bellman-Ford (Distance Vector)
- **Contexto**: Roteamento distribuído com suporte a pesos negativos
- **Objetivo**: Encontrar menor custo e detectar ciclos negativos
- **Cenário**: Redes com links assimétricos, caches e penalidades
- **Documentação**: [`docs/BellmanFord_teoria_e_cenario.md`](docs/BellmanFord_teoria_e_cenario.md)
- **Execução**: `python -m examples.bellman_ford_demo`

## 🚀 Como usar

### Instalação

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar dependências (se houver)
# pip install -r requirements.txt
```

### Executar demonstrações

```powershell
# BFS - Protocolo RIP (menor número de hops)
python -m examples.bfs_demo

# DFS - Descoberta de topologia LLDP/CDP
python -m examples.dfs_demo

# Dijkstra - Protocolo OSPF (menor custo)
python -m examples.dijkstra_demo

# Bellman-Ford - Roteamento com pesos negativos
python -m examples.bellman_ford_demo

packet-routing-system/
├── app/
│   ├── graph.py              # Estrutura do grafo (lista de adjacências)
│   ├── algorithms.py         # Implementação dos 4 algoritmos
│   └── scenarios/            # Cenários de teste para cada algoritmo
│       ├── bfs_scenario.py           # Rede metropolitana (16 roteadores)
│       ├── dfs_scenario.py           # Rede corporativa (18 dispositivos)
│       ├── dijkstra_scenario.py      # Redes com custos variados
│       └── bellman_ford_scenario.py  # Redes com pesos negativos
├── examples/
│   ├── bfs_demo.py           # Demo BFS: Protocolo RIP
│   ├── dfs_demo.py           # Demo DFS: Descoberta de topologia
│   ├── dijkstra_demo.py      # Demo Dijkstra: Protocolo OSPF
│   └── bellman_ford_demo.py  # Demo Bellman-Ford: Pesos negativos
├── docs/
│   ├── BFS_teoria_e_cenario.md         # Teoria BFS e RIP
│   ├── DFS_teoria_e_cenario.md         # Teoria DFS e LLDP/CDP
│   ├── Dijkstra_teoria_e_cenario.md    # Teoria Dijkstra e OSPF
│   └── BellmanFord_teoria_e_cenario.md # Teoria Bellman-Ford
└── README.md
```

## 🎯 Filosofia do Projeto

**Algoritmos genéricos resolvendo problemas específicos de redes!**

- Implementamos 4 algoritmos clássicos de grafos
- Aplicamos a contextos reais de roteamento de pacotes
- Demonstramos como cada algoritmo resolve problemas diferentes:
  - **BFS**: Menor número de saltos (RIP)
  - **DFS**: Descoberta de topologia (LLDP/CDP)
  - **Dijkstra**: Menor custo considerando pesos (OSPF)
  - **Bellman-Ford**: Suporte a pesos negativos e detecção de ciclos

## 📊 Comparação dos Algoritmos

| Algoritmo | Métrica | Pesos | Ciclos Negativos | Protocolo | Complexidade |
|-----------|---------|-------|------------------|-----------|--------------|
| **BFS** | Menor # hops | Não considera | N/A | RIP | O(V + E) |
| **DFS** | Exploração | Não considera | Detecta ciclos | LLDP/STP | O(V + E) |
| **Dijkstra** | Menor custo | Apenas positivos | Não suporta | OSPF | O(V²) ou O(E log V) |
| **Bellman-Ford** | Menor custo | Suporta negativos | Detecta | RIP distribuído | O(V × E) |

## 👥 Equipe

- Carlos Eduardo Cardoso Silva
- Gabriel Costa de Miranda
- Yago Patrick Schnorr Pinto

Projeto desenvolvido para a disciplina de Teoria de Grafos - CESUPA CC4
