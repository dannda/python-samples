#!/usr/bin/env python
# encoding: utf-8
# -*- coding:utf-8 -*-

import sys
import os
import re
from Tkinter import *
import tkMessageBox

def main_frame():
	frame.tkraise()

def raise_frame(myNum):
	exframes[myNum].tkraise()
	labelAny.grid_forget()
	labelAnyStr.grid_forget()
	labelAnyTrad.grid_forget()

def remove_art(arr):
	art=[]
	for k in range(0,len(arr)):
		if arr[k].lower()=="el" or arr[k].lower()=="la" or arr[k].lower()=="los" or arr[k].lower()=="las":
			art.append(k)
	for k in range(0,len(art)):
		del arr[art[k]-k]
	return arr

def make_pred(arr):
	ar=[]
	for k in range(0,len(arr)):
		if arr[k].lower()=="es" and arr[k+1]:
			arr[k]="es"+arr[k+1].capitalize()
			ar.append(k+1)
	for k in range(0,len(ar)):
		del arr[ar[k]-k]
	return arr
	
def trad(i,j,stri,arr,n):
	tradS=""
	pred=0
	arr=remove_art(arr)
	if i==0:
		for k in range(0,len(arr)):
			if arr[k].lower()=="no":
				tradS="¬ "
				break
		for k in range(0,len(arr)):
			if arr[k].lower()=="es":
				tradS+="es"
				pred=1
				break
		if pred==1:
			tradS+=(arr[len(arr)-1]).capitalize()+"("+arr[0]+")"
		else:
			tradS+=arr[len(arr)-1]+"("+arr[0]+")"
		
	elif i==1:
		if j==0:
			tradS+=arr[1]+arr[2].capitalize()+"("+arr[0]+","+arr[len(arr)-1]+")"
		else:
			tradS+="¬ "+arr[2]+arr[3].capitalize()+"("+arr[0]+","+arr[len(arr)-1]+")"
	
	elif i==2:
		if j==0:
			if arr[0].lower()=="todo" or arr[0].lower()=="toda":
				tradS+="∀x("
			else:
				tradS+="∃x("
			if len(arr)==7:
				tradS+="(es"+arr[1].capitalize()+"(x) ^ "+"es"+arr[4].capitalize()+"(x)) -> es"+arr[6].capitalize()+"(x))"
			else:
				tradS+="(es"+arr[1].capitalize()+"(x) ^ "+arr[3]+"(x)) -> es"+arr[5].capitalize()+"(x))"
		if j==1:
			if arr[0].lower()=="no":
				tradS+="¬ (∀x("
				if len(arr)==8:
					tradS+="(es"+arr[2].capitalize()+"(x) ^ "+"es"+arr[5].capitalize()+"(x)) -> es"+arr[7].capitalize()+"(x)))"
				else:
					tradS+="(es"+arr[2].capitalize()+"(x) ^ "+arr[4]+"(x)) -> es"+arr[6].capitalize()+"(x)))"
			else:
				tradS+="¬ (∃x("
				if len(arr)==7:
					tradS+="(es"+arr[1].capitalize()+"(x) ^ "+"es"+arr[4].capitalize()+"(x)) -> es"+arr[6].capitalize()+"(x)))"
				else:
					tradS+="(es"+arr[1].capitalize()+"(x) ^ "+arr[3]+"(x)) -> es"+arr[5].capitalize()+"(x)))"
	
	elif i==3:
		if j==0:
			tradS+="∀x(("
		elif j==1:
			tradS+="∃x(("
		elif j==2:
			tradS+="¬ (∀x(("	
		elif j==3:
			tradS+="¬ (∃x(("
		if j==2:	
			tradS+="es"+arr[2].capitalize()+"(x) v es"+arr[4].capitalize()+"(x)) -> "+arr[5]+"(x))"
		else:
			tradS+="es"+arr[1].capitalize()+"(x) v es"+arr[3].capitalize()+"(x)) -> "+arr[4]+"(x))"
		if j==2 or j==3:
			tradS+=")"
	
	elif i==4:
		arr=make_pred(arr)
		if j==0:
			if arr[0].lower()=="todo" or arr[0].lower()=="toda":
				tradS+="∀x"
			else:
				tradS+="∃x"
			if arr[4].lower()=="todo" or arr[4].lower()=="toda":
				tradS+=" ∀y("
			else:
				tradS+=" ∃y("		
			tradS+="(es"+arr[1].capitalize()+"(x) -> "+arr[2]+"(x)) ^ (es"+arr[5].capitalize()+"(y) -> "+arr[6]+"(y)))"
		elif j==1:
			tradS+="¬ (∀x ∀y("+"(es"+arr[2].capitalize()+"(x) -> "+arr[3]+"(x)) ^ (es"+arr[7].capitalize()+"(y) -> "+arr[8]+"(y))))"
		elif j==2:
			tradS+="¬ (∀x ∃y("+"(es"+arr[2].capitalize()+"(x) -> "+arr[3]+"(x)) ^ (es"+arr[6].capitalize()+"(y) -> "+arr[7]+"(y))))"
		elif j==3:
			tradS+="¬ (∃x ∀y("+"(es"+arr[1].capitalize()+"(x) -> "+arr[2]+"(x)) ^ (es"+arr[6].capitalize()+"(y) -> "+arr[7]+"(y))))"
		elif j==4:
			tradS+="¬ (∃x ∃y("+"(es"+arr[1].capitalize()+"(x) -> "+arr[2]+"(x)) ^ (es"+arr[5].capitalize()+"(y) -> "+arr[6]+"(y))))"
	else:
		return	
	
	if n!=1:
		l=len(addedEx[i])
		addedEx[i].append([Label(exframes[i],text=stri),Label(exframes[i],text=tradS,fg="red"),Button(exframes[i],text="Eliminar",command=lambda i=i,l=l:remove_addEx(i,l))])
		addedEx[i][-1][0].grid(row=(9+len(rules[i])+len(addedEx[i])),column=0,sticky="e")
		addedEx[i][-1][1].grid(row=(9+len(rules[i])+len(addedEx[i])),column=1,sticky="w")
		addedEx[i][-1][2].grid(row=(9+len(rules[i])+len(addedEx[i])),column=2,sticky="w")
	if n!=0:
		return tradS
	else:
		return

def remove_addEx(i,j):
	for k in range(0,3):
		addedEx[i][j][k].destroy()
	addedEx[i].pop(j)
	for k in range(0,len(addedEx[i])):
		addedEx[i][k][2].config(command=lambda i=i,k=k:remove_addEx(i,k))
	
def check_regex(num):
	stri = (str(entries[num].get()))
	
	for i in range(0,len(regex[num])):
		m = re.match(r""+regex[num][i],stri.lower())
		if m:
			trad(num,i,stri,stri.split(" "),0)
			return
	tkMessageBox.showerror("Error","No concuerda con la estructura.")

def check_regexEx(n1,n2):
	stri = exampleLabels[n1][n2]
	for i in range(0,len(regex[n1])):
		m = re.match(r""+regex[n1][i],stri.lower())
		if m:
			tradS = trad(n1,i,stri,stri.split(" "),1)
			return tradS

def add_any():
	stri = str(added.get())
	matching=0
	for i in range(0,len(regex)):
		for j in range(0,len(regex[i])):
			m = re.match(r""+regex[i][j],stri.lower())
			if m:
				matching=1
				tradS = trad(i,j,stri,stri.split(" "),2)
				labelAny.config(text="Se agregó el ejemplo a la estructura "+str(i+1))
				labelAny.grid(row=11,columnspan=2)
				labelAnyStr.config(text=stri)
				labelAnyStr.grid(row=12,column=0,sticky="e")
				labelAnyTrad.config(text=tradS)
				labelAnyTrad.grid(row=12,column=1,sticky="w")
				break
	if matching==0:
		tkMessageBox.showerror("Error","No concuerda con ninguna estructura.")
		
regex=[
	[
		"((el|la|los|las) )?[a-z]+( no)? (es )?[a-z]+$"
	],
	[
		"((el|la|los|las) )?[a-z]+ (es|son) [a-z]+ de ((el|la|los|las) )?[a-z]+$",
		"((el|la|los|las) )?[a-z]+( no)? (es|son) [a-z]+ de ((el|la|los|las) )?[a-z]+$"
	],
	[
		"((todo|toda|algun|algún|alguna) )[a-z]+( que)( es)? [a-z]+ (es) [a-z]+$",
		"(((no todo)|(no toda)|ningun|ningún|ninguna) )[a-z]+( que)( es)? [a-z]+ (es) [a-z]+$"
	],
	[
		"((todo|toda) )[a-z]+( y) [a-z]+ [a-z]+$",
		"((algun|algún|alguna) )[a-z]+( o) [a-z]+ [a-z]+$",
		"((no todo|no toda) )[a-z]+( y) [a-z]+ [a-z]+$",
		"((ningun|ningún|ninguna) )[a-z]+( o) [a-z]+ [a-z]+$"
	],
	[
		"((todo|toda|algun|algún|alguna) )[a-z]+( es)? [a-z]+( y) ((todo|toda|algun|algún|alguna) )[a-z]+( es)? [a-z]+$",
		"((no todo|no toda) )?[a-z]+( es)? [a-z]+( y) ((no todo|no toda) )[a-z]+( es)? [a-z]+$",
		"((no todo|no toda) )?[a-z]+( es)? [a-z]+( y) ((ningun|ningún|ninguna) )[a-z]+( es)? [a-z]+$",
		"((ningun|ningún|ninguna) )?[a-z]+( es)? [a-z]+( y) ((no todo|no toda) )[a-z]+( es)? [a-z]+$",
		"((ningun|ningún|ninguna) )?[a-z]+( es)? [a-z]+( y) ((ningun|ningún|ninguna) )[a-z]+( es)? [a-z]+$"
	]
]

structs=["SUSTANTIVO + PREDICADO",
	"SUSTANTIVO + ES/SON + SUSTANTIVO + DE + SUSTANTIVO",
	"CUANTIFICADOR + SUSTANTIVO + QUE + PREDICADO + ES + SUSTANTIVO/ADJETIVO",
	"CUANTIFICADOR + SUSTANTIVO + Y/O + SUSTANTIVO + VERBO",
	"CUANTIFICADOR + SUSTANTIVO + PREDICADO + Y + CUANTIFICADOR + SUSTANTIVO + PREDICADO"
]

exampleLabels=[
	[
		"Carlos juega",
		"Maria baila",
		"Alberto no respira",
		"Firulais no ladra",
		"Juan no estudia"
	],
	[
		"El perro no es hermano de el gato",
		"Itzayana no es madre de Melisa",
		"Juan no es padre de Juanito",
		"Alberto es gemelo de Andres",
		"La abeja es prima de la hormiga"
	],
	[
		"Todo perro que es negro es macho",
		"Algun hongo que es morado es venenoso",
		"No todo gato que camina es real",
		"Ningun animal que salta es elefante",
		"Ningun auto que funciona es chatarra"	
	],
	[
		"Todo estudiante y profesor bailan",
		"Algun perro o gato canta",
		"No todo hombre y mujer respiran",
		"No todo animal y planta vive",
		"Ningun ingeniero o profesionista trabaja"
	],
	[
		"Algun perro es verde y todo gato es azul",
		"Ningun animal canta y ningun ave vuela",
		"Todo pinguino es tierno y todo gato es cruel",
		"No todo hombre es padre y no toda mujer es madre",	
		"No todo libro es bueno y ninguna pelicula es mala"
	]
]

rules=[
	[
		"Un predicado puede ser un verbo o un 'es'+adjetivo o un 'es'+sustantivo.",
		"Se niega escribiendo 'no' antes del predicado."
	],
	[
		"Un predicado puede ser un verbo o un 'es'+adjetivo o un 'es'+sustantivo.",
		"Se niega escribiendo 'no' antes del 'es'/'son'.",
		"No se aceptan contracciones como 'del'."
	],
	[
		"Un predicado puede ser un verbo o un 'es'+adjetivo o un 'es'+sustantivo.",
		"El cuantificador puede ser 'todo'/'toda' o 'algun'/'alguna'.",
		"Se niega usando como cuantificador 'no todo'/'no toda' o 'ningun'/'ninguna'."
	],
	[
		"El cuantificador puede ser 'todo'/'toda' o 'algun'/'alguna'.",
		"Se niega usando como cuantificador 'no todo'/'no toda' o 'ningun'/'ninguna'.",
		"Si el cuantificador es 'todo'/'toda' se debe usar 'y', si es 'ningun'/'ninguna' se debe usar 'o'."
	],
	[
		"Un predicado puede ser un verbo o un 'es'+adjetivo o un 'es'+sustantivo.",
		"El cuantificador puede ser 'todo'/'toda' o 'algun'/'alguna'.",
		"Se niega usando como cuantificador 'no todo'/'no toda' o 'ningun'/'ninguna'.",
		"Para negar AMBOS cuantificadores deben estar negados."
	]
]

master=Tk()

frame=Frame(master,width=100,height=150,padx=10,pady=10)
frame.grid(row=0,column=0,sticky="nsew")

title=Label(frame,text="Estructuras",width=85)
title.grid(sticky="nsew",columnspan=2)
warn=Label(frame,text="No se aceptan entradas de texto con 'ñ' ni caracteres con acentos ni diéresis.",fg="red").grid(row=1,columnspan=2)

labels=[]
exbuttons=[]
exframes=[]
entries=[]
addedEx=[[],[],[],[],[]]
added=StringVar()
addedtrad=[]

for i in range(0,5):
	exbuttons.append(Button(frame,text="Estructura "+str(i+1),command=lambda i=i:raise_frame(i)))
	exbuttons[i].grid(row=i+2,columnspan=2)
	exframes.append(Frame(master,width=100,height=150,padx=10,pady=10))
	exframes[i].grid(row=0,column=0,sticky="nsew")
	Label(exframes[i],text="Estructura "+str(i+1),width=85).grid(column=0,columnspan=2)
	Label(exframes[i],text=structs[i]).grid(row=1,column=0,columnspan=2)
	entries.append(StringVar())
	for j in range(0,5):
		Label(exframes[i],text=exampleLabels[i][j]).grid(row=(j+2),column=0,sticky="e")
		Label(exframes[i],text=check_regexEx(i,j),fg="red").grid(row=(j+2),column=1,sticky="w")
	for j in range(0,len(rules[i])):
		Label(exframes[i],text=rules[i][j],fg="blue").grid(row=(j+7),column=0,columnspan=2)
	Entry(exframes[i],textvariable=entries[i],width=45).grid(row=(7+len(rules[i])),column=0,columnspan=2)
	Button(exframes[i],text="Agregar",command=lambda i=i:check_regex(i)).grid(row=(8+len(rules[i])),column=0,sticky="e")
	Button(exframes[i],text="Regresar",command=main_frame).grid(row=(8+len(rules[i])),column=1,sticky="w")

Label(frame,text="Agregar ejemplo de cualquier estructura:").grid(row=8,columnspan=2)
Entry(frame,textvariable=added,width=45).grid(row=9,columnspan=2)
Button(frame,text="Agregar",command=lambda:add_any()).grid(row=10,columnspan=2)
labelAny=Label(frame,text="")
labelAnyStr=Label(frame,text="")
labelAnyTrad=Label(frame,text="",fg="red")

frame.tkraise()

mainloop()