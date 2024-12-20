# Sobre

O **Interrupt-simulator** é um simulador de e/s com interrupções em um sistema operacional. A entrada/saída com interrupções é um mecanismo utilizado em sistemas operacionais para gerenciar dispositivos de E/S de forma eficiente, evitando que o processador fique ocioso aguardando a conclusão de operações de entrada ou saída.

O processador solicita uma operação de E/S (como leitura ou gravação) para um dispositivo.
Em vez de esperar o dispositivo concluir a operação, o processador continua executando outras tarefas. Quando o dispositivo finaliza a operação de E/S, ele gera uma interrupção que notifica o processador. O processador pausa momentaneamente sua tarefa atual, trata a interrupção (processa os dados ou confirma o término da operação) e depois retorna à tarefa anterior.

Esse processo garante:
+ Eficiência.
+ Resposta Rápida.
+ Permite multitarefa.


# Pré-requisitos e instalação

O sistema é desenvolvido na linguagem __python__, que pode ser feito o download [aqui](https://www.python.org/downloads/). O simulador pode ser visualizado [aqui](https://github.com/Y4ngfr/Interrupt-simulator)

Primeiramente deve ser clonado o repositório do projeto com o comando:

```$
git clone https://github.com/Y4ngfr/Interrupt-simulator.git
```

Com repositório clonado instale as dependências (é obrigatório o pacote estar instalado):
```Bash
pip install -r ./requirements.txt
```

Acesse a pasta do projeto e execute o arquivo main.py:

```$
python3 src/main.py
```

# Funcionamento do Simulador

A cada passo da simulação, o programa realiza as seguintes operações:

+ Cria o processo principal (que estará executando sempre no programa).
+ Enquanto executa, verifica se ocorreu uma interrupção (há 15% de chance de ocorrer uma interrupção).
+ Caso ocorra uma interrupção, coloca a interrupção na fila de interrupções (de acordo com a prioridade).
+ Salva o contexto do processo principal e o interrompe.
+ Trata as interrupções da fila (é possível que cheguem novas interrupções).
+ Retoma o contexto do processo principal e continua a execução.

# Arquitetura do Sistema

A arquitetura do simulador é composta pelas seguintes classes: ``Interrupcao``, ``OS`` e ``Processo``, cada uma com responsabilidades específicas que contribuem para o funcionamento do programa.

## Interrupcao

Classe responsável por modelar as interrupções do sistema. Ela define o dispositivo que gerou a interrupção, sua prioridade na fila de interrupções, o tipo de interrupção e o ocorrido.

## OS

A classe ``OS`` gerencia o controle e o fluxo de execução do sistema operacional. Ela é responsável por tratar as interrupções, gerenciar a fila de interrupções e salvar o contexto do processo afetado.

## Processo

A classe ``Processo`` modela os processos sendo simulados. Ela gerencia o ciclo de vida de cada processo, incluindo sua execução, interrupção e retomada.

# Cenários de Testes

O simulador possui alguns cenário possíveis durante a sua execução:

## Execução Contínua do Processo

A execução normal do processo principal sem interrupções. Nesse caso o processo é executado continuamente, incrementando e simulando os valores de tempo, pc e ponteiro para pilha.

## Geração de Interrupções

A chance de gerar uma interrupção é de 15%, nesse caso ocorrem as seguintes ações:

+ A interrupção é registrada no log.
+ O contexto do processo é salvo.
+ A interrupção é adicionada na fila de interrupções.

## Tratamento de Interrupções

As interrupções na fila são tratadas pelo sistema operacional. Quando uma nova interrupção chega, é possível que ela possua uma prioridade maior do que uma interrupção que esteja sendo tratada no mesmo instante. Nesse caso, o sistema operacional passa o tratamento para a interrupção de maior prioridade.

## Retomada do Processo Principal

O processo principal é retomado após o tratamento das interrupções. Isso ocorre quando a fila de interrupções está totalmente vazia, nesse caso os valores de tempo, pc e ponteiro da pilha do processo principal são retomados.