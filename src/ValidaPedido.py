from FilaPedido import FilaPedido

def ValidaPedido(pedido):
    '''
    {
            "Longitud": 4,
            "Latitude": 5,
            "PedidoID": 2,
            "Cliente": "Maria Oliveira",
            "Data": "2024-06-16",
            "Itens": [
                {
                    "ProdutoID": 303,
                    "NomeProduto": "Tênis Esportivo",
                    "Quantidade": 1,
                    "PrecoUnitario": 199.90
                }
            ],
            "TotalPedido": 199.90
    }
    '''
    FilaPedido.put(pedido)
   