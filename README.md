# Calculadora de KPI de Bônus (Refatorado)

Este programa em Python solicita ao usuário o nome, salário mensal e a porcentagem do bônus recebido para calcular e exibir o valor do bônus, utilizando uma fórmula específica. Esta versão do código foi refatorada para melhor organização, legibilidade e robustez.

## Funcionalidades

* Solicita o nome do usuário.
* Solicita o salário mensal do usuário, garantindo que a entrada seja um número válido através de tratamento de erros.
* Solicita a porcentagem do bônus recebido pelo usuário, garantindo que a entrada seja um número válido através de tratamento de erros.
* Calcula o KPI do bônus utilizando a fórmula: `1000 + salario * bônus`.
* Exibe uma mensagem de saudação com o nome do usuário e o valor calculado do bônus formatado.
* Utiliza funções para modularizar o código, tornando-o mais organizado e fácil de entender.
* Inclui tratamento de erros para garantir que as entradas de salário e bônus sejam números, melhorando a experiência do usuário.
* Define uma constante para o valor base do bônus, facilitando a manutenção.

## Explicação Detalhada do Código

* **`VALOR_BASE_BONUS = 1000`**: Define uma constante para o valor base que é adicionado ao cálculo do bônus. Usar constantes torna o código mais fácil de entender e manter.

* **`def obter_nome_usuario():`**:
    * Esta função não recebe argumentos.
    * Utiliza a função `input()` para solicitar que o usuário digite seu nome.
    * Retorna o nome digitado pelo usuário.
    * A docstring (`"""Solicita e retorna o nome do usuário."""`) explica o propósito da função.

* **`def obter_salario_usuario():`**:
    * Esta função não recebe argumentos.
    * Entra em um loop `while True` que continuará até que um salário válido seja inserido.
    * Dentro do bloco `try`, tenta converter a entrada do usuário para um número de ponto flutuante (`float`).
    * Se a conversão for bem-sucedida, a função retorna o valor do salário.
    * Se a conversão falhar (ou seja, o usuário digitou algo que não é um número), o bloco `except ValueError` é executado, exibindo uma mensagem de erro e o loop continua.
    * A docstring explica o propósito da função e seu tratamento de erros.

* **`def obter_bonus_percentual_usuario():`**:
    * Similar à função `obter_salario_usuario()`, esta função solicita a porcentagem do bônus e garante que a entrada seja um número de ponto flutuante usando tratamento de erros (`try-except`).
    * Retorna a porcentagem do bônus digitada pelo usuário.
    * A docstring explica o propósito da função e seu tratamento de erros.

* **`def calcular_kpi_bonus(salario, bonus_percentual):`**:
    * Recebe o `salario` e a `bonus_percentual` como argumentos.
    * Calcula o KPI do bônus usando a fórmula `VALOR_BASE_BONUS + salario * bonus_percentual`.
    * Retorna o valor calculado do KPI do bônus.
    * A docstring explica o propósito da função.

* **`def exibir_resultado(nome, kpi_bonus):`**:
    * Recebe o `nome` do usuário e o `kpi_bonus` calculado como argumentos.
    * Utiliza um f-string para formatar a mensagem de saudação, incluindo o nome do usuário e o valor do bônus formatado como um número inteiro (`:.0f`).
    * Imprime a mensagem formatada no console.
    * A docstring explica o propósito da função.

* **`def main():`**:
    * Esta função é a principal do programa e coordena a execução das outras funções.
    * Chama `obter_nome_usuario()` para obter o nome do usuário.
    * Chama `obter_salario_usuario()` para obter o salário do usuário.
    * Chama `obter_bonus_percentual_usuario()` para obter a porcentagem do bônus.
    * Chama `calcular_kpi_bonus()` para calcular o valor do bônus, passando o salário e a porcentagem obtidos.
    * Chama `exibir_resultado()` para mostrar a mensagem final ao usuário.
    * A docstring explica o propósito da função.

* **`if __name__ == "__main__":`**:
    * Esta é uma construção comum em Python. O código dentro deste bloco só será executado quando o script é executado diretamente (por exemplo, usando `python kpi_refactored.py`).
    * Neste caso, ele chama a função `main()` para iniciar a execução do programa. Isso permite que o código dentro de `main()` seja executado, e se este script fosse importado como um módulo em outro script, a função `main()` não seria executada automaticamente.

## Como Executar

1.  Certifique-se de que o Python esteja instalado no seu sistema. Você pode verificar se o Python está instalado abrindo o terminal ou prompt de comando e digitando:
    ```bash
    python --version
    ```
    Se o Python não estiver instalado, você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  Salve o script Python como `kpi_refactored.py`.

3.  Abra o terminal ou prompt de comando.

4.  Navegue até o diretório onde você salvou o arquivo `kpi_refactored.py` utilizando o comando `cd`:
    ```bash
    cd /caminho/para/seu/diretorio
    ```
    (Substitua `/caminho/para/seu/diretorio` pelo caminho real do diretório).

5.  Execute o programa utilizando o seguinte comando:
    ```bash
    python kpi_refactored.py
    ```

6.  O programa solicitará que você insira seu nome, salário e a porcentagem do bônus. Digite as informações solicitadas e pressione Enter após cada entrada. Se você inserir um valor inválido para o salário ou bônus (algo que não seja um número), o programa exibirá uma mensagem de erro e pedirá para você inserir novamente.

7.  O programa exibirá uma mensagem com seu nome e o valor calculado do bônus.

## Exemplo de Uso

```bash
python kpi_refactored.py
Digite seu nome: Eric
Digite o valor do seu salário mensal: 5000
Digite a porcentagem do bônus recebido: 1.5
Olá Eric, o seu bônus foi de 8500
```