from queue import Queue
from src.FilaPedidos import FilaPedidos
from src.GeraPedidos import GeraPedidos
from src.ProcessaPedido import ProcessaPedido
from src.ValidaPedido import ValidaPedido



evento = GeraPedidos()
ValidaPedido(evento)
print("")
ProcessaPedido(FilaPedidos)




