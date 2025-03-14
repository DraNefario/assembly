# Implementação de CPU e ULA

## Descrição

Este projeto foi desenvolvido como parte da disciplina de Performance em Sistemas Ciberfísicos, ministrada pelo professor Eduardo Kugler Viegas, na turma 3B de Ciência da Computação.

Este projeto consiste na implementação de uma CPU com uma Unidade de Controle, uma ULA e uma Memória Cache em nível de software utilizando Python. A CPU suporta um conjunto de instruções (ISA) e possui cinco registradores, além de uma Flag Zero (ZF) para comparação de valores.

## Estrutura da CPU

### Registradores

A CPU possui os seguintes registradores:

| Registrador | ID   | Descrição                           |
| ----------- | ---- | ----------------------------------- |
| CP          | 0x01 | Registrador de ponteiro de programa |
| AX          | 0x02 | Registrador de propósito geral      |
| BX          | 0x03 | Registrador de propósito geral      |
| CX          | 0x04 | Registrador de propósito geral      |
| DX          | 0x05 | Registrador de propósito geral      |

### Conjunto de Instruções (ISA)

A CPU implementa as seguintes instruções:

| #  | Instrução     | OPCode | Descrição                                 |
| -- | ------------- | ------ | ----------------------------------------- |
| 0  | ADD Reg, Byte | 0x00   | Soma um valor a um registrador            |
| 1  | ADD Reg, Reg  | 0x01   | Soma dois registradores                   |
| 2  | INC Reg       | 0x10   | Incrementa o valor de um registrador      |
| 3  | DEC Reg       | 0x20   | Decrementa o valor de um registrador      |
| 4  | SUB Reg, Byte | 0x30   | Subtrai um valor de um registrador        |
| 5  | SUB Reg, Reg  | 0x31   | Subtrai um registrador de outro           |
| 6  | MOV Reg, Byte | 0x40   | Move um valor para um registrador         |
| 7  | MOV Reg, Reg  | 0x41   | Move o valor de um registrador para outro |
| 8  | JMP Byte      | 0x50   | Salta para um endereço específico         |
| 9  | CMP Reg, Byte | 0x60   | Compara um registrador com um valor       |
| 10 | CMP Reg, Reg  | 0x61   | Compara dois registradores                |
| 11 | JZ Byte       | 0x79   | Salta se a Flag Zero for 1                |

## Funcionalidades Implementadas

O projeto inclui a implementação das seguintes funções:

1. **Buscar e Decodificar Instrução**
   - Retorna o ID da instrução a ser executada e exibe a instrução no terminal caso `CPU_DEBUG` seja verdadeiro.
2. **Calcular Próxima Instrução**
   - Atualiza o valor do contador de programa (CP) conforme a instrução corrente.
3. **Ler Operadores e Executar Instrução**
   - Executa a instrução recebida e exibe informações de debug caso `CPU_DEBUG` esteja ativado.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o script principal para testar a execução das instruções.
3. Utilize testes de mesa para validar a execução correta das instruções e o comportamento dos registradores.

## Autor

Thomas Manussadjian Steinhausser

