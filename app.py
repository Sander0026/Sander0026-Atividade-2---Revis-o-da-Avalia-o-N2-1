from queue import Queue
from src.FilaPedidos import FilaPedidos
from src.FilaGalpoes import FilaGalpoes
from src.GeraPedidos import GeraPedidos
from src.ProcessaPedido import ProcessaPedido
from src.ValidaPedido import ValidaPedido
from src.MelhorRota import MelhorRota



evento = GeraPedidos()
ValidaPedido(evento)
print("")
ProcessaPedido(FilaPedidos)
print("")
MelhorRota()
print("")


