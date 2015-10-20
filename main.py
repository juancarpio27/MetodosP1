import numpy as np
import matplotlib.pyplot as plt

def congruencial_mixto(x0,a,c,m,n):
	X = []
	for i in range(0,n):
		x = (a * x0 + c) % m
		x0 = x
		x = float(x) / m
		X.append(x)
	return X

def congruencial_multiplicativo(x0,a,m,n):
	X = []
	for i in range (0,n):
		x = (a * x0) % m
		x0 = x
		x = float(x) / m
		X.append(x)
	return X

def uniforme(X,a,b):
	h = float(1)/(b-a)
	U = []
	for i in X:
		x = (i + h*a) / h
		U.append(x)
	return U


def generador(generador,listaGenerador,funcion,funcionLista,N,M):
	#Generando el vector con congruencial mixto o multiplicativo
	if generador == "mixto":
		x0 = listaGenerador[0]
		a = listaGenerador[1]
		c = listaGenerador[2]
		m = listaGenerador[3]
		X = congruencial_mixto(x0,a,c,m,N)

	if generador == "multiplicativo":
		x0 = listaGenerador[0]
		a = listaGenerador[1]
		m = listaGenerador[2]
		X = congruencial_multiplicativo(x0,a,m,N)
	
	if funcion == "uniforme":
		a = funcionLista[0]
		b = funcionLista[1]
		U = uniforme(X,a,b)
		plt.hist(U,M)
		plt.show()
		return U

		
X = generador("mixto",[56,754,543,10000],"uniforme",[2,5],2000,10)
