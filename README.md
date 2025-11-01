# 🚚 Sistema de Processamento e Entrega de Pedidos 📦

Este projeto simula um sistema de processamento e entrega de pedidos, demonstrando um fluxo de trabalho desde a geração de um pedido até a notificação de sua expedição. O sistema utiliza uma arquitetura baseada em filas para desacoplar os diferentes estágios do processo.

## 📝 Visão Geral do Projeto

O fluxo do sistema é orquestrado pelo arquivo `app.py` e segue os seguintes passos:

1.  **Geração de Pedidos** 🛍️: Novos pedidos são gerados aleatoriamente.
2.  **Validação de Pedidos** ✅: Os pedidos gerados são validados para garantir que contenham todas as informações necessárias.
3.  **Processamento de Pedidos** 🔄: Os pedidos válidos são processados e armazenados em um "banco de dados" de pedidos processados.
4.  **Cálculo da Melhor Rota** 🗺️: O sistema determina o melhor galpão para despachar o pedido com base na localização do cliente e na disponibilidade do produto.
5.  **Geração de Ordem de Serviço** 🧾: Uma ordem de serviço é criada com todos os detalhes para a equipe de logística.
6.  **Notificação** 🔔: O cliente e a equipe de logística são notificados sobre a nova ordem de serviço.

## 🏗️ Estrutura do Projeto

O projeto está organizado da seguinte forma:

-   `app.py`: O ponto de entrada da aplicação, que orquestra a execução dos diferentes módulos.
-   `docs/`: Contém os arquivos JSON que simulam o banco de dados do sistema:
    -   `BancoGalpoes.json`: Armazena informações sobre os galpões.
    -   `BancoPedidos.json`: Armazena os pedidos que foram processados.
    -   `BancoProdutos.json`: Armazena informações sobre os produtos.
-   `filas/`: Módulos que definem as filas utilizadas para a comunicação entre os componentes do sistema:
    -   `FilaGalpoes.py`: Fila para os galpões selecionados para a entrega.
    -   `FilaOrdemServico.py`: Fila para as ordens de serviço geradas.
    -   `FilaPedidos.py`: Fila para os pedidos pendentes de processamento.
-   `src/`: Contém a lógica de negócio do sistema:
    -   `GeraPedidos.py`: Gera novos pedidos.
    -   `ValidaPedido.py`: Valida os pedidos.
    -   `ProcessaPedido.py`: Processa os pedidos.
    -   `MelhorRota.py`: Calcula a melhor rota de entrega.
    -   `CalculaDistancia.py`: Calcula a distância entre dois pontos.
    -   `OrdemServico.py`: Gera as ordens de serviço.
    -   `Notificacao.py`: Envia as notificações.
-   `schema/`: Contém o diagrama da arquitetura do sistema.

## 🚀 Como Executar

Para executar a simulação, basta rodar o arquivo `app.py`:

```bash
python app.py
```

Isso iniciará o processo de geração, validação, processamento e entrega de um pedido, exibindo no console as informações de cada etapa.

## 🏛️ Arquitetura

O sistema utiliza uma arquitetura de micro-serviços simulada, onde cada componente é responsável por uma parte específica do processo. A comunicação entre os componentes é feita através de filas, o que garante o desacoplamento e a escalabilidade do sistema.

![Arquitetura do Sistema](schema/Atividade%20%232%20-%20Revis%C3%A3o%20da%20Avalia%C3%A7%C3%A3o%20N2-1.drawio.png)