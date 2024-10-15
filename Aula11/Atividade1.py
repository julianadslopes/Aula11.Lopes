import pandas as pd 

# Criar um df de 3 colunas: nome do filme, gênero e ano de lançamento

filmes = {
    "título" : ["A Bela e a Fera", "Alien", "O Poderoso Chefão"],
    "gênero" : ["Desenho", "Terror", "Crime"],
    "ano" : ["1991", "1979", "1972" ]
}

# print(filmes)

df = pd.DataFrame(filmes)

print (" Data Frame completo")
print (df)

print ( "--------")

# Imprime a terceira linha do índice
df_linha = df.iloc[2]
print ("TERCEIRA LINHA")
print (df_linha, "\n")

print (30* "-")

# Imprime a coluna
df_titulo = df["título"]
print  ("NOMES DOS FILMES")
print (df_titulo, "\n")

print (30* "-")

# Filtrar dados
df_alien = df[df["título"]== "Alien"]

print("FILME ALIEN")
print (df_alien, "\n")

print (30* "-")

df_desenho = df[df["gênero"]== "Desenho"]

print ("FILME DE DESENHO")
print (df_desenho, "\n")