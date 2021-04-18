#%% slicing de listas
lista_precios = [12,42,1,23,41,5,5]
A = [[1,2,3],[3,4,5],[6,7,8]]
# %% generar una lista de pares desde 2 hasta 12
pares = []
for n in range(2,13):
    if n % 2 == 0:
        pares.append(n)
print(pares)
# %% list comprehension en python, lista de pares 2
pares = [n*n for n in range(2,13) if n % 2 == 0]
print(pares)
# %% tarea

