#!/usr/bin/env python
# encoding: utf-8
"""
buscaminas.py

Created by Dann on 2015-03-24.
Crea un tablero de buscaminas dada la entrada de filas, columnas, y cantidad de minas.
Luego pide seleccionar una casilla y actualiza el tablero.
todo: final exitoso
"""

import sys
import os
import random

m=0
n=0
tablero=[]
movs=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

def imprime(mina=False):
	for i in range(0,len(tablero)):
		print ' '+str(i+1)+' ',
	print ''
	j=1
	for row in tablero:
		for car in row:
			if mina or car != '*':
				print '['+car+']',
			else:
				print '['+' '+']',
		print ' '+str(j)
		j+=1
		
def ady(i,j,m,n):
	global tablero
	movs1=list(movs)
	movs2=list(movs)
	for mov1 in movs1:
		ti=i
		tj=j
		ti=ti+mov1[0]
		tj=tj+mov1[1]
		if(ti>=0 and tj>=0 and ti<m and tj<n and tablero[ti][tj]==' '):
			contM=0
			for mov2 in movs2:
				tti=ti
				ttj=tj
				tti=tti+mov2[0]
				ttj=ttj+mov2[1]
				if(tti>=0 and ttj>=0 and tti<m and ttj<n and tablero[tti][ttj]=='*'):
					contM+=1
			if contM!=0:
				tablero[ti][tj]=str(contM)
			else:
				if(ti>=0 and tj>=0 and ti<m and tj<n):
					tablero[ti][tj]='░'
					ady(ti,tj,m,n)
	
def main():
	
	print '***BUSCAMINAS***'
	m=int(raw_input('filas: '))
	n=int(raw_input('columnas: '))
	k=int(raw_input('cantidad de minas: '))
	
	vec=[]
	for i in range(0,m):
		vec=[]
		for i in range(0,n):
			vec.append(' ')
		tablero.append(vec)
	
	while k>0:
		i=random.choice(range(0,m))
		j=random.choice(range(0,n))
		if tablero[i][j]==' ':
			tablero[i][j]='*'
			k-=1
			
	imprime()
	
	mina=False
	while(mina==False):
		print '\nSelecciona una posición'
		i=(int(raw_input('fila: ')))-1
		j=(int(raw_input('columna: ')))-1
		
		print ''
		if tablero[i][j]=='*':
			print 'Hay una mina'
			mina=True
		else:
			contM=0
			for mov in movs:
				ti=i
				tj=j
				ti=ti+mov[0]
				tj=tj+mov[1]
				if(ti>=0 and tj>=0 and ti<m and tj<n and tablero[ti][tj]=='*'):
					contM+=1		
				
			if contM!=0:
				tablero[i][j]=str(contM)
			else:
				tablero[i][j]='░'
				ady(i,j,m,n)
		imprime(mina)
			
	
	pass


if __name__ == '__main__':
	main()

