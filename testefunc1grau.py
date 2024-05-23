def resolver_inequacao_1_grau(a, b, c):
    #desenvolva o cálculo necessário
    if a == 0:
        print('valor inválido para a')
    ld = c - b 
   
    #Se for negativo

    resultado = ld/a
    print(f'x > {resultado}')
resolver_inequacao_1_grau(3,3,3)