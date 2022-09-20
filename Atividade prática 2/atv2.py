import matplotlib.pyplot as plt
from copy import deepcopy as copia
import math
import numpy as np
lena = plt.imread("lena_gray.bmp")
lenaRuido = plt.imread("lena_ruido.bmp")
formas=plt.imread("formas.bmp")
quadro=plt.imread('quadro.png')

def media(imagem):
    resultado=copia(imagem)
    dimensoes=imagem.shape  
    i=0
    j=0
    for i in range (dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
   
            valor=0
            if(i==0 and j==0):
                valor=(
                    int(imagem[i][j])     +int(imagem[i][j+1]) 
                    +int(imagem[i+1][j])  +int(imagem[i+1][j+1]))/9
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    int(imagem[i][j-1])      +int(imagem[i][j])    +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])    +int(imagem[i+1][j])  +int(imagem[i+1][j+1]))/9
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(imagem[i-1][j])   +int(imagem[i-1][j+1])+
                    int(imagem[i][j])    +int(imagem[i][j+1])+
                    int(imagem[i+1][j])  +int(imagem[i+1][j+1]))/9
                             
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1]) +int(imagem[i-1][j]) +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])   +int(imagem[i][j])   +int(imagem[i][j+1]))
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1])    +int(imagem[i-1][j])+
                    int(imagem[i][j-1])      +int(imagem[i][j])+
                    int(imagem[i+1][j-1])    +int(imagem[i+1][j]))
                    
            else:
                valor=(
                    int(imagem[i-1][j-1])    +int(imagem[i-1][j])  +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])      +int(imagem[i][j])    +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])    +int(imagem[i+1][j])  +int(imagem[i+1][j+1]))

    return resultado


def laplaciano(imagem):
    imgCopia=mediana(imagem)
    dimensoes=imagem.shape  
    i=0
    j=0
    for i in range (dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
   
            valor=0
            if(i==0 and j==0):
                valor=(
                    8*int(imagem[i][j])     -1*int(imagem[i][j+1]) 
                    -1*int(imagem[i+1][j])  -1*int(imagem[i+1][j+1]))
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i][j-1])      +8*int(imagem[i][j])    -1*int(imagem[i][j+1])
                    -1*int(imagem[i+1][j-1])    -1*int(imagem[i+1][j])  -1*int(imagem[i+1][j+1]))
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    -1*int(imagem[i-1][j])  -1*int(imagem[i-1][j+1])
                    +8*int(imagem[i][j])    -1*int(imagem[i][j+1])
                    -1*int(imagem[i+1][j])  -1*int(imagem[i+1][j+1]))
                             
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i-1][j-1]) -1*int(imagem[i-1][j]) -1*int(imagem[i-1][j+1])
                    -1*int(imagem[i][j-1])   +8*int(imagem[i][j])   -1*int(imagem[i][j+1]))
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])
                    -1*int(imagem[i][j-1])      +8*int(imagem[i][j])
                    -1*int(imagem[i+1][j-1])    -1*int(imagem[i+1][j]))
                    
            else:
                valor=(
                    -1*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])  -1*int(imagem[i-1][j+1])
                    -1*int(imagem[i][j-1])      +8*int(imagem[i][j])    -1*int(imagem[i][j+1])
                    -1*int(imagem[i+1][j-1])    -1*int(imagem[i+1][j])  -1*int(imagem[i+1][j+1]))
                
            if(valor<65):               
                imgCopia[i][j]=0
            else:
                imgCopia[i][j]=(127+valor)/2    
                
    return imgCopia

    filtro=laplaciano(original)
    dimensoes=original.shape
    resultado=copia(original)
    i=0
    j=0
    for i in range (dimensoes[0]-1): 
        for j in range(dimensoes[1]-1):
            resultado[i][j]=int(original[i][j])-int(filtro[i][j])
    return resultado                

def unsharpMasking(imagem):
    borrada=copia(imagem)

    dimensoes=imagem.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            borrada[i][j]=0
            if(i==0 and j==0):
                valor=(
                    int(imagem[i][j])   +int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +int(imagem[i+1][j+1]))*(1/9)
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))*(1/9)
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(imagem[i-1][j]) +int(imagem[i-1][j+1])+
                    int(imagem[i][j])   +int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +int(imagem[i+1][j+1]))*(1/9)           
            
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])    +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1]))*(1/9)

            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])+
                    int(imagem[i][j-1])     +int(imagem[i][j])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j]))*(1/9)
                    
            else:
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])    +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))*(1/9)
            borrada[i][j]=valor
    mascara=copia(imagem)
    final=copia(imagem)

    for i in range(dimensoes[0]):
        for j in range(dimensoes[1]):
            mascara[i][j]=0
            final[i][j]=0
            mascara[i][j]=int(imagem[i][j]) -int(borrada[i][j])
            final[i][j]=(int(imagem[i][j])  +int(mascara[i][j]))
    return final

def highboost(imagem,k):
    borrada=copia(imagem) 
    dimensoes=imagem.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            borrada[i][j]=0
            if(i==0 and j==0):
                valor=(
                    int(imagem[i][j])   +int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +int(imagem[i+1][j+1]))*(1/9)
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))*(1/9)
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(imagem[i-1][j]) +int(imagem[i-1][j+1])+
                    int(imagem[i][j])   +int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +int(imagem[i+1][j+1]))*(1/9)
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])    +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1]))*(1/9)
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])+
                    int(imagem[i][j-1])     +int(imagem[i][j])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j]))*(1/9)
                    
            else:
                valor=(
                    int(imagem[i-1][j-1])   +int(imagem[i-1][j])    +int(imagem[i-1][j+1])+
                    int(imagem[i][j-1])     +int(imagem[i][j])      +int(imagem[i][j+1])+
                    int(imagem[i+1][j-1])   +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))*(1/9)
            borrada[i][j]=valor
    mascara=copia(imagem)
    final=copia(imagem)

    for i in range(dimensoes[0]):
        for j in range(dimensoes[1]):
            mascara[i][j]=0
            final[i][j]=0
            mascara[i][j]=int(imagem[i][j])-int(borrada[i][j])
            final[i][j]=int(imagem[i][j])+(k*int(mascara[i][j]))
    return final

def prewitt(imagem):
    filtragem1=copia(imagem)
    filtragem2=copia(imagem) 
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0

    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            filtragem1[i][j]=0
            filtragem2[i][j]=0
            if(i==0 and j==0):
                valor=(int(imagem[i+1][j]) +int(imagem[i+1][j+1]))/6
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(int(imagem[i+1][j-1]) +int(imagem[i+1][j]) +int(imagem[i+1][j+1]))/6
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    -1*int(imagem[i-1][j])  -1*int(imagem[i-1][j+1])
                    +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))/6
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(-1*int(imagem[i-1][j-1]) -1*int(imagem[i-1][j]) -1*int(imagem[i-1][j+1]))/6
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])+
                    int(imagem[i+1][j-1])       +int(imagem[i+1][j]))/6
                    
            else:
                valor=(
                    -1*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])  -1*int(imagem[i-1][j+1])+
                    int(imagem[i+1][j-1])       +int(imagem[i+1][j])    +int(imagem[i+1][j+1]))/6
            
            filtragem1[i][j]=valor
            valor=0

            if(i==0 and j==0):
                valor=(int(imagem[i][j+1])+int(imagem[i+1][j+1]))/6
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1])
                    -1*int(imagem[i+1][j-1])    +int(imagem[i+1][j+1]))/6
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(imagem[i-1][j+1])+
                    int(imagem[i][j+1])+
                    int(imagem[i+1][j+1]))/6
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i-1][j-1])    +int(imagem[i-1][j+1])
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1]))/6
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i-1][j-1])
                    -1*int(imagem[i][j-1])
                    -1*int(imagem[i+1][j-1]))/6
                    
            else:
                valor=(
                    -1*int(imagem[i-1][j-1])    +int(imagem[i-1][j+1])
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1])
                    -1*int(imagem[i+1][j-1])    +int(imagem[i+1][j+1]))/6
            filtragem2[i][j]=valor

    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            resultado[i][j]=int(filtragem1[i][j])+int(filtragem2[i][j])
    return resultado

def sobel(imagem):
    filtragem1=copia(imagem)
    filtragem2=copia(imagem) 
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            
            if(i==0 and j==0):
                valor=(
                    int(imagem[i][j+1])
                    -1*int(imagem[i+1][j]))/8
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1])+
                    -2*int(imagem[i+1][j-1])    -1*int(imagem[i+1][j]))/8
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(imagem[i-1][j]) +2*int(imagem[i-1][j+1])+
                    +int(imagem[i][j+1])
                    -1*int(imagem[i+1][j]))/8
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j])     +2*int(imagem[i-1][j+1])+
                    -1*int(imagem[i][j-1])  +int(imagem[i][j+1]))/8
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    int(imagem[i-1][j])+
                    -1*int(imagem[i][j-1])
                    -2*int(imagem[i+1][j-1]))/8
                    
            else:
                valor=(
                    int(imagem[i-1][j])         +2*int(imagem[i-1][j+1])
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1])+
                    -2*int(imagem[i+1][j-1])    -1*int(imagem[i+1][j]))/8
            filtragem1[i][j]=valor
            valor=0

            if(i==0 and j==0):
                valor=(
                    int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +2*int(imagem[i+1][j+1]))/8
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    -1*int(imagem[i][j-1])  +int(imagem[i][j+1])+
                    int(imagem[i+1][j])     +2*int(imagem[i+1][j+1]))/8
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    -1*int(imagem[i-1][j])+
                    int(imagem[i][j+1])+
                    int(imagem[i+1][j]) +2*int(imagem[i+1][j+1]))/8
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    -2*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1]))/8
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    -2*int(imagem[i-1][j-1]) -1*int(imagem[i-1][j])+
                    -1*int(imagem[i][j-1])+
                    int(imagem[i+1][j]))/8
                    
            else:
                valor=(
                    -2*int(imagem[i-1][j-1])    -1*int(imagem[i-1][j])
                    -1*int(imagem[i][j-1])      +int(imagem[i][j+1])+
                    -1*int(imagem[i+1][j])      +2*int(imagem[i+1][j+1]))/8
            filtragem2[i][j]=valor

    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            resultado[i][j]=int(filtragem1[i][j])+int(filtragem2[i][j])
    return resultado

def filtroQualquer(imagem,filtro,fatorFiltro):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0
    
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            
            if(i==0 and j==0):
                valor=(
                    int(filtro[1][1])*int(imagem[i][j])   + int(filtro[1][2])*int(imagem[i][j+1])+
                    int(filtro[2][1])*int(imagem[i+1][j]) + int(filtro[2][2])*int(imagem[i+1][j+1]))*(1/fatorFiltro)
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                valor=(
                    int(filtro[1][0])*int(imagem[i][j-1])   + int(filtro[1][1])*int(imagem[i][j])   + int(filtro[1][2])*int(imagem[i][j+1])+
                    int(filtro[2][0])*int(imagem[i+1][j-1]) + int(filtro[2][1])*int(imagem[i+1][j]) + int(filtro[2][2])*int(imagem[i+1][j+1]))*(1/fatorFiltro)
                
            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                valor=(
                    int(filtro[0][1])*int(imagem[i-1][j]) + int(filtro[0][2])*int(imagem[i-1][j+1])+
                    int(filtro[1][1])*int(imagem[i][j])   + int(filtro[1][2])*int(imagem[i][j+1])+
                    int(filtro[2][1])*int(imagem[i+1][j]) + int(filtro[2][2])*int(imagem[i+1][j+1]))*(1/fatorFiltro)                
            
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                valor=(
                    int(filtro[0][0])*int(imagem[i-1][j-1]) + int(filtro[0][1])*int(imagem[i-1][j]) + int(filtro[0][2])*int(imagem[i-1][j+1])+
                    int(filtro[1][0])*int(imagem[i][j-1])   + int(filtro[1][1])*int(imagem[i][j])   + int(filtro[1][2])*int(imagem[i][j+1]))*(1/fatorFiltro) 
                
            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                valor=(
                    int(filtro[0][0])*int(imagem[i-1][j-1]) + int(filtro[0][1])*int(imagem[i-1][j])+
                    int(filtro[1][0])*int(imagem[i][j-1])   + int(filtro[1][1])*int(imagem[i][j])+
                    int(filtro[2][0])*int(imagem[i+1][j-1]) + int(filtro[2][1])*int(imagem[i+1][j]))*(1/fatorFiltro) 
                    
            else:
                valor=(
                    int(filtro[0][0])*int(imagem[i-1][j-1]) + int(filtro[0][1])*int(imagem[i-1][j]) + int(filtro[0][2])*int(imagem[i-1][j+1])+
                    int(filtro[1][0])*int(imagem[i][j-1])   + int(filtro[1][1])*int(imagem[i][j])   + int(filtro[1][2])*int(imagem[i][j+1])+
                    int(filtro[2][0])*int(imagem[i+1][j-1]) + int(filtro[2][1])*int(imagem[i+1][j]) + int(filtro[2][2])*int(imagem[i+1][j+1]))*(1/fatorFiltro) 
            resultado[i][j]=valor

    return resultado

def mediana(imagem):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0
    
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            vetorMediana=[0,0,0,0,0,0,0,0,0]
            if(i==0 and j==0):
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[5]=int(imagem[i][j+1])
                vetorMediana[7]=int(imagem[i+1][j])
                vetorMediana[8]=int(imagem[i+1][j+1])
                               
            elif(i==0 and j>0 and j<dimensoes[1]-1 ):
                vetorMediana[3]=int(imagem[i][j-1])
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[5]=int(imagem[i][j+1])
                vetorMediana[6]=int(imagem[i+1][j-1]) 
                vetorMediana[7]=int(imagem[i+1][j])
                vetorMediana[8]=int(imagem[i+1][j+1])

            elif(i>0 and i<dimensoes[0]-1 and j==0 ):
                vetorMediana[1]=int(imagem[i-1][j])
                vetorMediana[2]=int(imagem[i-1][j+1])
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[5]=int(imagem[i][j+1])
                vetorMediana[7]=int(imagem[i+1][j])
                vetorMediana[8]=int(imagem[i+1][j+1])
                
            elif(i==dimensoes[0]-1 and j!=dimensoes[1]-1 ):
                vetorMediana[0]=int(imagem[i-1][j-1])
                vetorMediana[1]=int(imagem[i-1][j])
                vetorMediana[2]=int(imagem[i-1][j+1])
                vetorMediana[3]=int(imagem[i][j-1])
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[5]=int(imagem[i][j+1])

            elif(i!=dimensoes[0]-1 and j==dimensoes[1]-1 ):
                vetorMediana[0]=int(imagem[i-1][j-1])
                vetorMediana[1]=int(imagem[i-1][j])
                vetorMediana[3]=int(imagem[i][j-1])
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[6]=int(imagem[i+1][j-1]) 
                vetorMediana[7]=int(imagem[i+1][j])
                   
            else:
                vetorMediana[0]=int(imagem[i-1][j-1])
                vetorMediana[1]=int(imagem[i-1][j])
                vetorMediana[2]=int(imagem[i-1][j+1])
                vetorMediana[3]=int(imagem[i][j-1])
                vetorMediana[4]=int(imagem[i][j])
                vetorMediana[5]=int(imagem[i][j+1])
                vetorMediana[6]=int(imagem[i+1][j-1]) 
                vetorMediana[7]=int(imagem[i+1][j])
                vetorMediana[8]=int(imagem[i+1][j+1])
            vetorMediana.sort()
            resultado[i][j]=vetorMediana[4]
            
    return resultado        

def uniao(imagem1,imagem2):
    resultado=copia(imagem1)
    dimensoes=imagem1.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            resultado[i][j]=max(int(imagem1[i][j]),int(imagem2[i][j]))                                  
    return resultado

def interseccao(imagem1,imagem2):
    resultado=copia(imagem1)
    dimensoes=resultado.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            resultado[i][j]=min(int(imagem1[i][j]),int(imagem2[i][j]))

    return resultado

def diferenca(imagem1,imagem2):
    resultado=copia(imagem1)
    dimensoes=imagem1.shape
    i=0
    j=0

    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            resultado[i][j]=int(imagem1[i][j])-int(imagem2[i][j])        
           
    return resultado

def dilatacao(imagem,estruturante,centro):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    centrox=centro[0]
    centroy=centro[1]
    valorCentro=estruturante[centrox][centroy]
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):            
            valor=imagem[i][j]            
            if((valor==valorCentro)):
                resultado[i-1][j-1] =resultado[i-1][j-1] + int(estruturante[0][0])
                resultado[i-1][j]   =resultado[i-1][j]   + int(estruturante[0][1])
                resultado[i-1][j+1] =resultado[i-1][j+1] + int(estruturante[0][2])
                resultado[i][j-1]   =resultado[i][j-1]   + int(estruturante[1][0])
                resultado[i][j]     =resultado[i][j]     + int(estruturante[1][1])
                resultado[i][j+1]   =resultado[i][j+1]   + int(estruturante[1][2])
                resultado[i+1][j-1] =resultado[i+1][j-1] + int(estruturante[2][0])
                resultado[i+1][j]   =resultado[i+1][j]   + int(estruturante[2][1])
                resultado[i+1][j+1] =resultado[i+1][j+1] + int(estruturante[2][2])

    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            if(resultado[i][j]<4):
                resultado[i][j]=0
            else:
                resultado[i][j]=255             
    return resultado

def erosao(imagem,estruturante,centro):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    centrox=centro[0]
    centroy=centro[1]
    valorCentro=estruturante[centrox][centroy]
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):            
            valor=imagem[i][j]            
            if((valor==valorCentro)):
                resultado[i-1][j-1] =resultado[i-1][j-1] - int(estruturante[0][0])
                resultado[i-1][j]   =resultado[i-1][j]   - int(estruturante[0][1])
                resultado[i-1][j+1] =resultado[i-1][j+1] - int(estruturante[0][2])
                resultado[i][j-1]   =resultado[i][j-1]   - int(estruturante[1][0])
                resultado[i][j]     =resultado[i][j]     - int(estruturante[1][1])
                resultado[i][j+1]   =resultado[i][j+1]   - int(estruturante[1][2])
                resultado[i+1][j-1] =resultado[i+1][j-1] - int(estruturante[2][0])
                resultado[i+1][j]   =resultado[i+1][j]   - int(estruturante[2][1])
                resultado[i+1][j+1] =resultado[i+1][j+1] - int(estruturante[2][2])
    
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            if(resultado[i][j]<4):
                resultado[i][j]=0
            else:
                resultado[i][j]=255                        
    return resultado

def abertura(imagem,estruturante,centro):
    erodida=erosao(imagem, estruturante, centro)
    dilatada=dilatacao(erodida, estruturante, centro)
    return dilatada

def fechamento(imagem,estruturante,centro):
    dilatada=dilatacao(imagem, estruturante, centro)
    erodida=erosao(dilatada, estruturante, centro)
    return erodida

def preencherBuracos(imagem,cor):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1): 
            pixel=imagem[i][j] 
            if(pixel[0]==cor[0] and pixel[1]==cor[1] and pixel[2]==cor[2] 
                and i<dimensoes[0]-2 and j<dimensoes[1]-2
                and i>0 and j>0):
                resultado[i-2][j-2] =cor             
                resultado[i-2][j-1] =cor
                resultado[i-2][j]   =cor
                resultado[i-2][j+1] =cor
                resultado[i-2][j+2] =cor             

                resultado[i-1][j-2] =cor             
                resultado[i-1][j-1] =cor
                resultado[i-1][j]   =cor
                resultado[i-1][j+1] =cor
                resultado[i-1][j+2] =cor

                resultado[i][j-2]   =cor             
                resultado[i][j-1]   =cor
                resultado[i][j]     =cor
                resultado[i][j+1]   =cor
                resultado[i][j+2]   =cor

                resultado[i+1][j-2] =cor             
                resultado[i+1][j-1] =cor
                resultado[i+1][j]   =cor
                resultado[i+1][j+1] =cor
                resultado[i+1][j+2] =cor
                
                resultado[i+2][j-2] =cor             
                resultado[i+2][j-1] =cor
                resultado[i+2][j]   =cor
                resultado[i+2][j+1] =cor
                resultado[i+2][j+2] =cor

    return resultado

def apagarCor(imagem,cor):
    resultado=copia(imagem)
    dimensoes=imagem.shape
    i=0
    j=0
    for i in range(dimensoes[0]-1):
        for j in range(dimensoes[1]-1):
            pixel=imagem[i][j]
            if(pixel[0]==cor[0] and pixel[1]==cor[1] and pixel[2]==cor[2]):
                resultado[i][j]=[1,1,1,1]
    return resultado


plt.imshow(laplaciano(lena),cmap='gray')
plt.show()

plt.imshow(unsharpMasking(lena),cmap='gray')
plt.show()

plt.imshow(highboost(lena,3),cmap='gray')
plt.show()

plt.imshow(prewitt(lena),cmap='gray')
plt.show()

plt.imshow(sobel(lena),cmap='gray')
plt.show()



segA=[[0,1,0],[1,1,1],[0,1,0]]
segAFator=5
segB=[[1,1,1],[1,1,1],[1,1,1]]
segBFator=9
segC=[[1,3,1],[3,16,3],[1,3,1]]
segCFator=32
segD=[[0,1,0],[1,4,1],[0,1,0]]
segDFator=8
laplace=[[1,1,1],[1,-8,1],[1,1,1]]
fatorLaplace=8

plt.imshow(filtroQualquer(lenaRuido, segA, segAFator),cmap='gray')
plt.show()
plt.imshow(filtroQualquer(lenaRuido, segB, segBFator),cmap='gray')
plt.show()
plt.imshow(filtroQualquer(lenaRuido, segC, segCFator),cmap='gray')
plt.show()
plt.imshow(filtroQualquer(lenaRuido, segD, segDFator),cmap='gray')
plt.show()

plt.imshow(mediana(lenaRuido),cmap='gray')
plt.show()


plt.imshow(uniao(lena,lenaRuido),cmap="gray")
plt.show()
plt.imshow(diferenca(lena,lenaRuido),cmap="gray")
plt.show()
plt.imshow(interseccao(lena,lenaRuido),cmap="gray")
plt.show()


estruturante=np.array([[0,255,0],[255,255,255],[0,255,0]])
centro=np.array([1,1])

dilatacao1=dilatacao(formas, estruturante, centro)
plt.imshow(dilatacao1,cmap="gray")
plt.show()

erosao1=erosao(formas, estruturante, centro)
plt.imshow(erosao1,cmap="gray")
plt.show()

plt.imshow(abertura(formas, estruturante, centro),cmap="gray")
plt.show()

plt.imshow(fechamento(formas, estruturante, centro),cmap="gray")
plt.show()

preto   =np.array([0,0,0,1])
vermelho=np.array([1,0,0,1])
verde   =np.array([0,1,0,1])
azul    =np.array([0,0,1,1])
amarelo =np.array([1,1,0,1])
#5a
pretoPreenchido=preencherBuracos(quadro, preto)

plt.imshow(pretoPreenchido)
plt.show()

#5b
plt.imshow(apagarCor(pretoPreenchido, preto))
plt.show()