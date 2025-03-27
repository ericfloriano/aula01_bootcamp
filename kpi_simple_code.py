nome = input("Digire seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus_percentual = float(input("Digite a porcentagem do bônus: "))

kpi_bonus = 1000 + salario * bonus_percentual

print(f"Olá {nome}, o seu bônus foi de {kpi_bonus:.0f}")