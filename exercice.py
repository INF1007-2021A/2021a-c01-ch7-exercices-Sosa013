#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from exerciceA import frequence
import sys
sys.path.insert(0,"C:\\Users\aniyo\OneDrive\Documents\GitHub\exercice chap 6 (en devoir) inf1007\2021a-c01-ch6-1-exercices-Sosa013\exerciceA.py")
from turtle import *
# TODO: Définissez vos fonction ici
def VolumeMasse(a, b, c, massevolumique):

    V = 4/3 * (math.pi * a * b * c)
    masse = massevolumique * V
    tuple = (V, masse)
    return tuple


def draw_tree():
    setheading(90)
    color("brown")


    #appeler fonction recursive

    draw_branch(70,7,35)

    done()

def draw_branch(branch_len,pen_size, angle):
    if branch_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(VolumeMasse(1,2,3,5))
    print((lambda sentence: sorted(frequence(sentence).items(),key=lambda x:x[1])[-1][0])("je suis une phrase"))
    draw_tree()