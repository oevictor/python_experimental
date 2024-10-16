import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mplcursors

#tratamento de dados
def tratamento(file_name,cor):
    #dados a serem tratados
    dados=pd.read_csv(file_name, sep='\t',usecols=[0,2] ,names=["Velocidade da fonte (mm/s)","Contagem de fontos"])
    x = dados["Velocidade da fonte (mm/s)"]
    y = dados["Contagem de fontos"]
    #dados de calibração são os dados do ferro-alfa
    dados_fe_alfa = pd.read_csv('Espectroscopia Mössbauer\Dados\Mossbauer_data\Fe-alpha.txt', sep='\t',usecols=[0,2] ,names=["Velocidade da fonte (mm/s)","Contagem de fontos"])
    x_fe_alfa = dados_fe_alfa["Velocidade da fonte (mm/s)"]
    y_fe_alfa = dados_fe_alfa["Contagem de fontos"]
    normalizacao=y.max()/y_fe_alfa.max()
    y_fe_alfa=y_fe_alfa*normalizacao
    legenda_graficos= file_name.split('\\')[-1].replace('.txt','')
    #plot do grafico
    grafico_fe_alfa=plt.scatter(x_fe_alfa,y_fe_alfa,label='Fe_alfa',s=2, color='red')
    grafico=plt.scatter(x,y, label=legenda_graficos,s=2, color=cor)
    cursor_1= mplcursors.cursor(grafico_fe_alfa)
    cursor = mplcursors.cursor(grafico)
    plt.legend()
    plt.show()
        
tratamento(r'Espectroscopia Mössbauer\Dados\Mossbauer_data\aco_inox.txt',"black")
tratamento('Espectroscopia Mössbauer\Dados\Mossbauer_data\FeSO4.txt',"blue")
tratamento('Espectroscopia Mössbauer\Dados\Mossbauer_data\Hematita.txt',"green")

    
    