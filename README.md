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

+ Gera um processo.
+ Executa o processo até a finalização.
+ Enquanto executa, verifica se ocorreu uma interrupção.
+ Caso ocorra uma interrupção, trata-a e retorna ao fluxo de execução.

# Arquitetura do Sistema

A arquitetura do simulador é composta pelas seguintes classes: ``Interrupcao``, ``OS`` e ``Processo``, cada uma com responsabilidades específicas que contribuem para o funcionamento 

## Interrupcao

Classe responsável por modelar as interrupções do sistema. Ela define o dispositivo que gerou a interrupção, sua prioridade na fila de interrupções, o tipo de interrupção e o ocorrido.

## OS

A classe ``OS`` gerencia o controle e o fluxo de execução do sistema operacional. Ela é responsável por tratar as interrupções, gerenciar a fila de interrupções e salvar o contexto do processo afetado.

## Processo

A classe ``Processo`` modela os processos sendo simulados. Ela gerencia o ciclo de vida de cada processo, incluindo sua execução, interrupção e retomada.