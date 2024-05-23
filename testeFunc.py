import numpy as np

def resolver_inequacao_2_grau(a, b, c, d):
    #desenvolva o cálculo necessário considerando as 3 situações do delta
    #considere somente raízes reais
    #quando não houver raíz, retorne lista vazia
    #OBS: considere para delta= b**2 - 4*a*(c - d)
    valoresX = []

    c -= d

    delta = b**2 - 4 * a * c
    print('delta = ', delta)
    if delta < 0:
        print(f'Não há valores reais para x! valores de x: {valoresX}')
    elif delta == 0:
        x = -b/2 * a
        print(f'{x} > 0')
    elif delta > 0:
        x1 = (-b + np.sqrt(delta))/ (2 * a)
        x2 = (-b - np.sqrt(delta))/ (2 * a)
        valoresX.append(x1)
        valoresX.append(x2)
        print(f"{valoresX} > 0")

resolver_inequacao_2_grau(1, -5, 6, 0)
#resolver_inequacao_2_grau(1, -4, -4, -8)
#resolver_inequacao_2_grau(1, 2, 15, 10)
