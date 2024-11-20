class Processo:
    def __init__(self) -> None:
        self.tempo = 0
        self.pc = 0     # program counter
        self.pilha = 0  # stack pointer

    def executa(self):
        self.tempo += 1
        self.pc += 4
        self.pilha += 1000

    def interrompe(self):
        self.tempo = 0
        self.pc = 0
        self.pilha = 0

    def retomar(self, tempo, pilha, pc):
        self.tempo = tempo
        self.pc = pc
        self.pilha = pilha