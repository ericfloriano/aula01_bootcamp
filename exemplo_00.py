#Programa que o usuário digite 2 valores e depois apareça a soma

def obter_primeiro_numero():
    try:
        return int(input("Digite o primeiro número: "))
    except ValueError:
        print("Entrada inválida para o primeiro número.")
        # Se não retornar nada, a função retorna None por padrão

def obter_segundo_numero():
    try:
        return int(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida para o segundo número.")
        # Se não retornar nada, a função retorna None por padrão

primeiro_numero = obter_primeiro_numero()
segundo_numero = obter_segundo_numero()

resultado = primeiro_numero + segundo_numero
print(f"A soma é: {resultado}")