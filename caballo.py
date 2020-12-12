#!/usr/bin/env python
# encoding: utf-8
"""
caballo.py

Created by Dann on 2015-03-03.

Calcula el número de soluciones para que un caballo recorra cada casilla de un tablero nxn, para cada casilla inicial.
"""

import sys
import os
import math
import timeit

tablero=[]
s=0
movs=[[2,-1],[2,1],[1,2],[-1,2],[-2,-1],[1,-2],[-1,-2],[-2,1]]

def imprime():
	for row in tablero:
		print(row)
	print("")
	
def sol(n,i,j,num):
	global tablero
	global s
	movsu=[]
	if (num>(n*n)):
		s+=1
		return
	for mov in movs:
		r=0
		for element in movsu:
			if element==mov:
				r=1
		ti=i
		tj=j
		ti=ti+mov[0]
		tj=tj+mov[1]
		if(ti<0 or tj<0 or ti>=n or tj>=n):
			r=1
		if(r==0 and tablero[ti][tj]==0):
			tablero[ti][tj]=num
			sol(n,ti,tj,num+1)
			tablero[ti][tj]=0
			movsu.append(mov)
	return
		
		

def main():
	global tablero
	global s
	print("***RECORRIDO CABALLO***")
	n=(int)(raw_input("n: "))
	for i in range(0,n):
		vec=[0]
		for j in range(1,n):
			vec.append(0)
		tablero.append(vec)
	
	n2=round(n/2.)
	n2=int(n2)
	for i in range(0,n2):
		for j in range(0,n2):
			if(i==0 or j==n2-1 or i==j):
				s=0
				print("Posición inicial: "+str(i)+"-"+str(j))
				tablero[i][j]=1
				tic=timeit.default_timer()
				sol(n,i,j,2)
				toc=timeit.default_timer()
				tablero[i][j]=0
				print("Soluciones: "+str(s))
				print("Tiempo: "+str(toc-tic)+"\n")
	
	pass

if __name__ == '__main__':
	main()

