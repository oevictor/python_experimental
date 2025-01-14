from pymatgen.core import Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import matplotlib.pyplot as plt
import numpy as np

from texttable import Texttable


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

    # d_biblioteca = xrd_pattern.d_hkls
    # print(f'valores de d segundo a biblioteca pymatgen {d_biblioteca}')

    # identificar os planos cristalinos
    
    
    table = Texttable()
    table.set_cols_align(["c", "c", "c", "c", "c", "f", "f"])
    table.set_cols_dtype(["i", "f", "f", "f", "i", "f", "f"])  # Tipos de coluna
    table.add_row(["Pico", "2Theta", "Intensidade", "d", "Ordem de Reflexão", "a", "hkl²"])

    d_1 = []
    hkl_squared=[]
    hkl_squared.append(3)# sei que a primeira refelxão é 111 e usei ela para calcular o valor de a
    # Cálculo inicial e preenchimento da tabela
    # for i in range(len(intensidade)):
    for i in range(0,5):
        for n in range(1, 2): #como a ordem das reflexoes não me interessa, vou considerar apenas a primeira ordem
            d_valor = 1.54056 * n / (2 * np.sin(np.radians(dois_theta[i] / 2)))
            if n == 1:
                d_1.append(d_valor)
            
            # Cálculo de 'a' usando o primeiro valor de d_1
            if i == 0:
                hkl = 1  # Exemplo: hkl = 1 para o primeiro pico
                a = d_valor * np.sqrt(hkl**2 + hkl**2 + hkl**2)
                
            else:
                a = d_1[0] * np.sqrt(1**2 + 1**2 + 1**2)
                # hkl=(a/d_valor)**2
            # Cálculo de hkl²
            
            
            hkl_squared_value=int((a / d_valor) ** 2)
            hkl_squared.append (hkl_squared_value)
            
            # print(f'hkl_sq = {hkl_squared}')
                        
            # Testar as condições possíveis para haver um pico indexado corretamente
            hkl_indices = []
            for j in range(0, 4):
                for z in range(0, 4):
                    for v in range(0, 4):
                        if (j**2 + z**2 + v**2) == hkl_squared_value or (j**2 + z**2 + v**2) == 3:
                            hkl_indices.append(f'{j}{z}{v}')
            
            hkl_str = ', '.join(hkl_indices)
            
            print(hkl_str)
            
            
            
            
            
            # Adiciona os valores à tabela
            table.add_row([i + 1, dois_theta[i], intensidade[i], d_valor, n, a, hkl_squared[i]])
                      #testando as condições possiveis para haver um pico indexado corretamente TABELA DE CRISTALOGRAFIA VOLUME A
            h=[]
            k=[]
            l=[]
            for i in range(0,4):
                h.append(i)
                k.append(i)
                l.append(i)
                for j in h:
                    for z in k:
                        for v in l:
                            if (j**2 + z**2 + v**2) == hkl_squared:
                                print(f'hkl = {j}{z}{v} que correspodem ao hkl^2 {hkl_squared}')
    # Imprime a tabela
    print(table.draw())




   

    # Plotar o difratograma
    plt.figure(figsize=(8, 6))
    plt.scatter(dois_theta, intensidade, label="Difratograma Simulado", color="blue")
    plt.xlabel("2θ (graus)")
    plt.ylabel("Intensidade (u.a.)")
    plt.title("Difratograma de Raios X Simulado")
    plt.legend()
    plt.grid(True)
    # plt.show()

# Chamar a função
identificar_picos()
