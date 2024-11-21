from utils.loggerUtils import LoggerUtils
from models.Processo import Processo
from models.Interrupcao import Interrupcao
import random
import shutil
import signal
import os

# Contexto salvo pelo sistema operacional
tempo = 0
pc = 0x0
ponteiro_pilha = 0x0

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

def salva_contexto(processo):
    global tempo
    tempo = processo.tempo
    global pc
    pc = processo.pc
    global ponteiro_pilha
    ponteiro_pilha = processo.ponteiro_pilha

if __name__ == "__main__":
    processo = Processo.Processo()

    while True:
        processo.executa()
        chance = random.randint(0, 99)

        if chance < 14:                 # 15% de interromper o processo em andamento
            salva_contexto(processo)
            processo.interrompe()
            interrupcao = Interrupcao.Interrupcao()
            interrupcao.tratar()
            processo.retomar(tempo, pc, ponteiro_pilha)

        input()