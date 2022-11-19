from mandel_cy_op_main import main as mandel_main_cy_op
from mandel_cy_main import main as mandel_main_cy
from mandel_py_main import main as mandel_main_py

from timeit import repeat

formato_datos = "{:.5f}, {:.5f}, {:.5f}\n" 
niterations = 10

# Python
time_python = repeat("mandel_main_py()", number=niterations, repeat=1, globals=locals())
time_python = min(time_python)/ niterations 

# Cython no optimizado
time_cython = repeat("mandel_main_cy()", number=niterations, repeat=1, globals=locals())
time_cython = min(time_cython)/ niterations


# Cython optimizado
time_cython_opt = repeat("mandel_main_cy_op()", number=niterations, repeat=1, globals=locals())
time_cython_opt = min(time_cython_opt) / niterations


with (open("mandel.csv","a")) as archivo:
		archivo.write(formato_datos.format(time_python,time_cython, time_cython_opt))

print("Promedio de python para 10 iteraciones: ",time_python)
print("Promedio de Cython para 10 iteraciones: ",time_cython)
print("Mejora:                                    {:5.1f}".format(((time_python/time_cython)-1)))
print("Promedio de Cython optimizado para 10 iteraciones: ",time_cython_opt)
print("Mejora de Cython:                        {:5.1f}".format(((time_cython/time_cython_opt)-1)))

