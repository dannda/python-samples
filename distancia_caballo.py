#!/usr/bin/env python
# encoding: utf-8
"""
distancia_caballo.py

Created by Dann on 2015-03-11.
Para un tablero nxn imprime para cada casilla la cantidad de movimientos de distancia para un caballo en una casilla inicial dada.
"""

import sys
import os

tablero=[]
movs=[[2,-1],[2,1],[1,2],[-1,2],[-2,-1],[1,-2],[-1,-2],[-2,1]]

def imprime():
	for row in tablero:
		print(row)
	print("")

def main():
	print("***DISTANCIA CABALLO***")
	n=(int)(raw_input("Tablero tamaño n: "))
	for i in range(0,n):
		vec=[-1]
		for j in range(1,n):
			vec.append(-1)
		tablero.append(vec)
	
	xi=(int)(raw_input("x inicial: "))
	yi=(int)(raw_input("y inicial: "))
	
	tablero[xi-1][yi-1]=0
	
	for x in range(0,n):
		c=0
		for i in range(0,n):
			for j in range(0,n):
				if tablero[i][j]==x:
					c=1
					for mov in movs:
						ti=i
						tj=j
						ti=ti+mov[0]
						tj=tj+mov[1]
						if(ti>=0 and tj>=0 and ti<n and tj<n and tablero[ti][tj]==-1):
							tablero[ti][tj]=x+1
	
	imprime()
	
	pass


if __name__ == '__main__':
	main()

