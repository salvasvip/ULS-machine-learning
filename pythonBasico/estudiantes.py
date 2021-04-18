#%% Estudiante
materias = ['mat', 'fis', 'qmc']
notas = []
for materia in materias:
    notas.append(int(input(f"ingrese la nota para {materias}")))

promedio = (notas[0] + notas[1] + notas[2])/3
print(f'promedio: {promedio}')