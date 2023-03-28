import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


# inicialização das variáveis
if dados[0]["valor"] != 0:
    maior = dados[0]["valor"]
    menor = dados[0]["valor"]

soma = 0
quant = 0

# cálculo do maior, menor e soma para o cálculo da média
for dia in dados:
    valor = dia["valor"]
    if valor != 0:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        soma += valor
        quant += 1

media = soma / quant

#verificação da quantidade de dias em que o valor do faturamneto foi maior que a media
dias = 0
for dia in dados:
    if dia['valor'] > media:
        dias += 1


print("Maior valor de faturamento: ", maior)
print("Menor valor de faturamento: ", menor)
print("Média faturamento: ", media)
print("Número de dias com faturamento acima da média: ", dias)


