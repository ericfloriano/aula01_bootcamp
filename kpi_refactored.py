# Constante para o valor base do bônus
VALOR_BASE_BONUS = 1000

def obter_nome_usuario():
    """Solicita e retorna o nome do usuário."""
    return input("Digite seu nome: ")

def obter_salario_usuario():
    """Solicita e retorna o salário mensal do usuário, com tratamento de erro."""
    while True:
        try:
            salario = float(input("Digite o valor do seu salário mensal: "))
            return salario
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o salário.")

def obter_bonus_percentual_usuario():
    """Solicita e retorna a porcentagem do bônus, com tratamento de erro."""
    while True:
        try:
            bonus_percentual = float(input("Digite a porcentagem do bônus recebido: "))
            return bonus_percentual
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a porcentagem do bônus.")

def calcular_kpi_bonus(salario, bonus_percentual):
    """Calcula o KPI do bônus."""
    return VALOR_BASE_BONUS + salario * bonus_percentual

def exibir_resultado(nome, kpi_bonus):
    """Exibe a mensagem de saudação com o valor do bônus formatado."""
    print(f"Olá {nome}, o seu bônus foi de {kpi_bonus:.0f}")

def main():
    """Função principal para executar o programa."""
    nome = obter_nome_usuario()
    salario = obter_salario_usuario()
    bonus_percentual = obter_bonus_percentual_usuario()
    kpi_bonus = calcular_kpi_bonus(salario, bonus_percentual)
    exibir_resultado(nome, kpi_bonus)

if __name__ == "__main__":
    main()