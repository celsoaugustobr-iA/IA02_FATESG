# Respostas: NoSQL e Modelagem de Dados - 2º Período de Sistemas/IA

1. DEFINIÇÃO E CONCEITOS BASE
a) Bancos NoSQL (Not Only SQL) se diferenciam pela flexibilidade estrutural, operando sem a necessidade de esquemas tabulares fixos. Eles permitem o armazenamento de dados semiestruturados e não estruturados, priorizando a performance e o particionamento de dados em vez da normalização rigorosa do modelo relacional.

b) Entre as vantagens principais, destaco a escalabilidade horizontal facilitada, a agilidade no desenvolvimento (pela falta de impedância entre o código e o banco) e a capacidade de lidar com grandes volumes de escrita e leitura sob alta latência, algo complexo em bancos SQL tradicionais.

c) Aplicações práticas:
- Sistemas de mensageria e chats (persistência de mensagens em tempo real).
- Gestão de catálogos dinâmicos em e-commerces (produtos com diferentes atributos).
- Armazenamento de telemetria e dados de sensores (IoT) com formatos variáveis.

2. TAXONOMIA DE BANCOS NÃO-RELACIONAIS
a) Categorias principais:
- Orientados a Documentos: Organizam dados em formatos similares ao JSON, permitindo hierarquias complexas em um único registro (Ex: MongoDB).
- Chave-Valor: Funcionam como uma tabela de hash global, focados em máxima velocidade de acesso via chave única (Ex: Redis).
- Wide-Column (Colunas): Armazenam dados em famílias de colunas, otimizando a agregação e consulta em datasets massivos (Ex: Cassandra).
- Grafos: Modelam os dados como nós e arestas, sendo especialistas em analisar conexões e caminhos (Ex: Neo4j).

b) Ferramentas de mercado:
- Documentos: MongoDB, CouchDB e Firestore.
- Chave-Valor: Redis e Amazon DynamoDB.
- Colunas: Apache Cassandra e ScyllaDB.
- Grafos: Neo4j e JanusGraph.

3. ANÁLISE DE MODELAGEM
a) A diferença fundamental é que o modelo relacional foca na estrutura das entidades (tabelas) e usa junções (JOINs) em tempo de execução. Já o modelo de grafos foca na relação entre essas entidades; as conexões são persistidas fisicamente, o que torna a navegação entre dados interconectados muito mais performática.

b) Para redes sociais, o modelo de Grafos é o padrão ouro. O motivo é a natureza dos dados: o valor está nas conexões (amizades, interesses, interações). Operações como "recomendar amigos de amigos" são resolvidas com algoritmos de travessia simples em grafos, enquanto no SQL exigiriam consultas recursivas extremamente pesadas.

4. ESCALABILIDADE E ESTRUTURA
a) A escalabilidade horizontal consiste em distribuir a carga de processamento e armazenamento entre múltiplos servidores (nós) de um cluster. Através do sharding, o banco divide o conjunto de dados em pedaços menores e os distribui, permitindo aumentar a capacidade total do sistema apenas adicionando novas máquinas baratas, sem depender de um único hardware potente.

b) O schema flexível é vital porque permite que o banco evolua junto com a aplicação. Em um ambiente de desenvolvimento ágil, onde novos campos são criados constantemente, não há necessidade de travar o banco para realizar um "ALTER TABLE". Isso garante alta disponibilidade e reduz drasticamente o tempo de manutenção do banco de dados.

5. ESTUDO DE CASO: NETFLIX
a) Um caso emblemático é o uso do Apache Cassandra pela Netflix para sustentar sua arquitetura global.

b) A ferramenta é usada para gerenciar o estado das sessões, históricos de visualização e as listas personalizadas de cada usuário. Devido à natureza distribuída do Cassandra, a Netflix consegue replicar dados entre diferentes regiões geográficas. O benefício direto é a tolerância a falhas: se um data center cai, os usuários são redirecionados para outro sem perceber interrupções, mantendo a consistência dos dados de visualização de forma transparente e em escala massiva.