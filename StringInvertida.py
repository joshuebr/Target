#String Invertida


string = input("Informe uma string: ")

tamanho = len(string)
string_invertida = ""

for i in range(tamanho-1, -1, -1):
    string_invertida += string[i]

print(f"A string invertida é: {string_invertida}")
