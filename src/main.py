from models.Processo import Processo
from models.Interrupcao import Interrupcao
from models.OS import OS

from rich.console import Console
from rich.panel import Panel

import random
import signal
import time
import logging

def handle_sigint(signum, frame):
        console.log("\nEncerrando sistema...")
        a = console.export_text(clear=True, styles=False)
        
        with open(f"./logs/log{time.time().as_integer_ratio()[0]}.txt", "w", encoding="UTF-8") as file:
             file.write(a)
        exit(0)

if __name__ == "__main__":
    console = Console(record=True)
    processo = Processo.Processo()
    OS = OS.OS()

    signal.signal(signal.SIGINT, handle_sigint)

    ######## Imprime contexto do processo #########
    processo_atual = "Processo Principal"
    painel_processo = Panel(
        f"""Executando: [bold green]{processo_atual}[/bold green]\n\n[bold yellow]Tempo de Execução:[/bold yellow] {processo.tempo}\n[bold yellow]PC:[/bold yellow] {hex(processo.pc)}\n[bold yellow]Pilha:[/bold yellow] {hex(processo.ponteiro_pilha)}""",
        title="Processo Atual",
        border_style="blue",
        width=80,
        padding=(1, 2),
        style="bold cyan"
    )
    console.print(Panel.fit(painel_processo, title="Sistema Operacional", border_style="blue"))
    ######## Imprime contexto do processo #########
    
    input()

    while True:
        chance_de_nova_interrupcao = random.randint(0, 99)

        console.log("Gerando painel...")
        
        if chance_de_nova_interrupcao < 14:    # 15% de criar uma nova interrupção
            console.log(f"[bold yellow]! Nova interrupção ![/bold yellow]")
            if not processo.interrompido:
                console.log(f"[green] Contexto salvo pelo sistema operacional: tempo de execução = {processo.tempo}, pc = {hex(processo.pc)}, ponteiro da pilha = {hex(processo.ponteiro_pilha)}[/green]")
                OS.salva_contexto(processo)
                processo.interrompe()

            OS.adicionar_na_fila_de_interrupcoes(Interrupcao.Interrupcao())
        
        if not processo.interrompido:   # Se não houver interrupções executa normalmente
            processo.executa()

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


        else:                       # Se houver, tratam-se as interrupções
            interrupcao = OS.fila_de_interrupcoes[0]
            ######## Imprime interrupção sendo tratada #########
            interrupcao_atual = f"Interrupção - {interrupcao.dispositivo}"
            painel_interrupcao = Panel(
                f"Tratando [bold yellow]{interrupcao_atual}[/bold yellow]\n\n[bold red]Tipo:[/bold red] {interrupcao.tipo["tipo"]}\n[bold red]Ocorrido:[/bold red] {interrupcao.tipo["ocorrido"]}\n[bold red]Tempo de Execução Restante:[/bold red] {interrupcao.tempo_execucao}\n[bold red]Prioridade:[/bold red] {interrupcao.prioridade}",
                title="Tratamento Interrução",
                border_style="yellow",
                width=80,
                padding=(1, 2),
                style="bold yellow"
            )
            console.print(Panel.fit(painel_interrupcao, title="Sistema Operacional", border_style="blue"))
            ######## Imprime interrupção sendo tratada #########

            OS.tratar_interrupcao()


        if(len(OS.fila_de_interrupcoes) == 0 and processo.interrompido == True):
            processo.retomar(OS.tempo_salvo, OS.pc_salvo, OS.ponteiro_pilha_salvo)

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

        input()
