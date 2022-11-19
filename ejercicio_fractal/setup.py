from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

cython1=Extension('cython1',['mandel_cy.pyx'])
cython2=Extension('cython2',['mandel_cy_op.pyx'])

setup(ext_modules=cythonize([cython1,cython2]),include_dirs=[numpy.get_include()])
