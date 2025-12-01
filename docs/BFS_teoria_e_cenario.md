# BFS (Breadth-First Search) - Busca em Largura

## 🎓 Teoria do Algoritmo BFS

### O que é?

O **BFS (Breadth-First Search)** é um algoritmo de busca em grafos que explora os vértices do grafo **nível por nível** (em largura), começando de um vértice origem.

### Características Principais

- **Exploração por níveis**: Visita todos os vizinhos diretos antes de explorar vizinhos de segundo nível
- **Caminho mais curto**: Garante encontrar o caminho com menor número de arestas
- **Uso de fila**: Utiliza uma estrutura de fila (FIFO - First In, First Out)
- **Complexidade**: O(V + E) onde V = número de vértices e E = número de arestas
- **Aplicável a qualquer grafo**: Não é específico para nenhum domínio

### Como Funciona?

1. **Inicialização**:
   - Marca o vértice inicial como visitado
   - Adiciona o vértice inicial à fila

2. **Exploração**:
   - Remove o primeiro vértice da fila
   - Para cada vizinho não visitado:
     - Marca como visitado
     - Adiciona à fila
     - Registra o caminho

3. **Término**:
   - Para quando a fila está vazia (explorou tudo)
   - Ou quando encontra o destino procurado

### Pseudocódigo

```
BFS(grafo, origem, destino):
    fila = nova Fila()
    visitados = novo Conjunto()
    
    fila.adicionar((origem, [origem]))
    visitados.adicionar(origem)
    
    enquanto fila não está vazia:
        (atual, caminho) = fila.remover()
        
        se atual == destino:
            retornar caminho
        
        para cada vizinho de atual:
            se vizinho não está em visitados:
                visitados.adicionar(vizinho)
                novo_caminho = caminho + [vizinho]
                fila.adicionar((vizinho, novo_caminho))
    
    retornar null  // Não existe caminho
```

### Propriedades Importantes

- ✅ **Completude**: Sempre encontra uma solução se ela existir
- ✅ **Otimalidade**: Encontra o caminho mais curto (em número de arestas)
- ✅ **Espaço**: Requer O(V) de memória para armazenar visitados e fila
- ⚠️ **Limitação**: Não considera pesos das arestas (todas tratadas como peso 1)

### Aplicações Comuns do BFS

1. **Redes de computadores**:
   - Roteamento RIP (Routing Information Protocol)
   - Descoberta de vizinhos
   - Detecção de conectividade

2. **Redes sociais**:
   - Calcular grau de separação entre pessoas
   - Sugestão de amigos (amigos de amigos)
   - Análise de influência

3. **Jogos**:
   - Pathfinding em mapas grid
   - IA para movimentação de NPCs
   - Puzzles (Rubik's cube, 8-puzzle)

4. **Web**:
   - Web crawlers (explorar sites nível por nível)
   - Indexação de páginas
   - Análise de links

5. **Análise de grafos**:
   - Detectar componentes conectados
   - Verificar se grafo é bipartido
   - Encontrar ciclos

6. **Árvores**:
   - Travessia por nível (level-order traversal)
   - Encontrar altura da árvore
   - Serialização de estruturas hierárquicas

---

## 🌐 Cenário: Protocolo RIP em Rede Metropolitana

### Contexto do Problema

Este exemplo demonstra como o **algoritmo BFS puro e genérico** pode resolver um **problema específico de redes**: o roteamento de pacotes usando o protocolo RIP.

### O Protocolo RIP (Routing Information Protocol)

**RIP** é um dos protocolos de roteamento mais antigos da internet, usado para determinar as melhores rotas em redes IP.

#### Características do RIP:
- **Métrica**: Contagem de "hops" (saltos entre roteadores)
- **Objetivo**: Encontrar rota com menor número de hops
- **Limite**: Máximo de 15 hops (evita loops infinitos)
- **Tipo**: Protocolo de vetor de distância
- **Convergência**: Distribuída (cada roteador compartilha sua tabela)

#### Por que BFS resolve RIP?

O problema do RIP ("menor número de hops") é **exatamente** o mesmo que o BFS resolve ("caminho mais curto em arestas")!

**Tradução de conceitos**:
- Vértice → Roteador
- Aresta → Link de rede
- Distância (arestas) → Hops (saltos)
- Caminho mais curto → Rota com menos hops

### Topologia da Rede: MAN (Metropolitan Area Network)

Simulamos uma rede de provedor de internet (ISP) em uma cidade grande com **16 roteadores** organizados em 3 camadas hierárquicas:

#### 🏗️ Arquitetura em 3 Camadas

```
┌─────────────────────────────────────────────────────────────┐
│ CAMADA CORE (Backbone - 4 roteadores)                       │
├─────────────────────────────────────────────────────────────┤
│  • Core-Central  : Datacenter principal                      │
│  • Core-Norte    : PoP zona norte                            │
│  • Core-Sul      : PoP zona sul                              │
│  • Core-Leste    : PoP zona leste                            │
│                                                               │
│  Conectados em anel + conexões cruzadas para redundância     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAMADA DISTRIBUTION (Distribuição - 6 roteadores)           │
├─────────────────────────────────────────────────────────────┤
│  • Dist-ZonaNorte1, Dist-ZonaNorte2                         │
│  • Dist-ZonaSul1, Dist-ZonaSul2                             │
│  • Dist-ZonaLeste                                            │
│  • Dist-ZonaCentral                                          │
│                                                               │
│  Agregam tráfego de múltiplos pontos de acesso              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAMADA ACCESS (Acesso - 6 roteadores)                       │
├─────────────────────────────────────────────────────────────┤
│  • Access-Bairro1, Access-Bairro2 (Zona Norte)              │
│  • Access-Bairro3, Access-Bairro4 (Zona Sul)                │
│  • Access-Bairro5 (Zona Leste)                              │
│  • Access-Centro (Zona Central)                             │
│                                                               │
│  Pontos finais conectando clientes/empresas                  │
└─────────────────────────────────────────────────────────────┘
```

#### Características da Rede:

- **Total**: 16 roteadores, 22 links
- **Tipo**: Grafo não-direcionado (links bidirecionais)
- **Pesos**: Representam latência em milissegundos, mas BFS os ignora
- **Redundância**: Múltiplos caminhos entre pontos (alta disponibilidade)
- **Realismo**: Hierarquia baseada em arquiteturas reais de ISPs

### Cenários de Teste

#### 1. **Pior caso**: Access-Bairro1 → Access-Bairro4
Cliente de um extremo a outro da cidade (atravessa todas as camadas)

#### 2. **Múltiplas rotas**: Core-Central → Core-Leste
Rota direta (1 hop) vs. pelo anel (2+ hops) - BFS escolhe a mais curta

#### 3. **Rota inter-regional**: Access-Centro → Access-Bairro5
Comunicação entre diferentes zonas da cidade

#### 4. **Comunicação hierárquica**: Entre roteadores Distribution
Mostra como o backbone conecta diferentes regiões

#### 5. **Subida/descida**: Access ↔ Core
Demonstra a navegação vertical na hierarquia

#### 6. **Tabela de roteamento completa**
Gera tabela RIP com rotas para todos os destinos (simula protocolo real)

---

## 📊 Análise: RIP usando BFS

### ✅ Vantagens do RIP (BFS)

1. **Simplicidade**:
   - Algoritmo fácil de implementar e entender
   - Baixa complexidade computacional O(V + E)
   - Configuração mínima necessária

2. **Rapidez**:
   - Encontra rotas muito rápido
   - Adequado para redes pequenas e médias

3. **Convergência**:
   - Propaga mudanças de forma distribuída
   - Cada roteador compartilha sua tabela com vizinhos

4. **Baixo overhead**:
   - Pouca memória necessária
   - Processamento simples

### ⚠️ Limitações do RIP

1. **Ignora qualidade do link**:
   - Não considera latência, largura de banda ou congestionamento
   - Um link de 10ms e um de 100ms são tratados igual

2. **Métrica simplista**:
   - 2 hops lentos podem ser piores que 3 hops rápidos
   - Exemplo: 2 hops de satélite (500ms cada) vs 3 hops fibra (2ms cada)

3. **Limite de 15 hops**:
   - Inadequado para redes grandes e complexas
   - Redes com mais de 15 saltos não são suportadas

4. **Convergência lenta**:
   - Em redes grandes, demora para propagar mudanças
   - "Count to infinity" problem (problema clássico do RIP)

### 🔍 Quando usar BFS/RIP?

#### ✓ Use quando:
- Redes pequenas/médias (< 15 roteadores)
- Latência uniforme entre links
- Simplicidade é prioritária
- Recursos computacionais limitados
- Rede estática (poucas mudanças)

#### ✗ Evite quando:
- Redes grandes e complexas → Use **Dijkstra (OSPF)**
- Links heterogêneos (diferentes velocidades) → Use **Dijkstra (OSPF)**
- Necessita otimização por custo/latência → Use **Dijkstra (OSPF)**
- Ambiente dinâmico com falhas frequentes → Use protocolos modernos

---

## 🎯 Lição Principal

**Um ALGORITMO GENÉRICO bem projetado pode resolver MÚLTIPLOS PROBLEMAS!**

O BFS não sabe nada sobre redes, roteadores ou protocolos de internet. Ele apenas resolve o problema genérico de "encontrar o caminho mais curto em número de arestas".

Mas isso é **exatamente** o que o protocolo RIP precisa! Por isso, o BFS puro resolve perfeitamente o roteamento RIP sem precisar ser modificado.

### Próximos Passos

- **DFS**: Descoberta de topologia e detecção de loops
- **Dijkstra**: Roteamento com custos (OSPF) - melhor que BFS para redes reais
- **Bellman-Ford**: Roteamento distribuído (RIP real) com pesos negativos

---

## 📚 Referências

- **RIP**: RFC 2453 - RIP Version 2
- **BFS**: Introduction to Algorithms (CLRS), Cap. 22
- **Redes**: Computer Networks (Tanenbaum), Cap. 5
