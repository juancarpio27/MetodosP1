import numpy as np
import matplotlib.pyplot as plt
import math

#Congruencial mixto
def congruencial_mixto(x0,a,c,m,n):
	X = []
	for i in range(0,n):
		x = (a * x0 + c) % m
		x0 = x
		x = float(x) / m
		X.append(x)
	return X

#Congruencial multiplicativo
def congruencial_multiplicativo(x0,a,m,n):
	X = []
	for i in range (0,n):
		x = (a * x0) % m
		x0 = x
		x = float(x) / m
		X.append(x)
	return X

#Distribucion uniforme
def uniforme(X,a,b):
	h = float(1)/(b-a)
	Uniforme = []
	for i in X:
		x = (i + h*a) / h
		Uniforme.append(x)
	return Uniforme

#Distribucion exponencial
def exponencial(X,l):
	Exponencial = []
	for i in X:
		x = math.log(i) / (-l)
		Exponencial.append(x)
	return Exponencial

#Distribucion normal
def normal(media,desviacion,generador,listaGenerador,N,M):
	x0 = listaGenerador[0]
	Normal = []
	for i in range (0,N):
		if generador == "mixto":
			X = congruencial_mixto(x0,listaGenerador[1],listaGenerador[2],listaGenerador[3],12)
		if generador == "multiplicativo":
			X = congruencial_multiplicativo(x0,listaGenerador[1],listaGenerador[2],12)
		cont = 0
		for j in X:
			cont = cont + j
		x = cont - 6
		x = desviacion*x+media
		Normal.append(x)
		x0 = X[11]
	return Normal

#Distribucion binomial
def binomial(n,p,generador,listaGenerador,N,M):
	x0 = listaGenerador[0]
	Binomial = []
	for i in range (0,N):
		if generador == "mixto":
			X = congruencial_mixto(x0,listaGenerador[1],listaGenerador[2],listaGenerador[3],n)
		if generador == "multiplicativo":
			X = congruencial_multiplicativo(x0,listaGenerador[1],listaGenerador[2],n)
		exitos = 0;
		print X
		for j in X:
			if j < p:
				exitos = exitos + 1
		Binomial.append(exitos)
		x0 = X[n-1]
	return Binomial

#Distribucion triangular
def triangular(a,b,c,X):
	Triangular = []
	punto = float(b-a)/(c-a)
	for i in X:
		if (i<punto):
			x = math.sqrt(i*(c-a)*(b-a))+a
		else:
			x = -math.sqrt((b-c)*(b-c)+(b-a)*(c-b)-i*(c-a)*(c-b))+c
		Triangular.append(x)
	return Triangular

#distribucion de Poisson
def poisson(l,X):
	Poisson = []
	e = math.exp(-l)
	for i in X:
		p = i
		contador = 0
		while p > e:
			contador = contador + 1
			p = p*i
		contador = contador - 1
		Poisson.append(contador)
	return Poisson



#Funcion principal
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
	
	#Funcion uniforme
	if funcion == "uniforme":
		a = funcionLista[0]
		b = funcionLista[1]
		U = uniforme(X,a,b)
		plt.hist(U,M)
		plt.show()
		return U

	#Funcion exponencial
	if funcion == "exponencial":
		l = funcionLista[0]
		E = exponencial(X,l)
		plt.hist(E,M)
		plt.show()
		return E

	if funcion == "triangular":
		a = funcionLista[0]
		b = funcionLista[1]
		c = funcionLista[2]
		T = triangular(a,b,c,X)
		plt.hist(T,M)
		plt.show()
		return T

	if funcion == "poisson":
		l = funcionLista[0]
		P = poisson(l,X)
		plt.hist(P,M)
		plt.axis([0, 20, 0, 0.4])
		plt.show()
		return P

	
#X = generador("mixto",[56,754,543,10000],"exponencial",[0.5],2000,10)
#X = generador("mixto",[56,754,543,10000],"triangular",[2,4,6],2000,10)
X = generador("mixto",[56,754,543,10000],"poisson",[10],1000,100)
