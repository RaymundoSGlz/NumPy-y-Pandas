# %%
import numpy as np

# %% [markdown]
# ## Tipos de datos
# Los arrays de NumPy solo pueden contener un tipo de dato, ya que esto es lo que le confiere las ventajas de la *optimización de memoria*.

# %% [markdown]
# ### `.dtype`
# Si necesitamos saber el tipo de datos del array utilizamos `.dtype`

# %%
arr = np.array([1, 2, 3, 4])
arr.dtype

# %% [markdown]
# Podemos definir el tipo de datos desde la creación del array

# %%
arr = np.array([1, 2, 3, 4], dtype = 'float64')
arr.dtype

# %%
arr

# %% [markdown]
# ### `.astype`
# Si ya tenemos definido el array y queremos cambiar su tipo lo podemos hacer con `.astype`

# %%
arr = arr.astype(np.int64)
arr

# %% [markdown]
# Podemos utilizar esta sintaxis para otro tipo de datos

# %% [markdown]
# #### Booleano
# *Al convertir a booleano todos los elementos distintos de 0 serán **True***

# %%
arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.bool_)
arr

# %% [markdown]
# #### String

# %% [markdown]
# Podemos llevar de *int* a *string*

# %%
arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.string_)
arr

# %% [markdown]
# Podemos realizar también el proceso inverso

# %%
arr = arr.astype(np.int8)
arr

# %% [markdown]
# > *Debemos considerar que si intentamos convertir un string que contiene distintos tipos de datos obtendremos un error*

# %%
arr = np.array(['hola', '1', '2', '3', '4'])
arr = arr.astype(np.int8)
arr


