#!/usr/bin/env python
# coding: utf-8

# In[59]:


import matplotlib.pyplot as plt                                 # importar el módulo pyplot
x_axis = [10, 20, 30, 40, 50]                                  
plt.plot (x_axis, color = "pink", linewidth = 3.0)              # generar el gráfico de la función y=x
plt.title ("Distancia en función del tiempo", fontsize=16)      # título y tamaño de la letra
plt.ylabel('distance (m)')                                      # descripción en el eje y
plt.xlabel('time (s)')                                          # descripción en el eje x
plt.show()                                                      # mostrar el gráfico en pantalla


# se crea un gráfico que representa cinco puntos en un array y luego se muestra con show()


# In[44]:


import matplotlib.pyplot as plt
x = [1,2,3]
y = [1,2,3]
plt.plot (x, y, color = "green", linewidth = 2.0)
plt.plot(x, y)
plt.show()                                                     # mostrar el gráfico en pantalla


# In[88]:


import numpy                                      # otra opción: el comando %pylab carga automáticamente pylab
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy                                                      
plt = pyplot                                      

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

from pylab import *
from numpy import *                               # hasta aquí se activa el modo interactivo y se importa el módulo numpy


x = arange(10.)      # array de floats, de 0.0 a 9.0
grafica, = plot(x)   # generar el gráfico de la función y=x                                     
plot(x, 'c-')        # línea continua color cian, cian+(-)
plot(x, 'mo')        # pinta 10 puntos como "o" color magenta, magenta(o-)


# In[ ]:




