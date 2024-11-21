import random

class Interrupcao:
    def __init__(self) -> None:
        escolha_aleatoria = random.choice(["teclado", "impressora", "disco"])
        self.tipo = escolha_aleatoria
        self.prioridade = 0
        self.tempo_execucao = random.randint(1, 7)

    # def tratar(self):
    #     if self.tipo == "teclado":
    #         self.trata_interrupcao_teclado()
    #     elif self.tipo == "impressora":
    #         self.trata_interrupcao_impressora()
    #     elif self.tipo == "disco":
    #         self.trata_interrupcao_disco()
    #     self.tempo_execucao -= 1

    # def trata_interrupcao_teclado(self):
    #     print("Tratando interrupção teclado...")

    # def trata_interrupcao_impressora(self):
    #     print("Tratando interrupção impressora...")

    # def trata_interrupcao_disco(self):
    #     print("Tratando interrupção disco...")