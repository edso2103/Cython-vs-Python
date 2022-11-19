# Presentación
<p align="center"><img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"width="200" height="200">
</img><br>
<i><b>Docente:</b></i> John Corredor, PhD.
<br>
<i><b>Asignatura:</b></i> Computación Paralela y Distribuida
<br>
<i><b>Estudiante:</b></i> Edna Sofía Orjuela Puentes y Paula Sofía Godoy
<br>
<i><b>Tema:</b></i> Tercer Parcial. Cython vs Python
<br>
<i><b>Fecha:</b></i>17/11/22
<br>
</p>

# Resumen

El siguiente cuaderno tiene como objetivo, analizar los resultados obtenidos de la ejecución de tres ejercicios diferentes __"heat equation, mandelBrot Fractal, Knapsack"__ , con el fin de comprobar que cython presenta mayor rendimiento con respecto a python, debido a su combinación de lenguajes, c++, c y python.

# Introducción

Al momento de desarrollar software es importante tener en consideración el factor del rendimiento, este es de gran importancia en distintos campos como por ejemplo, el desarrollo de videojuegos, trabajo con gran cantidad de datos (big data) o simulación científica,  la cual requiere una gran capacidad de cómputo. El rendimiento como tal no es considerado una medida sino una mezcla de varias. En los casos más comunes se tiene en cuenta el tiempo de respuesta al ejecutar una aplicación.<br>
Es por esto que es importante tener en cuenta el lenguaje de programación en el cual se desarrolla el software.<br>

# Desarrollo
Cuando se habla de tiempo de ejecución es necesario tener en cuenta el lenguaje de programación con el que se está trabajando va a determinar su velocidad. De acuerdo con lo mencionado, existen dos clases de lenguajes, interpretados y compilados. Se define como un lenguaje compilado a aquel que lee por completo el programa escrito en un lenguaje de alto nivel y lo traduce a un código de maquina equivalente. El programa en lenguaje de máquina sera el que se ejecutará.<br><br>
Por otro lado, un lenguaje interpretado, leerá instrucción por instrucción y para cada una de ellas habrá una traducción a código de máquina.<br><br>
Se pretende realizar una prueba de rendimiento en el lenguaje de programación Python y en Cython, con el fin de verificar la existencia de una posible mejora en la implementación de este programa al desarrollarse en el lenguaje de programación Cython, ya que este combina el lenguaje de c y python.

# Ejercicios

## 1. Heat Equation

Se seleccionó un algoritmo que implementa una ecuación diferencial para señalar la distribución de temperatura que tiene un objeto.<br><br>
El algoritmo realiza varias iteraciones para cambiar los valores en la ecuación y con ello modificar la imágen guardada. El propósito de esto es obtener un experimento óptimo y preciso al hallar el promedio de los resultados obtenidos.<br><br>
Es importante aclarar que en cada iteración se probó con una carga diferente para ver el comportamiento de los tiempos de ejecución en cada algoritmo.<br><br>
A continuación, se puede observar la forma de una botella, debido a la información que ofrece el dataset usado (bottle.dat). Esta botella cambia a medida que se varían los parámetros de la ecuación de calor.

<center>

![png_to_gif](https://user-images.githubusercontent.com/65740725/202584483-9468495f-59df-4332-b8fd-a3322d3d1006.gif)

Dentro de la carpeta "ejercicio_cocacola", se encuentran tres algoritmos, los cuales son:

*  **Python:** algoritmo original en python.
*  **Cython:** algoritmo de python sin modificaciones, pero en C con Cython.
*  **Cython optimizado:** algoritmo con mejoras de rendimiento.

De este ejercicio se obtiene una mejora considerable en el algoritmo de Cython optimizado con respecto a los otros. Además, se observa una pequeña diferencia en tiempo de ejecución entre los algoritmos de Python y Cython sin optimizar, pese a que el programa de Cython sea el mismo de Python solo que convertido a lenguaje C.

<center>

![imagen](https://user-images.githubusercontent.com/65740725/202607810-70ddc922-3a87-476c-981b-b2db02fea416.png)


## 3. Knapsack

Por último, se decidió realizar un algoritmo para resolver el problema de la mochila, conocido como knapsack problem, este consiste en una mochila que tiene un peso máximo específico que puede contener. En la mochila caben varios objetos, y cada uno de ellos tiene un peso y un valor diferentes. El objetivo es meter en la mochila tantos artículos como sea posible para que el valor total sea máximo y el peso total no supere el límite de la mochila. En la variante más sencilla del problema, se ignoran el tamaño y las dimensiones físicas de los artículos.

Para el análisis de resultados se decidió realizar las pruebas sobre tres archivos distintos con el mismo número de iteraciones, dentro del primero se observa una cantidad de objetos de peso menor o igual que el de la mochila, por último, se realiza la prueba con una gran cantidad de objetos (500), con el objetivo de observar como se comportan los tiempos entre Python y Cython.

<center>
<img src="https://miro.medium.com/max/1400/1*3bZOzhhzAtmcYYc427m5Aw.png"
width="400" height="300">

De este experimento se evidencia un comportamiento ligeramente extraño, ya que tiene unas fluctuaciones pronunciadas, a pesar de que el tiempo tiende a disminuir a medida que avanzan las iteraciones. Por otro lado, el algoritmo en _Cython_ desde las primeras iteraciones busca que los tiempos de ejecución vayan disminuyendo, aunque a medida que van avanzando las iteraciones vuelve a aumentar ligeramente con un comportamiento más constante, a diferencia de _Python_.  Finalmente, se puede ver una comparación de los dos algoritmos donde se consigue una mejora considerable en rendimiento al implementar el algoritmo en el lenguaje de _Cython_.
![imagen](https://user-images.githubusercontent.com/65740725/202611453-24d9cbda-666e-4553-834e-59037bd1d34f.png)


# Guía para la ejecución del proyecto

Este proyecto cuenta con tres carpetas, en cada una de ellas, se encuentra un ejercicio diferente con 5 archivos que corresponden a:<br> 
1. **Makefile:** Automatizar la compilación de los programas <br>
2. **Setup:** Para construir el programa en cython.<br>
3. **principal.py:** Programa principal que permite la ejecución de los programas *planet_cy.pyx* y *planet_cy.py*, este archivo contiene el método 'repeat' de la biblioteca 'timeit' para realizar varias iteraciones y ofrecer un promedio de los tiempos de ejecución.
4. **ejemplo_cy.pyx:** Programa en cython de la solución propuesta para el problema, similar al programa en python, pero con algunas modificaciones para mejorar el rendimiento
5. **ejemplo_cy.py:** Programa en python de la solución propuesta para el problema.
6. **Cuaderno en google colab del análisis realizado:** [https://colab.research.google.com/drive/1DdR69P_DUUTEr8wQJor-EqIdbm3rN8Y1?usp=sharing](https://colab.research.google.com/drive/1vhlgFe3izWjVteg0-ps3j3pbQ2LAijRd?usp=sharing)

# Conclusiones



# Referencias

*  Difference Between Compiler and Interpreter: [Full Comparison]. (2022, 25 julio). InterviewBit. https://www.interviewbit.com/blog/difference-between-compiler-and-interpreter/ GitHub - sebmancipe/cython-exercises: Contains exercises related with Python/Cython algorithms optimization. (2022, 24 noviembre). 

*  GitHub. https://github.com/sebmancipe/cython-exercises
