# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:28:09 2017

@author: audren
"""

x=float(input("enter a number for x: "))
y=float(input("enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is", x/y)
    elif x<y:
        print ("x is smaller")
        else :
            print ("y is smaller")
            
print("thanks")

# c'est comme si le else ne reconnaissait pas le premier if , et comparé à la vidéo le elif devrait être a la meme abscisse que le premier if
# pb: même en rentrant des valeur adequate pour x et y ça ne prend pas else