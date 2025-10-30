import json
import os
from .CalculaDistancia import CalculaDistancia
import math
from .FilaGalpoes import FilaGalpoes

def MelhorRota():
    print("Iniciando cálculo da melhor rota de entrega...")
    caminhoBancoPedidos = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoPedidos.json')
    caminhoBancoGalpoes = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoGalpoes.json')
    caminhoBancoProdutos = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoProdutos.json')

    try:
        with open(caminhoBancoPedidos, 'r', encoding='utf-8') as arq:
            banco_pedidos = json.load(arq)

        with open(caminhoBancoGalpoes, 'r', encoding='utf-8') as arq:
            banco_galpoes = json.load(arq)

        with open(caminhoBancoProdutos, 'r', encoding='utf-8') as arq:
            banco_produtos = json.load(arq)

        # Pega o último pedido processado
        if not banco_pedidos["PedidosProcessados"]:
            print("Nenhum pedido processado encontrado.")
            return
        
        pedido_atual = banco_pedidos["PedidosProcessados"][-1]
        produto_id_pedido = pedido_atual["ProdutoID"]
        print(f"Analisando rota para o PedidoID: {pedido_atual['PedidoID']}")

        # Encontra o produto no banco de produtos para saber quais galpões o têm
        produto_info = None

        for p in banco_produtos["Produtos"]:
            if p["ProdutoID"] == produto_id_pedido:
                produto_info = p
                break 

        if not produto_info:
            print(f"ProdutoID {produto_id_pedido} não encontrado no banco de produtos.")
            return

        galpoes_com_produto = produto_info["GalpoesID"]
        if not galpoes_com_produto:
            print(f"Nenhum galpão possui o ProdutoID {produto_id_pedido}.")
            return

        # Calcula a distância para cada galpão que tem o produto
        melhor_galpao = None
        menor_distancia = math.inf

        for galpao_id in galpoes_com_produto:
            
            galpao_info = None

            # Percorre cada galpão na lista de galpões
            for g in banco_galpoes["Galpoes"]:
                if g["GalpaoID"] == galpao_id:
                    galpao_info = g
                    break 

            if galpao_info:
                distancia = CalculaDistancia(pedido_atual, galpao_info)
                print(f"  - Distância até o Galpão {galpao_id} ({galpao_info['Nome']}): {distancia:.2f}")
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    melhor_galpao = galpao_info
        
        # Retorna o resultado
        if melhor_galpao:
            print(f"\nMelhor rota encontrada! O pedido deve sair do Galpão {melhor_galpao['GalpaoID']} ({melhor_galpao['Nome']}).")
            FilaGalpoes.put(melhor_galpao)
            return {"status": 200, 
                "mensagem": "Pedido valido e adicionado à fila."}
        
    except FileNotFoundError as e:
        print(f"Erro:nam Arquivo não encontrado - {e.filee}")
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar um dos arquivos JSON. Verifique se o formato está correto.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    except KeyError:
        return {"status": 500, 
                "mensagem": "Preencha todos os campos!"}