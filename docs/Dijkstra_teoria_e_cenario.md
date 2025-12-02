# Dijkstra - Algoritmo de Caminho Mínimo

## 🎓 Teoria do Algoritmo de Dijkstra

### O que é?

O **algoritmo de Dijkstra** é um algoritmo de busca em grafos que encontra o **caminho de menor custo** entre um vértice origem e todos os outros vértices do grafo. Diferente do BFS que conta apenas saltos, Dijkstra considera os **pesos das arestas**.

### Características Principais

- **Exploração gulosa**: Sempre expande o vértice de menor distância conhecido
- **Caminho de menor custo**: Garante encontrar o caminho ótimo baseado em pesos
- **Não suporta pesos negativos**: Funciona apenas com pesos não-negativos
- **Complexidade**: O(V²) implementação básica, O((V + E) log V) com heap
- **Otimalidade**: Sempre encontra a solução ótima

### Como Funciona?

1. **Inicialização**:
   - Define distância da origem como 0
   - Define todas as outras distâncias como infinito
   - Marca todos os vértices como não visitados

2. **Loop principal**:
   - Seleciona o vértice não visitado com menor distância
   - Marca-o como visitado
   - Para cada vizinho não visitado:
     - Calcula nova distância = distância atual + peso da aresta
     - Se nova distância < distância conhecida:
       - Atualiza distância do vizinho
       - Atualiza predecessor

3. **Término**:
   - Quando todos os vértices foram visitados
   - Ou quando o destino foi alcançado

### Pseudocódigo

```
Dijkstra(grafo, origem, destino):
    distancias = {todos vértices: infinito}
    distancias[origem] = 0
    predecessores = {}
    visitados = conjunto vazio
    não_visitados = todos os vértices
    
    enquanto não_visitados não está vazio:
        // Encontra vértice de menor distância
        atual = vértice em não_visitados com menor distancias[atual]
        
        se distancias[atual] == infinito:
            break  // Não há mais vértices alcançáveis
        
        se atual == destino:
            return reconstruir_caminho(predecessores, destino)
        
        visitados.adicionar(atual)
        não_visitados.remover(atual)
        
        // Relaxamento de arestas
        para cada vizinho, peso em grafo.vizinhos(atual):
            se vizinho não em visitados:
                nova_distancia = distancias[atual] + peso
                
                se nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = atual
    
    return null  // Não existe caminho
```

### Propriedades Importantes

- ✅ **Completude**: Sempre encontra uma solução se ela existir
- ✅ **Otimalidade**: Encontra o caminho de menor custo
- ✅ **Eficiência**: Mais eficiente que Bellman-Ford para pesos positivos
- ⚠️ **Limitação**: NÃO funciona com pesos negativos
- 📊 **Espaço**: Requer O(V) de memória

### Comparação: BFS vs Dijkstra

| Característica | BFS | Dijkstra |
|---|---|---|
| **Métrica** | Contagem de saltos | Custo (peso) |
| **Pesos** | Ignora pesos | Usa pesos |
| **Resultado** | Menor nº de arestas | Menor custo total |
| **Complexidade** | O(V + E) | O(V²) ou O((V+E) log V) |
| **Uso de memória** | Fila simples | Fila de prioridade |
| **Aplicação** | Grafos não ponderados | Grafos ponderados |

### Aplicações Comuns do Dijkstra

1. **Redes de computadores**:
   - Protocolo OSPF (Open Shortest Path First)
   - Roteamento baseado em custo/latência
   - QoS (Quality of Service)

2. **GPS e Navegação**:
   - Google Maps, Waze
   - Encontrar rota mais rápida/curta
   - Considerar tráfego, pedágios

3. **Telecomunicações**:
   - Roteamento de chamadas
   - Otimização de largura de banda
   - Planejamento de capacidade

4. **Logística**:
   - Otimização de rotas de entrega
   - Planejamento de transporte
   - Cadeia de suprimentos

5. **Jogos**:
   - Pathfinding com terrenos diferentes
   - IA para movimentação otimizada
   - Planejamento estratégico

6. **Sistemas financeiros**:
   - Otimização de carteiras
   - Análise de fluxo de caixa
   - Redes de liquidação

---

## 🌐 Cenário: Roteamento Corporativo com Diferentes Qualidades de Links

### Contexto do Problema

Este exemplo demonstra como o **algoritmo de Dijkstra** resolve o problema de **roteamento em redes heterogêneas**, onde links têm diferentes qualidades (velocidades, custos, latências).

### Por que BFS não é suficiente?

Imagine dois caminhos entre dois data centers:

**Caminho A** (via satélite):
- 1 hop único
- Latência: 600ms
- **BFS escolhe este!** ✗

**Caminho B** (via fibra óptica):
- 3 hops
- Latência total: 6ms (2ms cada)
- **Dijkstra escolhe este!** ✓

O BFS escolhe erroneamente o satélite porque só conta saltos. Dijkstra considera o custo real!

### Cálculo de Custo OSPF

O protocolo OSPF (que usa Dijkstra) calcula custos baseados em largura de banda:

```
Custo OSPF = 10^8 / largura_de_banda_em_bps
```

#### Custos típicos:

| Tipo de Link | Largura de Banda | Custo OSPF |
|---|---|---|
| **Gigabit Ethernet** | 1 Gbps | 100 |
| **Fast Ethernet** | 100 Mbps | 1.000 |
| **T1 (WAN)** | 1.5 Mbps | 64.000 |
| **Satélite Backup** | 256 Kbps | 200.000 |

Links mais rápidos = custos menores = preferidos pelo algoritmo!

### Topologia da Rede: Rede Corporativa Multi-Site

Simulamos uma empresa com **10 roteadores** em arquitetura hierárquica:

#### 🏗️ Arquitetura em 3 Camadas

```
┌─────────────────────────────────────────────────────────────┐
│ CAMADA CORE (Backbone Gigabit - 3 roteadores)               │
├─────────────────────────────────────────────────────────────┤
│  • Core-A : Data center primário                             │
│  • Core-B : Data center secundário                           │
│  • Core-C : Data center backup                               │
│                                                               │
│  Interconexão: Anel redundante Gigabit (custo 100 cada)     │
│  Latência: ~1ms entre qualquer par                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAMADA DISTRIBUTION (Fast Ethernet - 4 roteadores)          │
├─────────────────────────────────────────────────────────────┤
│  • Dist-North  : Escritório regional norte                   │
│  • Dist-South  : Escritório regional sul                     │
│  • Dist-East   : Escritório regional leste                   │
│  • Dist-West   : Escritório regional oeste                   │
│                                                               │
│  Links para Core: Fast Ethernet (custo 1.000 cada)          │
│  Links entre Distribution: Fast Ethernet (custo 1.000)       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CAMADA ACCESS (WAN T1 + Backup Satélite - 3 roteadores)    │
├─────────────────────────────────────────────────────────────┤
│  • Remote-Office1 : Filial remota 1                          │
│  • Remote-Office2 : Filial remota 2                          │
│  • Remote-Office3 : Filial remota 3                          │
│                                                               │
│  Links primários: T1 WAN (custo 64.000 cada)                │
│  Links backup: Satélite (custo 200.000 cada)                │
│  Usado apenas em caso de falha do link principal            │
└─────────────────────────────────────────────────────────────┘
```

#### Características da Rede:

- **Total**: 10 roteadores, 15 links
- **Tipo**: Grafo não-direcionado
- **Pesos**: Custos OSPF baseados em largura de banda
- **Redundância**: Links backup com custo alto (só usados em emergência)
- **Realismo**: Baseado em arquiteturas corporativas reais

### Cenários de Teste - Comparação BFS vs Dijkstra

#### Cenário Crítico: Remote-Office1 → Remote-Office2

**Opção A - Link direto via satélite**:
- Hops: 1 (direto)
- Custo: 200.000
- **BFS escolhe esta rota!** ❌

**Opção B - Via backbone corporativo**:
- Hops: 3 (Remote1 → Dist-North → Dist-South → Remote2)
- Custo: 64.000 + 1.000 + 64.000 = 129.000
- **Dijkstra escolhe esta rota!** ✅

**Resultado**: Dijkstra encontra uma rota **35% mais eficiente** em custo real, mesmo usando mais hops!

#### Outros Cenários Testados:

1. **Core-A → Core-C**: Múltiplos caminhos no backbone
2. **Core-A → Remote-Office1**: Descida pela hierarquia
3. **Dist-North → Dist-East**: Comunicação inter-regional
4. **Core-B → Remote-Office3**: Caminho longo através da rede

---

## 📊 Análise: Por que Dijkstra é Superior ao BFS em Redes Reais?

### ✅ Vantagens do Dijkstra (OSPF)

1. **Decisões inteligentes**:
   - Considera qualidade real dos links
   - Evita links lentos mesmo que sejam diretos
   - Otimiza para performance real, não apenas saltos

2. **Escalabilidade**:
   - Sem limite de hops (diferente do RIP/BFS)
   - Adequado para redes grandes e complexas
   - Usado na internet backbone

3. **Flexibilidade**:
   - Pode usar diferentes métricas (latência, custo $, confiabilidade)
   - Administrador define pesos customizados
   - Adapta-se a diferentes necessidades

4. **Convergência rápida**:
   - Atualiza rotas rapidamente após mudanças
   - Link-state protocol (cada roteador tem mapa completo)
   - Menos problemas que distance-vector (RIP)

5. **Suporte a VLSM e CIDR**:
   - Protocolos modernos de endereçamento IP
   - Melhor utilização do espaço de endereços

### ⚠️ Desvantagens

1. **Complexidade computacional**:
   - Mais processamento que BFS
   - Mais memória necessária (mantém mapa completo da rede)
   - Requer roteadores mais potentes

2. **Overhead de protocolo**:
   - Mensagens LSA (Link State Advertisement) maiores
   - Mais tráfego de controle na inicialização
   - Database synchronization complexa

3. **Configuração**:
   - Mais complexo de configurar que RIP
   - Requer planejamento de áreas (em redes grandes)
   - Conhecimento técnico mais avançado

4. **Não suporta pesos negativos**:
   - Limitação matemática do algoritmo
   - Não pode representar "descontos" ou "créditos"
   - Para isso, use Bellman-Ford

### 🔍 Quando usar Dijkstra/OSPF?

#### ✓ Use quando:
- Redes médias a grandes (> 15 roteadores)
- Links heterogêneos (diferentes velocidades)
- Performance é crítica
- Rede complexa com múltiplos caminhos
- Ambiente corporativo profissional
- Necessita convergência rápida

#### ✗ Use BFS/RIP quando:
- Rede muito pequena (< 10 roteadores)
- Todos os links têm mesma qualidade
- Dispositivos com recursos limitados
- Simplicidade é mais importante que otimização
- Ambiente de aprendizado/laboratório

---

## 🎯 Comparação Prática: BFS vs Dijkstra

### Exemplo Real de Diferença

**Situação**: Enviar dados de São Paulo para Rio de Janeiro

#### Rota BFS (RIP):
```
SP → Rio (via satélite direto)
- Hops: 1
- Latência: 600ms
- Perda de pacotes: 2%
- Custo: Alto
```

#### Rota Dijkstra (OSPF):
```
SP → Campinas → Brasília → Belo Horizonte → Rio (via fibra)
- Hops: 4
- Latência total: 12ms
- Perda de pacotes: 0.01%
- Custo: Menor
```

**Conclusão**: Dijkstra escolhe o caminho **50x mais rápido** mesmo usando 4x mais saltos!

---

## 💡 Lição Principal

**Nem sempre o caminho mais curto (em saltos) é o mais rápido!**

Em redes reais, a **qualidade dos links** importa tanto quanto (ou mais que) a quantidade de saltos. O algoritmo de Dijkstra resolve esse problema considerando o **custo real** de cada link.

### Relação com Protocolos Reais

- **RIP** = BFS (ignora qualidade dos links)
- **OSPF** = Dijkstra (considera custo/velocidade)
- **BGP** = Dijkstra modificado (roteamento entre sistemas autônomos)

### Próximos Passos

- **Bellman-Ford**: Suporta pesos negativos e roteamento distribuído
- **A\***: Dijkstra com heurística para otimização adicional
- **Floyd-Warshall**: Caminhos mínimos entre todos os pares

---

## 📚 Referências

- **OSPF**: RFC 2328 - OSPF Version 2
- **Dijkstra**: "A Note on Two Problems in Connexion with Graphs" (1959)
- **Algoritmos**: Introduction to Algorithms (CLRS), Cap. 24
- **Redes**: Computer Networks (Tanenbaum), Cap. 5.2
