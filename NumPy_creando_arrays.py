# %%
import numpy as np

# %% [markdown]
# ## Creando arrays

# %% [markdown]
# NumPy nos brinda la posibilidad de crear arrays completamente desde 0, lo cual facilita el trabajo al no necesitar realizar una declaración antes
# 

# %% [markdown]
# ### `arange()`
# 
# Nos permite crear arrays desde un elemento inicial hasta uno final (similar al `range()` nativo de Python)

# %%
np.arange(1, 11)

# %% [markdown]
# Si queremos definir pasos en especifico, bastara simplemente con agregar una tercer entrada

# %%
np.arange(1, 11, 2)

# %% [markdown]
# ### `zeros()` 
# 
# Nos permite definir estructuras o esquemas compuestas en su totalidad por ceros

# %%
np.zeros(5)

# %%
np.zeros((10, 5))

# %% [markdown]
# ### `ones()`
# 
# Nos permite definir estructuras o esquemas compuestas en su totalidad por unos

# %%
np.ones(5)

# %%
np.ones((10, 5))

# %% [markdown]
# ### `linspace()` 
# 
# Permite generar una array definiendo un inicio, un final y cuantas divisiones tendrá, esto creando divisiones exactamente iguales para cubrir el tamaño total

# %%
np.linspace(0, 10, 10)

# %% [markdown]
# ### `eye()`
# 
# Nos permite generar una matriz identidad (solo tiene unos en su diagonal principal el resto son ceros)

# %%
np.eye(4)

# %% [markdown]
# ### `random.rand()`
# 
# Nos permite generar números aleatorios entre 0 y 1

# %% [markdown]
# Un solo elemento aleatorio

# %%
np.random.rand()

# %% [markdown]
# Un array de números aleatorios

# %%
np.random.rand(4)

# %% [markdown]
# Una matriz de números aleatorios

# %%
np.random.rand(4, 4)

# %% [markdown]
# ### `random.randint()`
# 
# Nos permite generar numeros aleatorios enteros entre dos valores específicos

# %% [markdown]
# Solo genera un elemento

# %%
np.random.randint(1, 15)

# %% [markdown]
# Generando los elementos necesarios para rellenar una estructura definida

# %%
np.random.randint(1, 15, (3, 3))


