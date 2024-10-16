import pandas as pd

import os
os.system("cls")

try:
    df = pd.read_csv("ClassicDisco.csv", sep= ',', encoding='utf-8')

    # print(df)
    # print (df.to_string)
    # print (df.head(10))
    # print (df.tail(10))
    # print (df.info())
    # print (df.describe())
    # pd.set_option ("display.min_rows", 20)
    # popularidade = df[df["Popularity"]>20]
    # print(popularidade[["Track", "Popularity"]])
    # michael_jackson = df[df["Artist"] == "Michael Jackson"]
    # print(michael_jackson[["Album", "Artist", "Track"]])
    # pd.set_option ('display.max_columns', None)
    # print(df)
    # df.to_csv("Base_modificada.csv", index=False, sep=",", encoding = "utf-8")
    # df.to_excel("Base_modificada.xls", index=False, engine="openpyxl")
  
except Exception as e:
    print (f"Erro {e}")



# # IMPRIMINDO AS 5 PRIMEIRAS LINHAS
# print (df.head())

# # IMPRIMINDO AS 10 PRIMEIRAS LINHAS
# print (df.head(10))

# # IMPRIMINDO AS 5 ÚLTIMAS LINHAS
# print (df.tail())

# # IMPRIMINDO INFORMAÇÕES DA BASE DE DADOS
# print (df.info())

# # IMPRIMINDO RESUMO DOS DADOS
# print (df.describe())
    
# # SALVANDO UM CSV
# df("Base_modificada.csv", index=False, sep=",", encoding = "utf-8")    