class OS:
    def __init__(self):
        self.tempo_salvo = 0
        self.pc_salvo = 0x0
        self.ponteiro_pilha_salvo = 0x0
        self.fila_de_interrupcoes = []

    def salva_contexto(self, processo):
        self.tempo_salvo = processo.tempo
        self.pc_salvo = processo.pc
        self.ponteiro_pilha_salvo = processo.ponteiro_pilha

    def adicionar_na_fila_de_interrupcoes(self, interrupcao):
        indice = 0
        while indice < len(self.fila_de_interrupcoes) and self.fila_de_interrupcoes <= interrupcao.prioridade:
            indice += 1
        self.fila_de_interrupcoes.insert(indice, interrupcao)

    def tratar_interrupcao(self):
        interrupcao = self.fila_de_interrupcoes[0]
        interrupcao.tempo_execucao -= 1

        if interrupcao.tempo_execucao == 0:
            self.fila_de_interrupcoes.pop(0)