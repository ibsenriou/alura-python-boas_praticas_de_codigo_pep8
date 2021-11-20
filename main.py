# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
#
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada
# fila_teste = FilaNormal()
#
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
#
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))
# print(FilaNormal.clientes_atendidos)
#
# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
# fila_teste_2.atualiza_fila()
#
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.chama_cliente(3))
#
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica_pra_normal = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()


teste_fabrica_pra_normal.atualiza_fila()
teste_fabrica_pra_normal.atualiza_fila()

print(teste_fabrica.chama_cliente(3))
print(teste_fabrica.chama_cliente(5))
print(teste_fabrica.chama_cliente(10))

print(teste_fabrica_pra_normal.chama_cliente(3))
print(teste_fabrica_pra_normal.chama_cliente(2))

print(teste_fabrica.estatistica(EstatisticaResumida('20/03/2021', 120)))
