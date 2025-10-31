from filas.FilaPedidos import FilaPedidos
from filas.FilaGalpoes import FilaGalpoes
from src.GeraPedidos import GeraPedidos
from src.ProcessaPedido import ProcessaPedido
from src.ValidaPedido import ValidaPedido
from src.MelhorRota import MelhorRota
from src.OrdemServico import OrdemDeServico
from filas.FilaGalpoes import FilaGalpoes
from filas.FilaOrdemServico import FilaOrdemServico
from src.Notificacao import Notificacao



evento = GeraPedidos()
ValidaPedido(evento)
print("")
ProcessaPedido(FilaPedidos)
print("")
MelhorRota()
print("")
OrdemDeServico(FilaGalpoes)
print("")
Notificacao(FilaOrdemServico)
print("")




