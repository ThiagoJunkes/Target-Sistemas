string_original = input("Digite uma string para ser invertida: ")

# Inverter a string
string_invertida = ""
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

print("A string invertida é:", string_invertida)
