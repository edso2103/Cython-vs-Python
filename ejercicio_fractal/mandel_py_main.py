import numpy as np
import matplotlib.pyplot as plt
import sys
from mandel_py import compute_mandel as compute_mandel_py


def plot_mandel(mandel):
    plt.imshow(mandel)
    plt.axis('off')
    plt.show()

def main(version='py'):
    kwargs = dict(cr=0.285, ci=0.01,
                  N=1000,
                  bound=1.5)
    if version == 'py':
        mandel_func = compute_mandel_py
   

    mandel_set, runtime = mandel_func(**kwargs)
    return mandel_set, runtime
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        mandel_set, runtime = main('py')
        
    print('Tiempo de ejecución en python de  {0:5.10f} s'.format(runtime))
    #plot_mandel(mandel_set)

