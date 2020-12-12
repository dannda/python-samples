#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Dann on 2015-02-25.
Cuadrado grecolatino octogonal
n:3 a,b,c A,B,C
pares únicos
 Ac Bb Ca
 Cb Aa Bc
 Ba Cc Ab
Cada par aparece una vez. Cada símbolo aparece una vez por fila y por columna.
"""

import sys
import os

cuadrado=[]
n=0
sim1=[]
sim2=[]

def imprime():
	for row in cuadrado:
		print(row)
	print("")

def checa(i,j,s,s2,n):
	for k in range(0,n):
		if (str)(cuadrado[i][k][0])==(str(s)) or (str)(cuadrado[i][k][1])==(str(s2)):
			return 1
		if (str)(cuadrado[k][j][0])==(str(s)) or (str)(cuadrado[k][j][1])==(str(s2)):
			return 1
	return 0

def llena(n,i,j,pares):
	global cuadrado
	pares=pares
	#cor=0
	simu1=[]
	if j==-1:
		imprime()
		return
	else:
		r=0
		for s in sim1:
			r=0
			simu2=[]
			for s2 in sim2:	
				r=0
				for element in simu1:
					if element==s:
						r=1
				for element in simu2:
					if element==s2:
						r=1
				for element in pares:
					if element==(str)(s)+(str)(s2):
						r=1
				if(cuadrado[i][j]=='/0' and r==0 and checa(i,j,s,s2,n)==0):
					cuadrado[i][j]=(str)(s)+(str)(s2)
					ni=i+1
					if(ni<n):
						nj=j
					else:
						ni=0
						nj=j+1
						if nj>=n:
							nj=-1
					pares1=list(pares)
					pares1.append((str)((str)(s)+(str)(s2)))
					llena(n,ni,nj,pares1)
					cuadrado[i][j]='/0'
					simu2.append(s2)
			simu1.append(s)

def main():
	print("***CUADRADO GRECOLATINO OCTOGONAL***\n")
	n=(int)(raw_input("n: "))
	for i in range(0,n):
		vec=['/0']
		for j in range(1,n):
			vec.append('/0')
		cuadrado.append(vec)
	
	for i in range(0,n):
		c=1
		while(c==1):
			s=(raw_input("Símbolo "+(str)(i+1)+" de la primera serie de símbolos: "))
			c=0
			for element in sim1:
				if str(s)==str(element):
					print("Símbolo ya existente.")
					c=1
			if len(s)<1:
				print("Símbolo vacío")
				c=1
		sim1.append(s)
	
	for i in range(0,n):
		c=1
		while(c==1):
			s=(raw_input("Símbolo "+(str)(i+1)+" de la segunda serie de símbolos: "))
			c=0
			for element in sim2:
				if str(s)==str(element):
					print("Símbolo ya existente.")
					c=1
			if len(s)<1:
				print("Símbolo vacío")
				c=1
			for element in sim1:
				if str(s)==str(element):
					print("Símbolo ya existente en los primeros símbolos.")
					c=1
		sim2.append(s)
		
	print("\nSímbolos:")
	print(sim1)
	print(sim2)
	print("")
	
	pares=[]
	llena(n,0,0,pares)
	
	
	pass


if __name__ == '__main__':
	main()

