from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("knapsack_cy.pyx"))
setup(ext_modules = exts)