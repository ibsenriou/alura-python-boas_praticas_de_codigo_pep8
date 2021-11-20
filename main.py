from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste = FilaNormal()

fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))
print(FilaNormal.clientes_atendidos)

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()

print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(3))

print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))
