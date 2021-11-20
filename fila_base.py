import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list[str] = []
    clientes_atendidos: list[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...
