import pandas as pd
import os

os.system ("cls")

dados = {
    "Cargos": ["assistente", "auxiliar", "gerente"],
    "Salarios": [2500,1800,750]
}

print (dados)

print (30*"-")

df = pd.DataFrame(dados)
print (df)

print (30*"-")

# df = pd.Series(dados["Cargos"])
# print (dados_cargos)

# print (30*"-")

# dados_salarios = pd.Series(dados["Salarios"])
# print (dados_salarios)

# print (30*"-")

# # Índices e Valores
# print (dados_cargos.index)

# print (30*"-")

# # Printar os valores
# print(dados_cargos.values)

# print (30*"-")

# Imprime a linha do índice
df_linha = df.iloc[1][:"Cargos"]
print (df_linha)

# Criando Índices Textuais

df.index = ["A", "B", "C"]

serie_colunas = df.loc["A"]

# print (serie_colunas, "\n")

# print (30*"-")

# print (df.iloc[1]['Cargos'])


# iloc para localizar por índices
print (serie_cargos.iloc[0])
