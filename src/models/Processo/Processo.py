import random

class Processo:
    def __init__(self) -> None:
        self.tempo = 0
        self.pc = 0x1000    # program counter
        self.ponteiro_pilha = 0x8000 # stack pointer

    def executa(self):
        self.tempo += 1

        acao_do_pc = random.randint(0, 99)
        if acao_do_pc > 65:
            self.pc += 4    # Incrementa o pc
        else:
            self.pc = random.randint(0x1000, 0xFFFF)    # Simula um desvio

        acao_da_pilha = random.choice(["push", "pop"])
        if acao_da_pilha == "push":
            self.ponteiro_pilha -= random.randint(1, 8)
        else:
            self.ponteiro_pilha += random.randint(1, 8)
        self.ponteiro_pilha = max(0x7000, min(0x8000, self.ponteiro_pilha)) # Limita o ponteiro ao intervalo 0x7000 a 0x8000

    def interrompe(self):
        self.tempo = 0
        self.pc = 0x1000
        self.ponteiro_pilha = 0x8000

    def retomar(self, tempo, pc, pilha):
        self.tempo = tempo
        self.pc = pc
        self.ponteiro_pilha = pilha