#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from exerciceA import frequence

# TODO: Définissez vos fonction ici
def VolumeMasse(a, b, c, massevolumique):

    V = 4/3 * (math.pi * a * b * c)
    masse = massevolumique * V
    tuple = (V, masse)
    return tuple

def frequence

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(VolumeMasse(1,2,3,5))

