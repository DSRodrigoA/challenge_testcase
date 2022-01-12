#!/usr/bin/env python
# coding: utf-8

# # Segundo Entregável - Transformação de arquivos Json para modelo Relacional

# In[15]:


# Bibliotecas utilizadas

import pandas as pd
import json
from pandas.io.json import json_normalize # Função de normalizalção do pandas
import numpy as np
import openpyxl


# ## 01. Carga de Dados

# In[2]:


# Carga local do arquivo json disponibilizado pela documentação

df = pd.read_json('C:/DataScience/L3/Artifact3/data/data.json')


# ## 02. Compreensão do Dataframe

# In[3]:


# Listagem das colunas do dataframe
list(df)


# In[4]:


# Visualização do dataframe criado, utilizando a biblioteca 'pandas'.

df


# ## 03. Engineering

# ### 03.01 - Dataframe 01 - Expansão da lista de dicionários

# In[5]:


# Aqui, podemos observar que temos uma lista de jsons, ou "nested jsons", deivo ao campo 'ItemList' conter uma lista
# de dicionários. Para resolver esta questão, utilizamos a função 'explode' para retirar os dicionários das listas e 
# colocar em relacionamento. Assim, teremos um dicionário respectivo a cada index, respeitando o modelo relacional.

df_exploded = df.explode(['ItemList'])
df_exploded


# ### 03-02. Dataframe 02 - Normalização do Dataframe 

# In[6]:


# Por final, utilizamos a função do pandas 'json_normalize' para normalizar os dicionários. Esta função, traz as chaves como 
# colunas do dataframe e mantém os respectivos valores, distribuindo todos os níveis do json ao longo do dataframe.

df_flatt = pd.json_normalize(json.loads(df_exploded.to_json(orient='records')))

df_flatt


# In[7]:


df_flatt


# ## 04. Exportando o Dataframe

# In[25]:


writer = pd.ExcelWriter('df_normalizado.xlsx', engine = 'xlsxwriter')
df_flatt.to_excel(writer, 'sheet1', index = False)
writer.save()
writer.close()


# ### Assim, concluímos a ingestão e normalização de arquivos json de forma relacional, possibilitando o direcionamento para pipelines de dados e ferramentas de visualização.

# # Fim
