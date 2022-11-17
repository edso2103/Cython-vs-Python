'''
Autor: Edna Sofia Orjuela Puentes
Clase: Computación Paralela Distribuida
Fecha: 15 de Noviembre del 2022
Universidad Sergio Arboleda
'''


from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

cython1=Extension('cython1',['heat_cy_1.pyx'])
cython2=Extension('cython2',['heat_cy_2.pyx'])

setup(ext_modules=cythonize([cython1,cython2]),include_dirs=[numpy.get_include()])
