import random


class Interrupcao:
    def __init__(self) -> None:
        teclas_precionadas = ['A']
        for i in range(0, random.randint(0, 10)):
            teclas_precionadas.append(chr(random.randint(65, 90)))

        escolha_aleatoria = random.choice([
            {
                "dispositivo": "teclado", "prioridade": 1,
                "acoes": [{"tipo": "Entrada", "ocorrido": f"As teclas \"{''.join(teclas_precionadas)}\" foram precionadas"}]
            },
            {
                "dispositivo": "disco", "prioridade": 3,
                "acoes": [{"tipo": "entrada", "ocorrido": f"Um dado foi lido."}, {"tipo": "saida", "ocorrido": "Um arquivo foi gravado."}]
            },
            {
                "dispositivo": "monitor", "prioridade": 3,
                "acoes": [{"tipo": "saida", "ocorrido":f"Foi mostrado \"{''.join(teclas_precionadas)}\""}]
            },
        ])
        
        self.dispositivo = escolha_aleatoria["dispositivo"]
        self.prioridade = escolha_aleatoria["prioridade"]
        self.tipo = escolha_aleatoria["acoes"][random.randint(0, len(escolha_aleatoria["acoes"])-1)]
        self.tempo_execucao = random.randint(1, 7)
