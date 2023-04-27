# Solicita ao usuário que digite um número e armazena em uma variável num
num = int(input("Digite um número: "))

# Define as duas primeiras variáveis da sequência de Fibonacci
fib1, fib2 = 0, 1

# Define uma variável booleana pertence, que será utilizada para indicar se o número pertence à sequência
pertence = False

# Loop while que realiza a busca binária no array
while fib2 <= num:
    # Verifica se o número atual na sequência de Fibonacci é igual ao número inserido
    if fib2 == num:
        # Caso seja, define a variável pertence como True e encerra o loop
        pertence = True
        break
    # Avança para o próximo número na sequência de Fibonacci
    fib1, fib2 = fib2, fib1 + fib2

# Inicializa uma lista de Fibonacci com os dois primeiros termos da sequência
fibonacci = [0, 1]

# Loop while que adiciona os termos da sequência até que o último seja maior ou igual ao número inserido
while fibonacci[-1] < num:
    # Adiciona um novo termo à lista, que é a soma dos dois últimos termos
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Imprime a lista de Fibonacci até o número inserido
print(f"A sequência de Fibonacci até o número {num} é: {fibonacci[:-1]}")

# Verifica se o número inserido pertence à sequência de Fibonacci e imprime o resultado
if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
