# %%
import numpy as np

# %% [markdown]
# ## Dimensiones

# %% [markdown]
# Cuando trabajamos con datos es común encontrarlos agrupados de formas distintas, podemos entonces describir estos acomodos como dimensiones, permitiéndonos asi nombrarlos de la siguiente forma:

# %% [markdown]
# Escalar: \
# Dim = 0 \
# Un solo dato o valor
# | 1 |
# |---|
# 
# Vector: \
# Dim = 1 \
# Listas de Python (Elementos colocados en una fila)
# | 0 | 1 | 2 | 3 | 4 |
# |---|---|---|---|---|
# 
# Matriz: \
# Dim = 2 \
# Hojas de cálculo (Elementos agrupados en forma de filas y columnas)
# | Color    | Pais     | Edad | Fruta   |
# |----------|----------|------|---------|
# | Rojo     | España   | 24   | Pera    |
# | Amarillo | Colombia | 30   | Manzana |
# 
# Tensor: \
# Dim >= 3 \
# Series de tiempo o imágenes (Objetos agrupados por capas)

# %% [markdown]
# ### `.ndim`

# %% [markdown]
# Si fuese necesario conocer la dimension de un objeto, podemos conocerla utilizando `.ndim`

# %% [markdown]
# #### Declarando un escalar

# %%
scalar = np.array(42)
print(scalar)
scalar.ndim

# %% [markdown]
# #### Declarando un vector

# %%
vector = np.array([1, 2, 3, 4])
print(vector)
vector.ndim

# %% [markdown]
# #### Declarando una matriz

# %%
Matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(matriz)
matriz.ndim

# %% [markdown]
# #### Declarando un tensor

# %%
tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13, 13, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(tensor)
tensor.ndim

# %% [markdown]
# El parámetro `.ndim`, nos permite declarar directamente el array con el numero de dimensiones

# %%
vector = np.array([1, 2, 3], ndmin = 10)
print(vector) 
vector.ndim 

# %% [markdown]
# ### `expand_dims()`

# %% [markdown]
# También podemos expandir las dimensiones de nuestro array con el método `expand_dims()`, donde utilizaremos **axis** = 0 que hace referencia a las filas y/o **axis** = 1 que hace referencia a las columnas.

# %%
expand = np.expand_dims(np.array([1, 2, 3]), axis = 0)
print(expand)
expand.ndim 

# %% [markdown]
# ### `squeeze`

# %% [markdown]
# Utilizaremos `squeeze` si lo que buscamos es remover(comprimir) las dimensiones que no están siendo ocupadas

# %%
print(vector, vector.ndim) 
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)


