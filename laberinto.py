#!/usr/bin/env python
# encoding: utf-8
"""
laberinto.py

Created by Dann on 2015-03-23.
Dado un archivo laberinto.txt con muros como '|' y espacios como '0',
busca e imprime todas las soluciones.
"""

import sys
import os

lab=[]
m=0
n=0
movs=[[0,1],[1,0],[0,-1],[-1,0]]

def imprime(x):
	
	labP=list(lab)
	if x>=10:
		for row in labP:
			for car in row:
				car=str(car)
				if car.isdigit():
					for i in range(0,len(str(x))-len(car)):
						car=str(' '+str(car))
				else:
					for i in range(0,len(str(x))+1):
						car+=str(car)
	#print labP
	print "Solución:\n"

	if x<10:
		for row in lab:
			for car in row:
				print car,
			print '\n'
	else:
		for row in lab:
			for car in row:
				car=str(car)
				if car.isdigit():
					for i in range(0,len(str(x))-len(car)):
						print ' ',
					for char in car:
						print char,
					print ' ',
				else:
					for i in range(0,len(str(x))+1):
						print car,
					#print ' ',
			print '\n'
	print '\n'

def sol(x,i,j,m,n):
	global lab
	if(i==1 and j==n-1):
		lab[i][j+1]=x
		imprime(x)
		return	
	for mov in movs:
		ti=i
		tj=j
		ti=ti+mov[0]
		tj=tj+mov[1]
		if(ti>=0 and tj>=0 and ti<m and tj<n and lab[ti][tj]==0):
			lab[ti][tj]=x
			sol(x+1,ti,tj,m,n)
			lab[ti][tj]=0
	return

def main():
	
	print "***Laberinto***\n"
	with open('laberinto.txt','r') as f:
		lines=f.readlines()
		f.close()
	
	m=0
	for line in lines:
		lab.append([])
		for n in range(0,len(line)-1):
			if line[n]=='0':
				lab[m].append(0)
			else:
				lab[m].append(line[n])
		m+=1
	
	print m
	print n
	
	if (lab[m-1][1]==0 and lab[1][n-1]==0):
		for row in lab:
			for car in row:
				print car,
			print '\n'
		print '\n'
		
		lab[m-1][1]=1
		sol(2,m-1,1,m,n)
		
	else:
		print "Error en laberinto\n"
			
	pass


if __name__ == '__main__':
	main()

