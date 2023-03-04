import json

with open('dados.json') as file:
    faturamento = json.load(file)

valores = []
for dia in faturamento:
    if dia['valor'] > 0:
        valores.append(dia['valor'])


menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = 0
for valor in valores:
    if valor > media_mensal:
        dias_acima_da_media += 1

print(f'Menor valor de faturamento: R${menor_valor:.2f}')
print(f'Maior valor de faturamento: R${maior_valor:.2f}')
print(f'{dias_acima_da_media} dias tiveram faturamento acima da média mensal de R${media_mensal:.2f}')

