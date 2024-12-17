import pandas as pd 
import matplotlib.pyplot as plt
import mplcursors 
#Importing the dada

def dados(filepath):
    
    #dados carregados 
    dados=pd.read_csv(filepath, delimiter='\t', usecols=[0,1], names=["Numero de onda", 'Intensidade'])
    x=dados['Numero de onda']
    y=dados['Intensidade']
    
    #primeira parte consite de encotrar a variação da frequencia dos modos E' e A1
    
    
    
    
    
    
    titulo = filepath.split('\\')[-1].replace('.txt', '')
    
    
    plt.title(titulo)
    grafico=plt.plot(x,y)
    plt.ylabel("Intesidade")
    plt.xlabel("Número de onda $(cm^{-1})$")
    mplcursors.cursor(hover=True)
    mplcursors.cursor(grafico)
    mplcursors.cursor(grafico)
    plt.show()

dados("Ramma\Dados\RAMAN_Dados\MoS2.txt")
dados("Ramma\Dados\RAMAN_Dados\WS2.txt")
dados("Ramma\Dados\RAMAN_Dados\MoSe2-532nm-30s-10acc-obj100x-250mW.txt")
dados("Ramma\Dados\RAMAN_Dados\MoSeS-532nm-30s-10acc-obj100x-gr1800-45mi.txt")