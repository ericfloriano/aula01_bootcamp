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