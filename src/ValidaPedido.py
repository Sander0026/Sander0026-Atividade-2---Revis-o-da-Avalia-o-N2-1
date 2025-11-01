from filas.FilaPedidos import FilaPedidos

def ValidaPedido(evento):
        
    pedido = evento
    try:  
        if ('PedidoID' in pedido and
            'Latitude' in pedido and
            'Longitude' in pedido):

            print(f"Pedido {pedido['PedidoID']} é VÁLIDO. Enviando para FilaPedido.")
            FilaPedidos.put(pedido)
        return {"status": 200, 
                "mensagem": "Pedido valido e adicionado à fila."}
    except KeyError:
        return {"status": 500, 
                "mensagem": "Preencha todos os campos!"}
    