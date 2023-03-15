# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Y5b-FxZS-47vO4JIu7zqaopiQNrKiyZ
"""

import numpy as np
import pandas as pd

"""**CARREGANDO O CONJUNTO DE DADOS EM UM QUADRO DE DADOS USANDO O PANDAS**

"""

#@title
df=pd.read_csv('agricultural_raw_material.csv')

"""**EXPLORANDO O CONJUNTO DE DADOS**"""

df.info

#checando se ele não é nulo
df.isnull().sum()

"""**TRATANDO DADOS NULOS, INCORRETOS E INVALIDOS**

"""

#subistituindo %, "," e "-"
df = df.replace("%",'',regex=True)
df = df.replace(",",'',regex=True)
df = df.replace("-",'',regex=True)
df = df.replace('',np.nan)
df = df.replace("MAY90",np.nan)
#Retirando os valores nulos
df = df.dropna()
#Checando se os valores nulos foram realmente tratados
df.isnull().sum()
#convertendo o tipo de dados para float
lst = ["Coarse wool Price","Coarse wool price % Change","Copra Price","Copra price % Change","Cotton Price","Cotton price % Change", "Fine wool Price","Fine wool price % Change","Hard log Price","Hard log price % Change","Hard sawnwood Price","Hard sawnwood price % Change","Hide Price","Hide price % change","Plywood Price","Plywood price % Change","Rubber Price","Rubber price % Change","Softlog Price","Softlog price % Change","Soft sawnwood Price","Soft sawnwood price % Change","Wood pulp Price","Wood pulp price % Change"]
df[lst] = df[lst].apply(pd.to_numeric, errors='coerce')
#verificando se deu tudo certo na troca de tipos
df.dtypes

#top 5 colunas dentro do dataframe
df.head()

#Transformando a coluna MONTH em dataTime e defenindo-a como indice p ara o conjunto de dados
df.Month = pd.to_datetime(df.Month, format='%b%y', yearfirst=False)

df.head()

"""***ANÁLISE EXPLORATÓRIA***"""

# Commented out IPython magic to ensure Python compatibility.
#importando as duas bibliotecas mais utilizadas para visualização de gráfico em PYTHON:
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] =14
matplotlib.rcParams['figure.figsize'] = (9,5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

#lista de matérias-primas ou raw-materials list/ quanto mais alto o preço de uma mais facil ter uma relação de aumento nas outras
raw_data=['Coarse wool Price','Copra Price','Cotton Price','Fine wool Price','Hard log Price','Hard sawnwood Price','Hide Price','Plywood Price','Rubber Price','Softlog Price','Soft sawnwood Price','Wood pulp Price']
#mostrando a relação na matriz com o mapa de calor.
corrmat = df[raw_data].corr()
#setando o tamanho do plot
fig = plt.figure(figsize = (12,9))
mask = np.triu(np.ones_like(corrmat, dtype=bool))
sns.heatmap(corrmat, vmax= .8,mask=mask, square = True, annot = True)
plt.show

#Não há relações de significancia no percentual de variação (quantidade no mercado)
plt.figure(figsize=(30,15))
changeList = ['Coarse wool price % Change','Copra price % Change','Cotton price % Change','Fine wool price % Change','Hard log price % Change','Hard sawnwood price % Change','Hide price % change','Plywood price % Change','Rubber price % Change','Softlog price % Change','Soft sawnwood price % Change','Wood pulp price % Change']
#Gerar uma matriz de correlação para todo o conjunto de dados
corrMatrix = df[changeList].corr()
sns.heatmap(corrMatrix, annot=True)
plt.show

""" 

*  O valor negativo afirma que duas variaveis estão negativamente correlacionadas (um aumenta e o outro decrementa)
*   Zero implica nenhuma relação

*   caso contrário, maior o valor maior a chance de relação, preço e sus graficos de % de mudança



"""

#Variação do preço da Lã grossa
axes=df[["Coarse wool Price", "Coarse wool price % Change"]].plot(figsize=(11,9), subplots=True, linewidth=1)

changeList = ['Coarse wool price % Change','Copra price % Change','Cotton price % Change','Fine wool price % Change','Hard log price % Change','Hard sawnwood price % Change','Hide price % change','Plywood price % Change','Rubber price % Change','Softlog price % Change','Soft sawnwood price % Change','Wood pulp price % Change']
for i in range(len(changeList)):
  plt.figure(figsize=(12,12))
  df[changeList[i]].hist(figsize=(11,9),linewidth =1)
  plt.xlabel('% Change')# Preço
  plt.ylabel('count')#Quantidade
  plt.legend(changeList[i:],loc='upper center',bbox_to_anchor=(1.2,1))

#Encontrando a materia prima que tem o menor preço ao longo dos anos
plt.figure(figsize=(10,10))
listaDeMaterial=['Coarse wool Price','Copra Price','Cotton Price','Fine wool Price','Hard log Price','Hard sawnwood Price','Hide Price','Plywood Price','Rubber Price','Softlog Price','Soft sawnwood Price','Wood pulp Price']
for i in range(len(listaDeMaterial)):
    plt.subplot(4,3, i+1)
    plt.subplots_adjust(hspace=1, wspace=0.5)
    plt.title(listaDeMaterial[i])
    plt.plot(df[listaDeMaterial[i]])
    plt.xticks(rotation=90)
plt.suptitle("Comparação de preço das materias primas")

#comparando borracha e algodão 
plt.figure(figsize=(10,10))
plt.plot(df[["Cotton Price","Rubber Price"]])
plt.title("Comparação de preço de materias primas")
plt.xlabel("Anos")
plt.ylabel("Preços")
plt.legend(["Cotton Price","Rubber Price"],loc='upper center',bbox_to_anchor=(1.2,1))