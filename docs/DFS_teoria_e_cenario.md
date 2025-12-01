# DFS (Depth-First Search) - Busca em Profundidade

## 🎓 Teoria do Algoritmo DFS

### O que é?

O **DFS (Depth-First Search)** é um algoritmo de busca em grafos que explora os vértices do grafo **em profundidade**, seguindo um caminho até o fim antes de retroceder (backtracking).

### Características Principais

- **Exploração profunda**: Vai o mais fundo possível antes de voltar
- **Uso de pilha**: Utiliza pilha (implícita via recursão ou explícita)
- **Backtracking**: Retrocede quando não há mais vizinhos não visitados
- **Complexidade**: O(V + E) onde V = número de vértices e E = número de arestas
- **NÃO garante caminho mais curto**: Encontra UM caminho, não necessariamente o menor
- **Aplicável a qualquer grafo**: Não é específico para nenhum domínio

### Como Funciona?

1. **Inicialização**:
   - Marca o vértice inicial como visitado
   - Adiciona à pilha (ou chama recursivamente)

2. **Exploração**:
   - Para o vértice atual, escolhe um vizinho não visitado
   - Visita esse vizinho recursivamente (vai fundo)
   - Quando não há mais vizinhos não visitados, retrocede (backtrack)

3. **Término**:
   - Para quando todos os vértices alcançáveis foram visitados
   - Ou quando encontra o objetivo (em busca direcionada)

### Pseudocódigo

```
DFS(grafo, origem):
    visitados = novo Conjunto()
    
    DFS_Recursivo(origem, visitados)

DFS_Recursivo(vertice, visitados):
    visitados.adicionar(vertice)
    processar(vertice)
    
    para cada vizinho de vertice:
        se vizinho não está em visitados:
            DFS_Recursivo(vizinho, visitados)
```

### Propriedades Importantes

- ✅ **Completude**: Encontra solução se ela existir (em espaço finito)
- ❌ **Otimalidade**: NÃO garante o caminho mais curto
- ✅ **Espaço**: Requer O(V) no pior caso (profundidade máxima)
- ✅ **Classificação de arestas**: Identifica tipos de arestas (tree, back, forward, cross)
- ✅ **Detecção de ciclos**: Back edges indicam ciclos

### Tipos de Arestas no DFS

Em grafos direcionados, DFS classifica arestas em:

1. **Tree edges** (Árvore): Arestas que formam a árvore DFS
2. **Back edges** (Retorno): Apontam para ancestrais → indicam CICLOS
3. **Forward edges** (Avanço): Apontam para descendentes (não na árvore)
4. **Cross edges** (Cruzamento): Conectam subárvores diferentes

### DFS vs BFS

| Característica | DFS | BFS |
|---------------|-----|-----|
| Estrutura | Pilha (recursão) | Fila |
| Exploração | Profundidade | Largura |
| Caminho mais curto | ❌ Não | ✅ Sim |
| Uso de memória | Menor (O(altura)) | Maior (O(largura)) |
| Detecção de ciclos | ✅ Excelente | ⚠️ Possível |
| Componentes conectados | ✅ Excelente | ✅ Excelente |

### Aplicações Comuns do DFS

1. **Detecção de ciclos**:
   - Encontrar loops em redes
   - Validar grafos acíclicos (DAG)
   - Spanning Tree Protocol (STP)

2. **Componentes conectados**:
   - Identificar segmentos de rede isolados
   - Análise de conectividade
   - Particionamento de grafos

3. **Ordenação topológica**:
   - Dependências de tarefas
   - Compilação de programas
   - Resolução de pré-requisitos

4. **Descoberta de topologia**:
   - Protocolos de descoberta (LLDP, CDP)
   - Mapeamento de redes
   - Análise de estrutura

5. **Pathfinding**:
   - Labirintos e puzzles
   - IA de jogos
   - Backtracking em problemas de busca

6. **Análise de grafos**:
   - Pontes e pontos de articulação
   - Componentes fortemente conectados
   - Biconectividade

---

## 🌐 Cenário: Descoberta de Topologia em Rede Corporativa

### Contexto do Problema

Este exemplo demonstra como o **algoritmo DFS puro e genérico** pode resolver problemas específicos de **descoberta e análise de redes**: mapeamento de topologia, detecção de loops e identificação de segmentos.

### Protocolos de Descoberta de Rede

Protocolos como **LLDP (Link Layer Discovery Protocol)** e **CDP (Cisco Discovery Protocol)** usam conceitos similares ao DFS para descobrir dispositivos vizinhos e mapear a topologia da rede.

#### Características:
- **Descoberta automática**: Mapeia dispositivos e conexões
- **Exploração sistemática**: Visita cada dispositivo sequencialmente
- **Detecção de loops**: Identifica links redundantes que formam ciclos
- **Componentes**: Identifica segmentos isolados (falhas de conectividade)

#### Por que DFS resolve esses problemas?

O DFS é perfeito para:
1. **Exploração completa**: Visita todos os dispositivos alcançáveis
2. **Detecção de loops**: Back edges revelam ciclos na topologia
3. **Segmentação**: Múltiplas execuções identificam componentes separados
4. **Árvore de descoberta**: Constrói árvore hierárquica da rede

**Tradução de conceitos**:
- Vértice → Dispositivo de rede (switch, router)
- Aresta → Link/conexão física
- Caminho → Sequência de dispositivos conectados
- Ciclo → Loop na topologia (redundância ou problema)
- Componente → Segmento de rede isolado

### Topologia da Rede: Corporação Distribuída

Simulamos uma **rede corporativa distribuída** com **18 dispositivos** em múltiplos sites:

#### 🏗️ Arquitetura Multi-Site

```
┌─────────────────────────────────────────────────────────────┐
│ HEADQUARTERS (Sede - 6 dispositivos)                        │
├─────────────────────────────────────────────────────────────┤
│  Core Layer:                                                 │
│    • HQ-Core-SW1, HQ-Core-SW2 (backbone principal)          │
│                                                               │
│  Distribution Layer:                                         │
│    • HQ-Dist-SW1, HQ-Dist-SW2 (distribuição)                │
│                                                               │
│  Access Layer:                                               │
│    • HQ-Access-SW1, HQ-Access-SW2 (acesso)                  │
│                                                               │
│  Links redundantes entre camadas                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DATA CENTER (2 dispositivos)                                │
├─────────────────────────────────────────────────────────────┤
│  • DC-Core-SW1, DC-Core-SW2                                 │
│  • Conecta com HQ via links redundantes                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ BRANCH OFFICE 1 (Filial 1 - 5 dispositivos)                │
├─────────────────────────────────────────────────────────────┤
│  • Branch1-Router (roteador WAN)                            │
│  • Branch1-SW1, Branch1-SW2 (switches core)                 │
│  • Branch1-Access1, Branch1-Access2 (acesso)                │
│  • Conecta com HQ via WAN                                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ BRANCH OFFICE 2 (Filial 2 - 5 dispositivos)                │
├─────────────────────────────────────────────────────────────┤
│  • Branch2-Router (roteador WAN)                            │
│  • Branch2-SW1, Branch2-SW2 (switches core)                 │
│  • Branch2-Access1, Branch2-Access2 (acesso)                │
│  • Conecta com HQ via WAN                                   │
└─────────────────────────────────────────────────────────────┘
```

#### Características da Rede:

- **Total**: 18 dispositivos, múltiplos links redundantes
- **Tipo**: Grafo não-direcionado (links bidirecionais)
- **Redundância**: Múltiplos caminhos entre sites (alta disponibilidade)
- **Loops**: Links redundantes formam ciclos (testam STP)
- **Realismo**: Arquitetura baseada em redes corporativas reais

### Cenários de Teste

#### 1. **Descoberta Completa de Topologia**
Inicia do Core HQ e mapeia toda a rede alcançável

#### 2. **Detecção de Loops**
Identifica links redundantes que formam ciclos (importante para STP)

#### 3. **Identificação de Segmentos Isolados**
Detecta componentes desconectados (falhas de WAN, partições)

#### 4. **Exploração a partir de Filial**
Descobre topologia da perspectiva de um site remoto

#### 5. **Análise de Conectividade**
Verifica se todos os sites estão alcançáveis

---

## 📊 Análise: DFS para Descoberta de Redes

### ✅ Vantagens do DFS

1. **Exploração completa**:
   - Garante visitar todos os dispositivos alcançáveis
   - Constrói árvore completa de descoberta

2. **Detecção eficiente de loops**:
   - Back edges revelam imediatamente ciclos
   - Fundamental para Spanning Tree Protocol

3. **Baixo uso de memória**:
   - O(altura da árvore) em vez de O(largura)
   - Eficiente para redes hierárquicas (comum em empresas)

4. **Componentes conectados**:
   - Identifica facilmente segmentos isolados
   - Detecta falhas de conectividade

5. **Árvore hierárquica**:
   - Estrutura natural para topologias em camadas
   - Representa bem arquiteturas Core/Distribution/Access

### ⚠️ Limitações do DFS

1. **Caminho não otimizado**:
   - Não encontra o caminho mais curto
   - Pode explorar rotas longas desnecessariamente

2. **Ordem arbitrária**:
   - Ordem de exploração depende da ordem dos vizinhos
   - Diferentes execuções podem gerar árvores diferentes

3. **Não considera custos**:
   - Ignora latência, largura de banda, etc.
   - Apenas estrutura topológica

### 🔍 Quando usar DFS?

#### ✓ Use quando:
- Precisa mapear topologia completa
- Quer detectar loops/ciclos
- Busca componentes desconectados
- Analisa estrutura hierárquica
- Implementa Spanning Tree Protocol
- Memória é limitada (redes muito grandes)

#### ✗ Evite quando:
- Precisa do caminho mais curto → Use **BFS**
- Quer otimizar por custo/latência → Use **Dijkstra**
- Necessita análise de centralidade → Use algoritmos específicos

---

## 🎯 Aplicações Práticas

### 1. Spanning Tree Protocol (STP)

STP usa conceitos similares ao DFS para:
- Detectar loops na rede L2
- Desabilitar portas redundantes
- Criar árvore spanning livre de loops

### 2. Link Layer Discovery Protocol (LLDP)

LLDP descobre vizinhos sequencialmente:
- Cada dispositivo anuncia sua presença
- Constrói mapa da topologia
- Identifica conexões físicas

### 3. Diagnóstico de Rede

DFS ajuda a:
- Mapear dispositivos alcançáveis
- Identificar segmentos isolados
- Verificar conectividade end-to-end
- Detectar falhas de link

---

## 🎯 Lição Principal

**Um ALGORITMO GENÉRICO (DFS) resolve MÚLTIPLOS PROBLEMAS de redes!**

O DFS não sabe nada sobre switches, routers ou protocolos de rede. Ele apenas explora grafos em profundidade.

Mas isso é **exatamente** o que precisamos para:
- Descobrir topologia de rede
- Detectar loops (Spanning Tree)
- Identificar segmentos isolados
- Construir árvores hierárquicas

### Comparação: BFS vs DFS

| Problema | BFS | DFS |
|----------|-----|-----|
| Caminho mais curto (hops) | ✅ Melhor | ❌ |
| Descoberta de topologia | ✅ Bom | ✅ Melhor |
| Detecção de loops | ⚠️ Possível | ✅ Melhor |
| Componentes conectados | ✅ Bom | ✅ Melhor |
| Uso de memória | ⚠️ Maior | ✅ Menor |
| Protocolo RIP (hops) | ✅ Perfeito | ❌ |
| Spanning Tree | ❌ | ✅ Perfeito |

---

## 📚 Referências

- **STP**: IEEE 802.1D - Spanning Tree Protocol
- **LLDP**: IEEE 802.1AB - Link Layer Discovery Protocol
- **DFS**: Introduction to Algorithms (CLRS), Cap. 22
- **Network Discovery**: Network Management Best Practices
