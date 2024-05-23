import numpy as np

def funcao_exponencial(a, b, x):
    #use a função disponível em Numpy
    y = np.power(a, x) + b
    print(f"f({x}) = {y}")

funcao_exponencial(2,1,2)