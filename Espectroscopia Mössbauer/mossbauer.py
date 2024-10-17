import matplotlib.pyplot as plt
import pandas as pd
import mplcursors
from scipy.signal import find_peaks
import numpy as np
#tratamento_Isomerico de dados
def tratamento_Isomerico(file_name,cor,relacoao_ao_alfa=True):
    #dados a serem tratados
    dados=pd.read_csv(file_name, sep='\t',usecols=[0,2] ,names=["Velocidade da fonte (mm/s)","Contagem de fontos"])
    x = dados["Velocidade da fonte (mm/s)"]
    y = dados["Contagem de fontos"]
    legenda_graficos= file_name.split('\\')[-1].replace('.txt','')
    #plot do grafico
    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    if relacoao_ao_alfa==True:
        plt.axvline(x=0.84, color='black', linestyle='-')#plotando uma linha vertical em Fe_x=0 para ver justamente o desvio a Fe_alfa cujo desvio isometrico é 0
    grafico=plt.scatter(x,y, label=legenda_graficos,s=2, color=cor)
    cursor = mplcursors.cursor(grafico)
    plt.xlabel('Velocidade da fonte (mm/s)')
    plt.ylabel('Contagem de fontos')
    plt.title(f'Desvio Isomérico {legenda_graficos}')
    plt.legend()
    plt.savefig("Espectroscopia Mössbauer\graficos\\"+legenda_graficos+'.png')
    plt.show()
 
#Esse esta calculando o desvio isometrico em relação ao ferro-alfa 
tratamento_Isomerico('Espectroscopia Mössbauer\Dados\Mossbauer_data\Fe-alpha.txt',"red", True)        
tratamento_Isomerico(r'Espectroscopia Mössbauer\Dados\Mossbauer_data\aco_inox.txt',"gray",True)
tratamento_Isomerico('Espectroscopia Mössbauer\Dados\Mossbauer_data\FeSO4.txt',"blue",True)
tratamento_Isomerico('Espectroscopia Mössbauer\Dados\Mossbauer_data\Hematita.txt',"green",True)

#intereção quadrupolar
def interacao_quadruplar(file_name, cor, altura):
    # Ler dados do arquivo
    dados = pd.read_csv(file_name, sep='\t', usecols=[0, 2], names=["Velocidade da fonte (mm/s)", "Contagem de fontos"])
    x = dados["Velocidade da fonte (mm/s)"]
    y = dados["Contagem de fontos"]
    
    # Definir legenda a partir do nome do arquivo
    legenda_graficos = file_name.split('\\')[-1].replace('.txt', '')
    
    # Plot do gráfico
    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    
    # Linha de referência em x=0
    plt.axvline(x=0, color='black', linestyle='-')
    
    # Definir limites de x para encontrar os picos
    x_min = -1
    x_max = 3
    mask = (x > x_min) & (x < x_max)  # Apenas valores no intervalo -1 < x < 1
    
    # Filtrar os dados para o intervalo desejado
    x_lim = x[mask]
    y_lim = y[mask]
    
    # Inverter os valores de y para detecção de picos negativos
    y_invertido = -y_lim
    
    # Encontrar picos no intervalo filtrado
    picos, _ = find_peaks(y_invertido, height=altura)
    
    # Plotar os dados e os picos encontrados
    grafico=plt.scatter(x, y, label=legenda_graficos, s=2, color=cor)
    plt.plot(x_lim.iloc[picos], y_lim.iloc[picos], "ro")  # Usar índices relativos ao intervalo filtrado
    posições_picos=x_lim.iloc[picos].values
    
    diferenca=x_lim.iloc[picos].diff()
    # Configurar cursor interativo
    plt.scatter(x_lim.iloc[picos], y_lim.iloc[picos],label=posições_picos, s=2)
    mplcursors.cursor(grafico)
    
    # Configurações do gráfico
    plt.xlabel('Velocidade da fonte (mm/s)')
    plt.ylabel('Contagem de fontos')
    plt.title(f'Interação Quadrupolar {legenda_graficos}')
    plt.legend()
    
    # Salvar e mostrar o gráfico
    plt.savefig("Espectroscopia Mössbauer/graficos_Quadrupolar/" + legenda_graficos + '.png')
    plt.show()
# interacao_quadruplar('Espectroscopia Mössbauer\Dados\Mossbauer_data\Fe-alpha.txt')
# interacao_quadruplar(r'Espectroscopia Mössbauer\Dados\Mossbauer_data\aco_inox.txt')
interacao_quadruplar('Espectroscopia Mössbauer\Dados\Mossbauer_data\FeSO4.txt',cor="blue",altura=-5e5)
interacao_quadruplar('Espectroscopia Mössbauer\Dados\Mossbauer_data\Hematita.txt',cor="green",altura=-1.4e5)

def interacoes_heperfinas(file_name,cor,altura):
    # Ler dados do arquivo
    dados = pd.read_csv(file_name, sep='\t', usecols=[0, 2], names=["Velocidade da fonte (mm/s)", "Contagem de fontos"])
    x = dados["Velocidade da fonte (mm/s)"]
    y = dados["Contagem de fontos"]
    
    # Definir legenda a partir do nome do arquivo
    legenda_graficos = file_name.split('\\')[-1].replace('.txt', '')
    
    # Plot do gráfico
    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    
    # Linha de referência em x=0
    # plt.axvline(x=0, color='black', linestyle='-')
    
    # Definir limites de x para encontrar os picos
    x_min = -9
    x_max = 9
    mask = (x > x_min) & (x < x_max)  # Apenas valores no intervalo -1 < x < 1
    
    # Filtrar os dados para o intervalo desejado
    x_lim = x[mask]
    y_lim = y[mask]
    
    # Inverter os valores de y para detecção de picos negativos
    y_invertido = -y_lim
    
    # Encontrar picos no intervalo filtrado
    picos, _ = find_peaks(y_invertido, height=altura)
    
    # Plotar os dados e os picos encontrados
    grafico=plt.scatter(x, y, label=legenda_graficos, s=2, color=cor)
    plt.plot(x_lim.iloc[picos], y_lim.iloc[picos], "ro")  # Usar índices relativos ao intervalo filtrado
    posições_picos=x_lim.iloc[picos].values
    
    # Configurar cursor interativo
    plt.scatter(x_lim.iloc[picos], y_lim.iloc[picos],label=posições_picos, s=2)
    mplcursors.cursor(grafico)
    
    # Configurações do gráfico
    plt.xlabel('Velocidade da fonte (mm/s)')
    plt.ylabel('Contagem de fontos')
    plt.title(f'Interação Hiperfina {legenda_graficos}')
    plt.legend()
    plt.savefig("Espectroscopia Mössbauer/grafico_hiperfino/" + legenda_graficos + '.png')

    plt.show()
    
interacoes_heperfinas('Espectroscopia Mössbauer\Dados\Mossbauer_data\Fe-alpha.txt',"red",altura=-1.4e7)
interacoes_heperfinas(r'Espectroscopia Mössbauer\Dados\Mossbauer_data\aco_inox.txt',"gray",altura=-1.4e4)
interacoes_heperfinas('Espectroscopia Mössbauer\Dados\Mossbauer_data\FeSO4.txt',"blue",altura=-5e5)
interacoes_heperfinas('Espectroscopia Mössbauer\Dados\Mossbauer_data\Hematita.txt',"green",altura=-1.4e5)
    
    