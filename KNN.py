# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:56:32 2016

@author: crush
"""

import csv
import math
import OCR
import matplotlib.image as mpimg
f= open('dataset.csv')
lns=csv.reader(f)
print("Cual es el nombre de la imagen que se va clasificar: ",end="")
rutaImagen=input()
img=mpimg.imread(rutaImagen)
dataset=list(lns)

distancias=[0,0]
beca=[0,0]
contador=0

for i in dataset:
    
    dataset[contador][0]=float(dataset[contador][0])
    dataset[contador][1]=float(dataset[contador][1])
    dataset[contador][2]=float(dataset[contador][2])
    dataset[contador][3]=float(dataset[contador][3])
    dataset[contador][4]=float(dataset[contador][4])
    dataset[contador][5]=float(dataset[contador][5])
    dataset[contador][6]=float(dataset[contador][6])
    dataset[contador][7]=float(dataset[contador][7])
    dataset[contador][8]=float(dataset[contador][8])
    dataset[contador][9]=float(dataset[contador][9])
    dataset[contador][10]=float(dataset[contador][10])
    dataset[contador][11]=float(dataset[contador][11])
    dataset[contador][12]=float(dataset[contador][12])
    dataset[contador][13]=float(dataset[contador][13])
    dataset[contador][14]=float(dataset[contador][14])
    dataset[contador][15]=float(dataset[contador][15])
    dataset[contador][16]=float(dataset[contador][16])
    contador+=1
    
Matrix=dataset
[fila,columna]=img.shape
dato1=OCR.Relacion(img)
dato2=OCR.Area(img)
[dato3,negro1]=OCR.lineaVertical(fila,columna,img)
[dato4,negro2]=OCR.lineaHorizontal(fila,columna,img)
[x1,x2,x3,x4]=OCR.lineasVerticalesyHorizontales2(img)
dato5=OCR.lineasHorizontales5(img)
dato6=OCR.lineasVerticales5(img)
dato7=OCR.lineasHorizontales3(img)
dato8=OCR.lineasVerticales3(img)
dato9=x1+x2 #cuantos "1" encontre en los dos cortes 
dato10=x3+x4# cuantos cambios de valor encontre en los dos cortes 
dato11=negro1
dato12=negro2
dato13=(dato3+dato4)/fila # relacion entre los cambios quedetecte en una cruz en la imagen entre las filas 
[dato14,dato15]=OCR.pixelesNegrosYBlancos(fila,columna,img)


prediccion=[dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15] 
contador=0



for i in Matrix:# realizo la distancia euclidiana
    aux=0
    aux=(pow((Matrix[contador][0]-dato1),2))+ (pow((Matrix[contador][1]-dato2),2))+ (pow((Matrix[contador][2]-dato3),2))+ (pow((Matrix[contador][3]-dato4),2))+(pow((Matrix[contador][4]-dato5),2)) +(pow((Matrix[contador][5]-dato6),2))
    aux=aux+(pow((Matrix[contador][6]-dato7),2))+ (pow((Matrix[contador][7]-dato8),2))+ (pow((Matrix[contador][8]-dato9),2))+ (pow((Matrix[contador][9]-dato10),2))+(pow((Matrix[contador][10]-dato11),2)) +(pow((Matrix[contador][11]-dato12),2))
    aux=aux+(pow((Matrix[contador][12]-dato13),2))+ (pow((Matrix[contador][13]-dato14),2))+ (pow((Matrix[contador][14]-dato15),2))     
    aux=math.sqrt(aux)
    Matrix[contador].append(aux)
    contador+=1
print(Matrix[0])
Matrix.sort(key=lambda Matrix: Matrix[17])


print("Ingrese el numero de K vecinos: ",end="")
k=input()
k=int(k)
contador0=0
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
contador6=0
contador7=0
contador8=0
contador9=0

print("\tInformacion del dataset ************************\n\n")
print("Numero de instancias: "+str(len(Matrix)))
print("Numero de clases: 10")
print("Nombre de las clases: 0,1,2,3,4,5,6,7,8,9 ")
print("Numero de propiedades por instancia: "+str(len(dataset[0])-2))
print(len(Matrix))
print("\t\tresultados de la clasificacion|||||||||||||||||||||||||\n")
for i in range(0,k):
    print("\n")
    print("Vecino #"+str(i+1))
    print ("\tDistancia euclidiana: "+str(Matrix[i][17])+"\tClase a la que pertenece: "+str(Matrix[i][15])+"Numero de instancia: "+str(Matrix[i][16]))
print("\n")    
no

for i in range  (k):
    
    #print(Matrix[contador][4])
    if Matrix[i][15]==1:
        contador1+=1
    if Matrix[i][15]==2:
        contador2+=1
    if Matrix[i][15]==3:
        contador3+=1
    if Matrix[i][15]==4:
        contador4+=1
    if Matrix[i][15]==5:
        contador5+=1
    if Matrix[i][15]==6:
        contador6+=1
    if Matrix[i][15]==7:
        contador7+=1
    if Matrix[i][15]==8:
        contador8+=1
    if Matrix[i][15]==9:
        contador9+=1
    if Matrix[i][15]==0:
        contador0+=1

totales=[[contador0," es un cero"],[contador1,"El numero es un uno "],[contador2,"El numero es un dos"],[contador3,"El numero es un tres"],[contador4,"El numero es un cuatro"],[contador5,"El numero es un cinco"],[contador6,"El numero es un seis"],[contador7,"El numero es un siete"],[contador8,"El numero es un ocho"],[contador9,"El numero es un nueve"],]

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
for i in range(0,len(totales)):
    print("Se encontraron "+str(totales[i][0])+" resigistros de la clase "+str(i))
totales.sort(key=lambda totales: totales[0])
print("\n\n\resultado de la clasificacion\n\n")
print (totales[9][1])