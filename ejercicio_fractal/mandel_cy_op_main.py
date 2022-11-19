import numpy as np
import matplotlib.pyplot as plt
import sys
from cython2 import compute_mandel as compute_mandel_cy_op


def plot_mandel(mandel):
    plt.imshow(mandel)
    plt.axis('off')
    plt.show()

def main(version='cy_op'):
    kwargs = dict(cr=0.285, ci=0.01,
                  N=1000,
                  bound=1.5)

    if version == 'cy_op':
        mandel_func = compute_mandel_cy_op
   

    mandel_set, runtime = mandel_func(**kwargs)
    return mandel_set, runtime
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        mandel_set, runtime = main('cy_op')
        
    print('Tiempo de ejecución en cython optimizado de  {0:5.10f} s'.format(runtime))
    plot_mandel(mandel_set)

