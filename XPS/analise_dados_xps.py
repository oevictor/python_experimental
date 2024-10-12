import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Cursor
import mplcursors



# dados sem Sputtering
def grafico(file_name, text, posicao):
    # importando dados
    file_name_save = file_name.split('\\')[-1].replace('.txt', '')
    numero_da_amostra = ''.join(filter(str.isdigit, file_name))

    dados = pd.read_csv(file_name, delimiter='\t', usecols=[0, 2], names=["Energia Cinetica eV", "Sinal"])
    x = 1486.68 - dados["Energia Cinetica eV"]

    x_minimo = x.min()
    x_maximo = x.max()

    y = dados["Sinal"] * 10
    # grafico
    grafico=plt.plot(x, y, label=f'Amostra {numero_da_amostra}')
    plt.xlabel('Energia de ligação (eV)')
    plt.ylabel('Intensidade (a.u.)')
    plt.title('Espectro de fotoelétrons de valência Sem Sputtering')
    
    for i, texto in enumerate(text):
        if i<len(posicao):
            plt.annotate(
                texto,
                xy=(posicao[i][0], posicao[i][1]),
                xytext=(posicao[i][0] + 85, posicao[i][1] + 8e4),  # Ajuste a posição do texto para aumentar a seta

                arrowprops=dict(facecolor='black',
                                shrink=2,# Ajuste a quantidade de encolhimento da seta
                                width=1,  # Ajuste a largura da linha da seta
                                headwidth=4,  # Ajuste a largura da cabeça da seta
                                headlength=5 # Ajuste o comprimento da cabeça da seta
                                ),  # Ajuste as propriedades da seta
                fontsize=7
            )
    
    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    plt.xlim(x_maximo, x_minimo)
    plt.xticks(np.arange(0,x_maximo, 100))
    curso=Cursor(plt.gca(), useblit=True, color='red', linewidth=1)
    cursor = mplcursors.cursor(grafico)
    plt.legend()
    plt.savefig(f'grafico_amostra{file_name_save}.png')
    plt.show()

text_sem_sputtering = {
    "Am1": [r"$Ar2p_{1/2}$", r"C1s",r"O1s",r"F1s"],
    "Am2": [r"Li1s",r"$Cr2p_{3/2}$", r"C1s",r"$Fe2p_{3/2}$",r"O1s",r"$Ge2p_{3/2}$"],
    "Am3": [r"$Zn2p_{1/2}$", r"$Zn2p_{1/2}$",r"$Cu2p_{1/2}$",r"$Cu2p_{3/2}$",r"O1s",r"Sc2s",r"C1s",r"$Cl2p_{1/2}$",r"$As3p_{3/2}$",r"Cu3s",r"$Zn3p_{1/2}$"]
}
posicao_sem_sputtering = {
    "Am1": [[244, 9e4], [285, 2.54e5],[531,4.24e5],[685,1.3e5]],
    "Am2": [[55,1.08e5],[574, 2.39e5], [285, 3.36e5],[707, 4.43e5],[530.4,4.85e5],[1222,6.34e5]],
    "Am3": [[1045, 7e5],[1022,7.6e5],[953,6e5],[933,7e5],[533,3.89e5],[483,2.42e5],[286, 3.06e5],[200,1e5],[140,1.2e5],[122,1.05e6],[91,1.02e7]]
}

# dados com Sputtering
def grafico_Sputtering(file_name, text, posicao):
    # importando dados
    file_name_save = file_name.split('\\')[-1].replace('.txt', '')
    numero_da_amostra = ''.join(filter(str.isdigit, file_name))

    dados = pd.read_csv(file_name, delimiter='\t', usecols=[0, 2], names=["Energia Cinetica eV", "Sinal"])
    x = 1486.68 - dados["Energia Cinetica eV"]

    x_minimo = x.min()
    x_maximo = x.max()

    y = dados["Sinal"] * 10
    # grafico
    grafico=plt.plot(x, y, label=f'Amostra {numero_da_amostra}')
    plt.xlabel('Energia de ligação (eV)')
    plt.ylabel('Intensidade (a.u.)')
    plt.title('Espectro de fotoelétrons de valência com Sputtering')
    
    for i, texto in enumerate(text):
        if len(posicao)>i:
            plt.annotate(
                texto,
                xy=(posicao[i][0], posicao[i][1]),
                xytext=(posicao[i][0] + 25, posicao[i][1] + 8e4),  # Ajuste a posição do texto para aumentar a seta
                # plt.arrow(posicao[i][0], posicao[i][1], 50, 2e5, head_width=0.05, head_length=0.1, fc='k', ec='k'),
                arrowprops=dict(facecolor='black',
                                shrink=1,# Ajuste a quantidade de encolhimento da seta
                                width=1,  # Ajuste a largura da linha da seta
                                headwidth=4,  # Ajuste a largura da cabeça da seta
                                headlength=5 # Ajuste o comprimento da cabeça da seta
                                ),  # Ajuste as propriedades da seta
                fontsize=7
            )
    
    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    plt.xlim(x_maximo, x_minimo)
    plt.xticks(np.arange(0,x_maximo, 100))
    curso=Cursor(plt.gca(), useblit=True, color='red', linewidth=1)
    cursor = mplcursors.cursor(grafico)
    plt.legend()
    plt.savefig(f'grafico_amostra{file_name_save}.png')
    plt.show()
text = {
    "Am1": [r"$Fe2p_{3/2}$", r"O1s",r"Ar2s",r"$Ar2p_{3/2}$",r"Al2s",r"$Al2p_{3/2}$" ],
    "Am2": [r"Ni3s",r"Fe2s",r"$Fe2p_{1/2}$",r"$Fe2p_{3/2}$",r"$Cr2p_{1/2}$",r"O1s",r"C1s"],
    "Am3": [r"$Zn2s$",r"$Cu2s$",r"$Zn2p_{1/2}$",r"$Zn2p_{3/2}$",r"$Cu2p_{3/2}$",r'$Fe2p_{1/2}$']
}
posicao = {
    "Am1": [[707,8.82e4],[533,8.47e4],[320,1.198e5],[242,1.33e5],[117,3e5],[75,1.22e5]], 
    "Am2": [[853, 1.29e7],[846,1.215e6],[720,1.328e6],[708,1.489e7],[583,3.26e5],[532,1.10e5],[285,1.19e5]],
    "Am3": [[1195, 1.36e6],[1097,1.58e6],[1045,1.78e6],[1021,2.18e6],[933,1.24e6],[720,1.27e6]]
}

def grafico_scan(file_name,x_linha,text, posicao):

    #importando dados
    file_name_save = file_name.split('\\')[-1].replace('.txt', '')
    nome_da_amostra = file_name.split('\\')[-1].split('_')[-1].replace('.txt', '')
    dados = pd.read_csv(file_name, delimiter='\t', usecols=[0, 2], names=["Energia Cinetica eV", "Sinal"])
    x = 1486.68-dados["Energia Cinetica eV"]
    x_minimo = x.min()
    x_maximo = x.max()
    y= dados["Sinal"]*10
    #grafico
    grafico=plt.plot(x, y, label=f'Amostra {nome_da_amostra}')
    plt.xlabel('Energia de ligação (eV)')
    plt.ylabel('Intensidade (a.u.)')
    plt.title('Scan da amostra')
    for i, texto in enumerate(text):
        if len(posicao)>i:
            plt.annotate(
                texto,
                xy=(posicao[i][0], posicao[i][1] ),
                xytext=(posicao[i][0] , posicao[i][1] ),  # Ajuste a posição do texto para aumentar a seta
                # plt.arrow(posicao[i][0], posicao[i][1], 50, 2e5, head_width=0.05, head_length=0.1, fc='k', ec='k'),
                arrowprops=dict(facecolor='black',
                                shrink=1,# Ajuste a quantidade de encolhimento da seta
                                width=1,  # Ajuste a largura da linha da seta
                                headwidth=4,  # Ajuste a largura da cabeça da seta
                                headlength=5 # Ajuste o comprimento da cabeça da seta
                                ),  # Ajuste as propriedades da seta
                fontsize=7
            )
    
    #linas
    for linha in x_linha:
        plt.axvline(x=linha, color='r', linestyle='--')

    plt.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    plt.xlim(x_maximo, x_minimo)
    
    curso=Cursor(plt.gca(), useblit=True, color='red', linewidth=1)
    cursor = mplcursors.cursor(grafico)
    plt.legend()
    plt.savefig(f'grafico_amostra{file_name_save}.png')
    plt.show()

for amostra in ["Am1", "Am2", "Am3"]:
    grafico(f'XPS\\dados\\{amostra}_survey.txt',text_sem_sputtering[amostra], posicao_sem_sputtering[amostra])
    grafico_Sputtering(f'XPS\\dados\\{amostra}_surv_sput.txt',text[amostra], posicao[amostra])


# Valores para os gráficos sput
x_linha_cr = [583.43, 574]
texto_cr = [r"$Cr2p_{3/2}$", r"$Cr2p_{3/2}$"]
posicao_cr = [[583, 1.15e5], [574, 1.79e5]]

x_linha_fe = [719.95, 706.75]
texto_fe = [r"$Fe2p_{1/2}$", r"$Fe2p_{3/2}$"]
posicao_fe = [[719.95, 4.42e5], [706.75, 7.41e5]]

grafico_scan('XPS\\dados\\Am2_Cr2p.txt', x_linha_cr, texto_cr, posicao_cr)
grafico_scan('XPS\\dados\\Am2_Fe2p.txt', x_linha_fe, texto_fe, posicao_fe)


def grafico_ao_lado(grafico,grafico_Sputtering,file_name):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(grafico)
    axs[1].imshow(grafico_Sputtering)
    plt.savefig(f'grafico_amostra_juntas{file_name}.png')
    plt.show()
    
for amostra in ["Am1", "Am2", "Am3"]:
    grafico_ao_lado(plt.imread(f'grafico_amostra{amostra}_survey.png'), plt.imread(f'grafico_amostra{amostra}_surv_sput.png'),f"{amostra}")



