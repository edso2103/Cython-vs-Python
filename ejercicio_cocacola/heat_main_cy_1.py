'''
Nombre: Edna Sofía Orjuela Puentes
Materia: Computación Paralela y Distribuida
Algoritmo: Heat equation en cython (MAIN)
'''

from __future__ import print_function
import time
import argparse

from cython1 import init_fields, write_field, iterate


def main(input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=100, image_interval=10):

    # Inicializar el campo de temperatura
    field, field0 = init_fields(input_file)

    # Escribir el campo inicial
    write_field(field, 0)
    
    # Realizar iteraciones
    t0 = time.time()
    iterate(field, field0, a, dx, dy, timesteps, image_interval)
    t1 = time.time()
    
    # Escribir el campo final
    write_field(field, timesteps)
    #print("Tiempo de ejecución Cython sin optimizar{0} s".format(t1-t0))


if __name__ == '__main__':

    # Argumentos o parámetros 
    parser = argparse.ArgumentParser(description='Heat equation')
    parser.add_argument('-dx', type=float, default=0.01,
                        help='grid spacing in x-direction')
    parser.add_argument('-dy', type=float, default=0.01,
                        help='grid spacing in y-direction')
    parser.add_argument('-a', type=float, default=0.5,
                        help='diffusion constant')
    parser.add_argument('-n', type=int, default=100,
                        help='number of time steps')
    parser.add_argument('-i', type=int, default=10,
                        help='image interval')
    parser.add_argument('-f', type=str, default='bottle.dat', 
                        help='input file')

    args = parser.parse_args()

    main(args.f, args.a, args.dx, args.dy, args.n, args.i)

