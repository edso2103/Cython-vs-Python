#cython: language_level=3

import numpy as np
cimport numpy as array_def #https://stackoverflow.com/a/51269679
import cython

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Establecer el mapa de colores
plt.rcParams['image.cmap'] = 'BrBG'

""" 
La siguiente función es para la evolución de la imagen, donde 
u: es un nuevo campo de temperatura
u_previous: es el campo anterior
a: es la constante de difusión
dt: es el salto de tiempo. 
"""

#Se define el decorador para evitar errores en la división
@cython.cdivision(True)
cdef evolve(array_def.ndarray[array_def.double_t, ndim=2] u, 
            array_def.ndarray[array_def.double_t, ndim=2] u_previous,		
            double a, double dt, double dx2, double dy2):

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]

    cdef int i,j

    # Se cambia la división por la multiplicación ya que consume menos tiempo
    cdef double inver_dx_2 = 1. / dx2 #Se halla la inversa
    cdef double inver_dy_2 = 1. / dy2

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) * inver_dx_2 + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) * inver_dy_2 )
    u_previous[:] = u[:]


# Función para realizar el procedimiento en un número de de pasos de tiempo determinados
def iterate(field, field0, a, dx, dy, timesteps, image_interval):

    dx2 = dx**2
    dy2 = dy**2

    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

# Función para leer la temperatura inicial
def init_fields(filename):
    # Se lee del archivo
    field = np.loadtxt(filename)
    field0 = field.copy() 
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))

