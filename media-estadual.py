faturamento_estados = {'SP': 67836.43,
                       'RJ': 36678.66,
                       'MG': 29229.88,
                       'ES': 27165.48,
                       'Outros': 19849.53}

print("Valor de faturamento mensal por estado:")
for estado, valor in faturamento_estados.items():
    print(f"{estado} - R${valor}")

valor_total_mensal = sum(faturamento_estados.values())

percentuais = {}
for estado, valor in faturamento_estados.items():
    percentuais[estado] = valor / valor_total_mensal * 100

print()
print("Percentual de vendas: ")
for estado, percentual in percentuais.items():
    print(f"{estado} - {percentual:.2f}%")
