# def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
#     estatistica: Dict[str, Union[List[str], str, int]] = {}
#     if flag != 'detail':
#         estatistica[f'f{agencia}-{dia}'] = len(self.clientes_atendidos)
#     else:
#
#         estatistica['dia'] = dia
#         estatistica['agencia'] = agencia
#         estatistica['clientes_atendidos'] = self.clientes_atendidos
#         estatistica['quantidade_clientes_atendidos'] = (
#             len(self.clientes_atendidos)
#         )
#
#     return estatistica
