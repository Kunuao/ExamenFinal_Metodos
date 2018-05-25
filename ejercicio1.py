# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

derivada1 = []
derivada2 = []
x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
fx1=np.array([0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.]) 

valor0 = fx[0] - fx1[0]
valor1 = fx[1] - fx1[1]
valor2 = fx[2] - fx1[2]
valor3 = fx[3] - fx1[3]
valor4 = fx[4] - fx1[4]
valor5 = fx[5] - fx1[5]
valor6 = fx[6] - fx1[6]
valor7 = fx[7] - fx1[7]
valor8 = fx[8] - fx1[8]

derivada1.append(valor0)
derivada1.append(valor1)
derivada1.append(valor2)
derivada1.append(valor3)
derivada1.append(valor4)
derivada1.append(valor5)
derivada1.append(valor6)
derivada1.append(valor7)
derivada1.append(valor8)


val0= derivada[1] - derivada[0]
val1= derivada[2] - derivada[1]
val2= derivada[3] - derivada[2]
val3= derivada[4] - derivada[3]
val4= derivada[5] - derivada[4]
val5= derivada[6] - derivada[5]
val6= derivada[7] - derivada[6]
val7= derivada[8] - derivada[7]


derivada2.append(val0)
derivada2.append(val1)
derivada2.append(val2)
derivada2.append(val3)
derivada2.append(val4)
derivada2.append(val5)
derivada2.append(val6)
derivada2.append(val7)

plt.plot(derivada2,x)
plt.show()
plt.savefig("segunda.png")