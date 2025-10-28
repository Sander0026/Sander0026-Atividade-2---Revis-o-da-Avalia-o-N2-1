import json
from FilaPedido import FilaPedido

def ProcessaPedido(fila_pedidos):
    '''
    Processa os pedidos na fila de pedidos.
    '''
    pedido = fila_pedidos.get()
    arq = open('./schema/BancoPedidos.json', 'r')
    dadosBanco = json.loads(arq.read())
    arq.close()
     
    for pedidoBanco in dadosBanco['Pedidos']:

        try:
            if (pedidoBanco['PedidoID'] == pedido['PedidoID'] and 
                pedidoBanco['Cliente'] == pedido['Cliente'] and 
                pedidoBanco['Data'] == pedido['Data']):

                return {"status": 200, 
                        "mensagem": "Pedido processado com sucesso."}
        
        except KeyError:
            return {"status": 500, 
                    "mensagem": "Preencha todos os campos!"}

            
           