"Indexação de dados de DRX para uma amostra de NaCl"

import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def identificar_picos():
    """Identifica picos em um padrão de difração de raios X.
    
    Args:
        dados (pd.DataFrame): Padrão de difração de raios X.
        limiar (float): Limiar para identificação de picos.
        
    Returns:
        pd.DataFrame: Picos identificados.
    """
    dados = pd.read_csv(
        'DRX\DADOS\Pratica_DRX\DadosAula-2024-11-01\Sal_Pa20_E2_PIX22Red_HYB_SP4S-E1_DS18-12_M10_SoIncDif04_As168_45V40A_2a140_005_82s_8min.xy', 
        delim_whitespace=True, 
        header=None, 
        names=['2Theta', 'Intensidade'],
    )
        
    dados_x = dados['2Theta']
    dados_y = dados['Intensidade']

    #encontrando os picos
    picos,_=find_peaks(dados_y, height=200)
    
    #Apartir dos picos encontrados, identificar os planos cristalinos
    #encontandos os indices hkl usando a lei de bragg 2dsin(theta)=n*lambda
    #primeiro passos é encontrar o d
    d_1 = []
    for i in range(len(picos)):
        for n in range(1,4):
            d = 1.54*n/(2*np.sin(np.radians(dados_x[picos[i]]/2)))
            
            if n==1:
                d_1.append(d)
            print(f'Pico {i+1} - 2Theta: {dados_x[picos[i]]}, Intensidade: {dados_y[picos[i]]}, d: {d}, ordem de reflexão: {n}')
    # Com o valor de d podemos encontrar os indices hkl, sabendo que a formula é d = a/sqrt(h^2+k^2+l^2) sem saber o valor de a
    # podemos usar a tabela de d do NaCl para encontrar os indices hkl, considerando a reflexão de ordem 1 e supondo que hkl =1
    # podemos encontrar a
    print(f'Os valores de d_1 são {d_1}')
    
    # for i in range(len(d_1)):
    #     hkl = 1
    #     d = d_1[1]
    #     a = d*np.sqrt(hkl**2 + hkl**2 + hkl**2)
    #     print(f'Pico {i+1} - a: {a} este pico foi encontrado usando o valor de d = {d} e hkl = {hkl}')
    #     print(20*'-')
    

    hkl = 1
    d = d_1[0]
    a = d*np.sqrt(hkl**2 + hkl**2 + hkl**2)
    print(f'Pico {1} - a: {a} este pico foi encontrado usando o valor de d = {d} e hkl = {hkl}')
    print(150*'-')
    #sabendo que o valor de a=5.619 \\A podemos encontrar os indices hkl para os outros valores de n e indexar os picos de cada um desses valores
    #para isso vamos usar a formula d = a/sqrt(h^2+k^2+l^2) e a tabela de d do NaCl
    #chamerei os indides de hkl
    for n in range(len(picos)):
        # a=5.619362828509709
        # print(f'Esse é o a {a}')
        hkl=(a/d_1[n])**2
        print(f'Pico {n+1} cuja posição é {d_1[n]} - hkl²: {hkl}')
        

    
    plt.plot(dados_x, dados_y)
    plt.title('Padrão de Difração Do NaCl')
    plt.ylabel('Intensidade')
    plt.xlabel('2Theta')
    plt.scatter(dados_x[picos], dados_y[picos], color='red')
    plt.legend(['Dados', 'Picos'])
    plt.show()
    
    return
    
    
    
identificar_picos()