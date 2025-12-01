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
- **Objetivo**: Mapear topologia, detectar loops, identificar componentes
- **Cenário**: Rede corporativa distribuída com 18 dispositivos em múltiplos sites
- **Documentação**: [`docs/DFS_teoria_e_cenario.md`](docs/DFS_teoria_e_cenario.md)
- **Execução**: `python -m examples.dfs_demo`

### 🚧 Em desenvolvimento:
- **Dijkstra**: Roteamento OSPF (menor custo considerando pesos)
- **Bellman-Ford**: Roteamento distribuído com pesos negativos

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

# DFS - Descoberta de topologia e loops
python -m examples.dfs_demo
```

packet-routing-system/
├── app/
│   ├── graph.py              # Estrutura do grafo (lista de adjacências)
│   ├── algorithms.py         # Algoritmos puros (BFS, DFS, etc.)
│   └── scenarios/            # Cenários de teste para cada algoritmo
│       ├── bfs_scenario.py   # Rede metropolitana (16 roteadores)
│       └── dfs_scenario.py   # Rede corporativa (18 dispositivos)
├── examples/
│   ├── bfs_demo.py           # Demo BFS: Protocolo RIP
│   └── dfs_demo.py           # Demo DFS: Descoberta de topologia
├── docs/
│   ├── BFS_teoria_e_cenario.md  # Teoria BFS e RIP
│   └── DFS_teoria_e_cenario.md  # Teoria DFS e descoberta de rede
└── README.mdemo.py           # Demonstração do BFS
├── docs/
│   └── BFS_teoria_e_cenario.md  # Teoria e explicação do BFS
└── README.md
```

## 🎯 Filosofia do Projeto

**Algoritmos genéricos resolvendo problemas específicos!**

- Implementamos algoritmos **puros e genéricos**
- Aplicamos a **contextos específicos** (roteamento de pacotes)
- Demonstramos como **um algoritmo pode resolver múltiplos problemas**

## 👥 Equipe

Projeto desenvolvido para a disciplina de Teoria de Grafos - CESUPA CC4
