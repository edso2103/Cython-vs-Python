import numpy as np
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

def evolve(u, u_previous, a, dt, dx2, dy2):
    n, m = u.shape

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) / dx2 + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) / dy2 )
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
    field0 = field.copy() # Array for field of previous time step
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))


