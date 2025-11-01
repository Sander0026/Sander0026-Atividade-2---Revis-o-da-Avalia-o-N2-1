import json
import os
import uuid
from datetime import datetime
from filas.FilaOrdemServico import FilaOrdemServico
from .CalculaDistancia import CalculaDistancia

# Gera uma Ordem de Serviço baseada na melhor rota já calculada
def OrdemDeServico(FilaGalpoes):
    print("Iniciando geração de Ordem de Serviço...")
    caminhoBancoProdutos = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoProdutos.json')
    caminhoBancoPedidos = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoPedidos.json')
    caminhoBancoGalpoes = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoGalpoes.json')

    try:
        if FilaGalpoes.empty():
            print("Nenhum galpão na fila. Confira a melhor rota antes de gerar Ordem de Serviço.")
            return

        dados_fila = FilaGalpoes.get()
        melhor_galpao = dados_fila.get("melhor_galpao")
        pedido_id = dados_fila.get("pedidoID")

        with open(caminhoBancoPedidos, 'r', encoding='utf-8') as arq:
            banco_pedidos = json.load(arq)

        with open(caminhoBancoProdutos, 'r', encoding='utf-8') as arq:
            banco_produtos = json.load(arq)

        # Busca os dados do pedido no BancoPedidos
        pedido = None
        for p in banco_pedidos["PedidosProcessados"]:
            if p["PedidoID"] == pedido_id:
                pedido = p
                break

        if not pedido:
            print(f"Pedido {pedido_id} não encontrado no banco.")
            return

        # Busca o produto
        produto = None
        for prod in banco_produtos["Produtos"]:
            if prod["ProdutoID"] == pedido["ProdutoID"]:
                produto = prod
                break

        if not produto:
            print(f"Produto {pedido['ProdutoID']} não encontrado.")
            return

        # Calcula distância final cliente ↔ galpão
        distancia = CalculaDistancia(pedido, melhor_galpao)

        # Cria a ordem de serviço (OS)
        os_dados = {
            "OS_ID": str(uuid.uuid4()),
            "PedidoID": pedido["PedidoID"],
            "Cliente": pedido["Cliente"],
            "Produto": produto["Nome"],
            "Galpao": melhor_galpao["Nome"],
            "Localizacao_Galpao": melhor_galpao['localizacao'],
            "Data_Geracao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Distancia_KM": round(distancia, 2),
            "Status": "AGUARDANDO_EXPEDICAO"
        }

        # Envia para fila de Ordens de Serviço
        FilaOrdemServico.put(os_dados)
        print(f"Ordem de Serviço gerada e adicionada à fila: {os_dados['OS_ID']}")
        print(json.dumps(os_dados, indent=4, ensure_ascii=False))
        return os_dados

    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e.filename}")
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar um dos arquivos JSON.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")