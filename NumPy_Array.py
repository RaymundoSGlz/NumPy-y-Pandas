# %% [markdown]
# # NumPy
# 
# 
# ## Indice:
# * [Array](#Array)
# * * [Slicing](#Slicing)

# %%
import numpy as np

# %% [markdown]
# ## Array
# El array es el principal objeto de la librería. Representa datos de manera estructurada y se puede acceder a ellos a través del indexado, a un dato específico o un grupo de muchos datos específicos.

# %%
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista

# %% [markdown]
# Convertimos nuestra lista en un array

# %%
arr = np.array(lista)
arr

# %% [markdown]
# Una matriz son varios Vectores o listas agrupadas una encima de la otra

# %%
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
matriz

# %% [markdown]
# El indexado nos permite acceder a los elementos de los array y matrices
# Los elementos se empiezan a contar desde 0.
# 
# | Index    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
# |----------|---|---|---|---|---|---|---|---|---|
# | Elemento | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
# 
# Es posible operar directamente con los elementos.

# %%
arr[0] + arr[5]

# %% [markdown]
# En el caso de las matrices, al indexar una posición se regresa el array de dicha posición.

# %%
matriz[0]

# %% [markdown]
# | Index | 0 | 1 | 2 |
# |-------|---|---|---|
# | 0     | 1 | 2 | 3 |
# | 1     | 4 | 5 | 6 |
# | 2     | 7 | 8 | 9 |
# 
# Para seleccionar un solo elemento de la matriz se especifica la posición del elemento separada por comas.
# 
# Donde el primer elemento selecciona las filas, el segundo elemento las columnas

# %%
matriz[0][2]

# %% [markdown]
# ### Slicing
# 
# Nos permite extraer varios datos, tiene un comienzo y un final.

# %%
arr[2:6]

# %% [markdown]
# Si no agregamos el **primer indice**, se tomara como inicio el 0

# %%
arr[:4]

# %% [markdown]
# Si no agregamos el **segundo indice**, se tomara como final el ultimo elemento

# %%
arr[5:]

# %% [markdown]
# Podemos utilizar un tercer indice, para poder indicar **los pasos**
# 
# Para recorrer todo el array de dos en dos

# %%
arr[::2]

# %% [markdown]
# *Podemos también recorrer los elementos de derecha a izquierda utilizando indices negativos*

# %%
arr[-5:-2]

# %% [markdown]
# De manera muy similar podemos trabajar con matrices

# %%
matriz[1:]

# %% [markdown]
# Para trabajar con filas y columnas especificas

# %%
matriz[1:,:2]


