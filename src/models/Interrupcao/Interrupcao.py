import random

class Interrupcao:
    def __init__(self) -> None:
        escolha_aleatoria = random.choice([{"tipo":"teclado", "prioridade": 1}, {"tipo":"impressora", "prioridade": 2}, {"tipo":"disco", "prioridade": 3}])
        self.tipo = escolha_aleatoria["tipo"]
        self.prioridade = escolha_aleatoria["prioridade"]
        self.tempo_execucao = random.randint(1, 7)
