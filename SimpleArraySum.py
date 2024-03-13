import os
import random
import re
import sys

def simpleArraySum(ar):
   # Write your code here
    if len(ar) <= 0 or len(ar) >= 1000:
        raise ValueError
        
    total=sum(ar)
    
    return total
if __name__ == '__main__':
    
    ar_count = int(input("Ingrese el tamaño de la matriz: ").strip())

    ar = list(map(int, input("Ingrese los elementos de la matriz separados por espacios: ").rstrip().split()))

    result = simpleArraySum(ar)

    print("La suma de los elementos del array es:", result)