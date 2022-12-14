import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
x_1 = int(input("Ingresa la posicion en que empieza el canguro 1"))
v_1 = int(input("Ingresa la velocidad a la que se mueve el canguro 1"))
x_2 = int(input("Ingresa la posicion en que empieza el canguro 2"))
v_2 = int(input("Ingresa la velocidad a la que se mueve el canguro 2"))

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 < x2 and v1 > v2:
        return True
    elif x1 > x2 and v1 < v2:
        return True
    else:
        return False

print (kangaroo(x_1,v_1,x_2,v_2))