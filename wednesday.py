from turtle import *
from random import randint

Screen()
bgcolor("black")
pencolor("red", "green", "yellow")
title("wednesday")
speed()


def estrella(longitud):
    for i in range(5):
                 
        forward(longitud)
        right(180 - 36)
        

def espiral_estrellas():
    for i in range(72):
                
        # Estrella de 300 de longitud
        estrella(200)
        # Girar 5 grados
        right(5)
        
# Yo no quiero animaciones

# Dibujar espiral
espiral_estrellas()
# El input es para pausar el programa
input("Presiona Enter para salir...")
