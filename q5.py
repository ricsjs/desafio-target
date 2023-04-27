# lê a string do usuário
string = input("Digite uma string: ")

# inicializa uma nova string vazia para armazenar a string invertida
string_invertida = ""

# percorre a string de trás para frente, adicionando cada caractere à nova string
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# imprime a string invertida
print("A string invertida é:", string_invertida)
