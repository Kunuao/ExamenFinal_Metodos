# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.int_(np.random.random(100)*1000)
print(x)

i=0
while (i<len(x)):
        if(x[i]%2 != 0):
            if(x[i]<800):
                print (x[i])
        elif(x[i]>800):
            i > len(x)
        i = i+1
            
                
                


