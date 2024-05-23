def polinomio_1_grau(a, b, x):
    resultado = (a*x) + b
    print(f'p({x}) = {resultado}')

#polinomio_1_grau(2,1,0)

def polinomio_2_grau(a, b, c, x):
    #desenvolva o cálculo necessário
    resultado = (a * (x**2)) + (b*x) + c
    print(f'p({x}) = {resultado}')
    
polinomio_2_grau(2,3,1,2)