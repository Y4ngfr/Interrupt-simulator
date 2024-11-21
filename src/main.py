from utils.loggerUtils import LoggerUtils
from models.Processo import Processo
from models.Interrupcao import Interrupcao
from models.OS import OS

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

import random
import time
import shutil
import signal
import os

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

console = Console()

if __name__ == "__main__":
    processo = Processo.Processo()
    os = OS.OS()

    signal.signal(signal.SIGINT, handle_sigint)

    while True:
        chance_de_nova_interrupcao = random.randint(0, 99)

        if not processo.interrompido:   # Se não houver interrupções executa normalmente
            ######## Imprime contexto do processo #########
            processo_atual = "Processo Principal"
            painel_processo = Panel(
                f"Executando: [bold green]{processo_atual}[/bold green]\n\n[bold yellow]Tempo de Execução:[/bold yellow] {processo.tempo}\n[bold yellow]PC:[/bold yellow] {hex(processo.pc)}\n[bold yellow]Pilha:[/bold yellow] {hex(processo.ponteiro_pilha)}",
                title="Processo Atual",
                border_style="blue",
                width=80,
                padding=(1, 2),
                style="bold cyan"
            )
            console.print(Panel.fit(painel_processo, title="Sistema Operacional", border_style="blue"))
            ######## Imprime contexto do processo #########

            processo.executa()
        else:                       # Se houver, tratam-se as interrupções
            
            os.tratar_interrupcao()

        if chance_de_nova_interrupcao < 14:    # 15% de criar uma nova interrupção
            if not processo.interrompido:
                os.salva_contexto(processo)
                processo.interrompe()

            os.adicionar_na_fila_de_interrupcoes(Interrupcao.Interrupcao())

        if(len(os.fila_de_interrupcoes) == 0):
            processo.retomar(os.tempo_salvo, os.pc_salvo, os.ponteiro_pilha_salvo)

        input()