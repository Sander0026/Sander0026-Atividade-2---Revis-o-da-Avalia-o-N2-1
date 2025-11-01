import json
import os

def ProcessaPedido(Fila):
    print("Iniciando o processamento de pedidos...")
    
    pedido = Fila.get()
     
    try:
        if ('PedidoID' in pedido and 
            'Latitude' in pedido and 
            'Longitude' in pedido):
            pedido['Status'] = 'PROCESSADO'
            print(f"Pedido {pedido['PedidoID']} processado com sucesso.")

            # Constrói o caminho relativo para o arquivo JSON
            caminhoBancoPedidos = os.path.join(os.path.dirname(__file__), '..', 'docs', 'BancoPedidos.json')
            
            # Abre o arquivo para leitura e carrega os dados
            with open(caminhoBancoPedidos, 'r', encoding='utf-8') as arq:
                BancoPedidos = json.load(arq)
           
            # Adiciona o novo pedido processado à lista
            BancoPedidos["PedidosProcessados"].append(pedido)

            # Abre o arquivo para escrita e salva os dados atualizados
            with open(caminhoBancoPedidos, 'w', encoding='utf-8') as arq:
                json.dump(BancoPedidos, arq, indent=4, ensure_ascii=False)

            return {"status": 200, 
                    "mensagem": "Pedido processado com sucesso."}
        
    except KeyError:
        return {"status": 500, 
                "mensagem": "Preencha todos os campos!"}
