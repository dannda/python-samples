#!/usr/bin/env python
# encoding: utf-8
"""
cuadrado_latino.py

Created by Dann on 2015-02-24.
Calcula el cuadrado latino nxn dados los n símbolos de entrada.
En un cuadrado latino los n símbolos aparecen una vez en cada fila y cada columna.
"""

import sys
import os

cuadrado=[]
n=0
sim=[]

def imprime():
	for row in cuadrado:
		print(row)
	print("")

def checa(i,j,s,n):
	for k in range(0,n):
		if (str)(cuadrado[i][k])==str(s):
			return 1
		if (str)(cuadrado[k][j])==str(s):
			return 1
	return 0
	
def llena(n,i,j):
	global cuadrado
	simu=[]
	if j==-1:
		imprime()
		return
	else:
		for s in sim:
			r=0
			for element in simu:
				if element==s:
					r=1
			if(cuadrado[i][j]=='/0' and r==0 and checa(i,j,s,n)==0):
				cuadrado[i][j]=s
				ni=i+1
				if(ni<n):
					nj=j
				else:
					ni=0
					nj=j+1
					if nj>=n:
						nj=-1
				llena(n,ni,nj)
				cuadrado[i][j]='/0'
				simu.append(s)

def main():
	print("***CUADRADO LATINO***\n")
	n=(int)(raw_input("n: "))
	for i in range(0,n):
		vec=['/0']
		for j in range(1,n):
			vec.append('/0')
		cuadrado.append(vec)
	
	for i in range(0,n):
		c=1
		while(c==1):
			s=(raw_input("Símbolo "+(str)(i+1)+": "))
			c=0
			for element in sim:
				if str(s)==str(element):
					print("Símbolo ya existente.")
					c=1
		sim.append(s)
	
	print("\nSímbolos:")
	print(sim)
	print("")
	
	imprime()
	llena(n,0,0)
	
	pass


if __name__ == '__main__':
	main()

