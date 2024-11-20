from utils.loggerUtils import LoggerUtils
from Processo import Processo
import random
import shutil
import signal
import os

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

def salva_contexto(Processo):


if __name__ == "__main__":
    processo = Processo()

    while True:
        processo.executa()
        if chance:
            salva_contexto(processo)
            processo.interrompe()
            interrupcao.tratar()
            processo.retomar()