from pymatgen.core import Structure #imporante para a leitura do arquivo CIF
from pymatgen.analysis.diffraction.xrd import XRDCalculator #importante para a simulação de difração de raios-X
import matplotlib.pyplot as plt
import numpy as np


def identificar_picos():
    """Identifica picos em um padrão de difração de raios X.
    
    Args:
        dados de um arquivo CIF.
        
    Returns:
        Plot com os picos indetificados e com os valores de 2Theta e intensidade.
    """
    # Carregar a estrutura a partir do arquivo CIF
    estrutura = Structure.from_file("microscopia_eletronica\CIF_Ag_9008459.cif")

    # Criar um simulador de difração de raios-X
    xrd_calculator = XRDCalculator()


    # Gerar o padrão de difração
    xrd_pattern = xrd_calculator.get_pattern(estrutura)


    # Obter os dados de 2θ e intensidade
    dois_theta = xrd_pattern.x
    intensidade = xrd_pattern.y


    
    
    # Plotar o difratograma
    plt.figure(figsize=(8, 6))
    plt.scatter(dois_theta, intensidade, label="Difratograma Simulado", color="blue")
    plt.xlabel("2θ (graus)")
    plt.ylabel("Intensidade (u.a.)")
    plt.title("Difratograma de Raios X Simulado")
    plt.legend()
    plt.grid(True)
    plt.show()    
    
    # identificar os planos cristalinos
    #encontandos os indices hkl usando a lei de bragg 2dsin(theta)=n*lambda
    # #primeiro passos é encontrar o d
    d_1 = []
    for i in range(len(intensidade)):
        for n in range(1,4):
            d = 1.54*n/(2*np.sin(np.radians(dois_theta[i]/2)))
            
            if n==1:
                d_1.append(d)
            print(f'Pico {i+1} - 2Theta: {dois_theta[i]}, Intensidade: {intensidade[i]}, d: {d}, ordem de reflexão: {n}')
    # # Com o valor de d podemos encontrar os indices hkl, sabendo que a formula é d = a/sqrt(h^2+k^2+l^2) sem saber o valor de a
    # # podemos usar a tabela de d do NaCl para encontrar os indices hkl, considerando a reflexão de ordem 1 e supondo que hkl =1
    # # podemos encontrar a
    print(f'Os valores de d_1 são {d_1}')
    
    
    hkl = 1
    d = d_1[0]
    a = d*np.sqrt(hkl**2 + hkl**2 + hkl**2)
    print(f'Pico {1} - a: {a} este pico foi encontrado usando o valor de d = {d} e hkl = {hkl}')
    print(150*'-')
    #sabendo que o valor de a=5.619 \\A podemos encontrar os indices hkl para os outros valores de n e indexar os picos de cada um desses valores
    #para isso vamos usar a formula d = a/sqrt(h^2+k^2+l^2) e a tabela de d do NaCl
    #chamerei os indides de hkl
    for n in range(len(intensidade)):
        # a=5.619362828509709
        hkl=(a/d_1[n])**2
        print(f'Pico {n+1} cuja posição é {d_1[n]:.2f} - hkl²: {hkl:.2f}')
        

    
    plt.scatter(dois_theta, intensidade)
    plt.title('Padrão de Difração Do Ag')
    plt.ylabel('Intensidade')
    plt.xlabel('2Theta')
    # plt.scatter(dados_x[picos], dados_y[picos], color='red')
    plt.legend(['Dados', 'Picos'])
    plt.show()
    
    return

identificar_picos()