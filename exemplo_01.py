# Programa que retorna o número de caracteres

def contar_caracteres_nome():
  """Solicita o nome do usuário e retorna o número de caracteres."""
  nome = input("Digite seu nome: ")
  return len(nome)

# Chama a função e imprime o resultado
numero_caracteres = contar_caracteres_nome()
print(numero_caracteres)