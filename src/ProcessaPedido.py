import json

def ProcessaPedido(Fila):
    print("Iniciando o processamento de pedidos...")
    
    pedido = Fila.get()
     
    try:
        if ('PedidoID' in pedido and 
            'Latitude' in pedido and 
            'Longitud' in pedido):
            pedido['Status'] = 'PROCESSADO'
            print(f"Pedido {pedido['PedidoID']} processado com sucesso.")

            # Caminho para o arquivo JSON
            json_path = 'e:\\Sistemas_Web\\Sander0026-Atividade-2---Revis-o-da-Avalia-o-N2-1\\docs\\BancoPedidos.json'
            
            # Abre o arquivo para leitura e carrega os dados
            with open(json_path, 'r', encoding='utf-8') as arq:
                BancoPedidos = json.load(arq)
           
            # Adiciona o novo pedido processado à lista
            BancoPedidos["PedidosProcessados"].append(pedido)

            # Abre o arquivo para escrita e salva os dados atualizados
            with open(json_path, 'w', encoding='utf-8') as arq:
                json.dump(BancoPedidos, arq, indent=4, ensure_ascii=False)

            return {"status": 200, 
                    "mensagem": "Pedido processado com sucesso."}
        
    except KeyError:
        return {"status": 500, 
                "mensagem": "Preencha todos os campos!"}

