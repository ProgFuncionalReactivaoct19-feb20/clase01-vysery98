from metodos import *

# Salida de Datos enviando parámetros a los Métodos

print(metodoUno(3))

print(metodoDos(metodoUno(4)))

print(metodoTres(metodoDos(metodoTres(5))))

print(metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))