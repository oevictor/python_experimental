from pymatgen.core import Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import matplotlib.pyplot as plt
import numpy as np
from texttable import Texttable
import math

def identificar_picos():
    """
    Identifica picos em um padrão de difração de raios X e exibe os resultados
    em uma tabela, incluindo as diferentes regras de seleção (1–5), além de
    imprimir todas as combinações hkl possíveis ao final.
    """

    # ----------------------------------------------------------
    # 1) Carregar a estrutura a partir do arquivo CIF
    # ----------------------------------------------------------
    estrutura = Structure.from_file("microscopia_eletronica\\CIF_Ag_9008459.cif")

    # ----------------------------------------------------------
    # 2) Criar um simulador de difração de raios-X e gerar o padrão
    # ----------------------------------------------------------
    xrd_calculator = XRDCalculator()
    xrd_pattern = xrd_calculator.get_pattern(estrutura)

    # Extraindo dados de 2θ (graus) e intensidade
    dois_theta = xrd_pattern.x
    intensidade = xrd_pattern.y

    # ----------------------------------------------------------
    # 3) Criar tabela para exibição e configurar larguras de colunas
    # ----------------------------------------------------------
    table = Texttable()

    # Opcional: Definir alinhamento das colunas
    table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c"])
    # Definir tipo de dado de cada coluna (ex.: 'f' = float, 'i' = int, 't' = texto)
    table.set_cols_dtype(["i", "f", "f", "f", "i", "f", "f", "t", "t"])
    # Aumentar a largura de cada coluna (em caracteres)
    table.set_cols_width([6, 10, 12, 10, 12, 10, 10, 10, 30])

    # Cabeçalho da tabela
    table.add_row([
        "Pico", 
        "2Theta", 
        "Intensidade", 
        "d", 
        "Ordem Ref", 
        "a", 
        "hkl²", 
        "hkl", 
        "Regras"
    ])

    # ----------------------------------------------------------
    # 4) Iniciar listas para cálculos e armazenar hkl²
    # ----------------------------------------------------------
    d_1 = []            # Lista dos espaçamentos d calculados
    hkl_squared = []    # Lista dos valores calculados de hkl²
    # hkl_squared.append(3)  # Exemplo: o primeiro valor é 3 (corresponde a (111) no FCC)

    # Vamos definir a ordem de reflexão como 1 para este exemplo
    n = 1

    # ----------------------------------------------------------
    # 5) Calcular d, a e hkl² para cada pico
    # ----------------------------------------------------------
    for i in range(min(len(dois_theta), len(intensidade))):
        # 1.54056 é o comprimento de onda em Angstrom do Cu-Kα (aproximadamente)
        d_valor = 1.54056 * n / (2 * np.sin(np.radians(dois_theta[i] / 2)))
        d_1.append(d_valor)

        # # Cálculo de 'a' usando o primeiro valor de d_1 para normalizar (no 1º pico)
        # if i == 0:
        #     hkl = 1  # Exemplo: (1,1,1) => hkl=1 se quisermos usar para escalonar
        #     a = d_valor * np.sqrt(hkl**2 + hkl**2 + hkl**2)
        # else:
            # Em picos subsequentes, usamos d_1[0] e a suposição do primeiro pico
        a = d_1[0] * np.sqrt(1**2 + 1**2 + 1**2)

        # Calcular valor de hkl² de acordo com 'a' e o d_valor do i-ésimo pico
        # hkl_sq = int((a / d_valor) ** 2)
        hkl_sq = math.ceil(a**2 / d_1[i]**2)
        print('começa aqui ')
        print(a**2 / d_valor**2)
        print(f'aqui estão os valore de hkl_sq = {hkl_sq}')
        print(f'os valores de a = {a} e d = {d_valor}')
        hkl_squared.append(hkl_sq)
        
        print(f'os valores de hkl_sq = {hkl_squared}')

    # ----------------------------------------------------------
    # 6) Função para aplicar as regras de seleção e armazenar resultados
    # ----------------------------------------------------------
    def regra_hkl(hkl_squared_values):
        """
        Percorre cada valor em hkl_squared_values e verifica todos os (h,k,l)
        cuja soma de quadrados é igual a hkl_sq. Aplica também as Regras 1-4
        e a Regra 5:
        
        - Regra 5: h^2 + k^2 + l^2 = hkl_squared  (se encontrar, já satisfaz)
        - Regra 1: (h + k), (h + l), (k + l) = 2n
        - Regra 2: 0kl, onde k e l = 2n
        - Regra 3: hhl, onde h + l = 2n
        - Regra 4: h00, onde h = 2n

        Retorna duas listas de mesmo tamanho:
           hkl_indices_list (lista de strings "hkl")
           regras_list (lista de strings descrevendo as regras satisfeitas)
        na **ordem** de busca.
        """

        hkl_indices_list = []  # lista final de hkl para cada valor de hkl²
        regras_list = []       # lista final de string com as regras satisfeitas

        # (Opcional) Dicionário para armazenar *todas* as possibilidades
        # associadas a um mesmo valor de hkl².
        # Formato: resultados_por_hkl2[hkl_sq] = [ { "hkl": "xyz", "regras": "Regra 5 | ..." }, ... ]
        resultados_por_hkl2 = {}

        for hkl_sq in hkl_squared_values:
            encontrou_algum = False

            # Inicializa lista de resultados para esse hkl²
            resultados_por_hkl2[hkl_sq] = []

            # Percorrer h, k, l em um intervalo maior ou menor dependendo do material
            for j in range(5,-1,-1):
                for z in range(5,-1,-1):
                    for v in range(5,-1,-1):
                        if j**2 + z**2 + v**2 == hkl_sq:
                            # Montar uma lista de regras cumpridas
                            regras_que_cumpriu = []

                            # Regra 5: h^2 + k^2 + l^2 = hkl_squared
                            # Se estamos aqui, já satisfaz a Regra 5
                            regras_que_cumpriu.append("Regra 5: h^2+k^2+l^2 = hkl_squared")

                            # Regra 1: h+k, h+l, k+l = 2n
                            if ((j + z) % 2 == 0 and
                                (j + v) % 2 == 0 and
                                (z + v) % 2 == 0):
                                regras_que_cumpriu.append("Regra 1: (h+k),(h+l),(k+l)=2n")

                            # Regra 2: 0kl, onde k e l = 2n
                            if j == 0 and (z % 2 == 0) and (v % 2 == 0):
                                regras_que_cumpriu.append("Regra 2: 0kl (k,l=2n)")

                            # Regra 3: hhl, onde h+l = 2n
                            if z == j and (j + v) % 2 == 0:
                                regras_que_cumpriu.append("Regra 3: hhl (h+l=2n)")

                            # Regra 4: h00, onde h=2n
                            if z == 0 and v == 0 and (j % 2 == 0):
                                regras_que_cumpriu.append("Regra 4: h00 (h=2n)")

                            # Cria uma única string com as regras que foram cumpridas
                            regras_str = " | ".join(regras_que_cumpriu)

                            # Armazena para imprimir no final: 
                            # cada hkl encontrado e suas regras
                            resultados_por_hkl2[hkl_sq].append({
                                "hkl": f"{j}{z}{v}",
                                "regras": regras_str
                            })

                            # Se ainda não adicionamos nada para este valor de hkl² 
                            # em hkl_indices_list, vamos adicionar o *primeiro* que aparecer.
                            if not encontrou_algum:
                                hkl_indices_list.append(f"{j}{z}{v}")
                                regras_list.append(regras_str)
                                encontrou_algum = True

            # Se não encontrou nenhum (h,k,l) que satisfizesse, colocar "N/A"
            if not encontrou_algum:
                hkl_indices_list.append("N/A")
                regras_list.append("Sem regra identificada")

        # ------------------------------------------------------
        # 7) Exibir TODAS as respostas possíveis ao final
        #    Aqui retornamos as duas listas (1-para-1 com picos)
        #    e também esse dicionário com *todas* as combinações.
        # ------------------------------------------------------
        print(f'hkl_indices_list: {hkl_indices_list}')
        return hkl_indices_list, regras_list, resultados_por_hkl2
    
    # ----------------------------------------------------------
    # 8) Chamar a função de regras e obter listas e resultados
    # ----------------------------------------------------------
    hkl_indices_validos_list, regras_correspondentes_list, resultados_todos = regra_hkl(hkl_squared)

    # ----------------------------------------------------------
    # 9) Preencher a tabela, linha por linha
    # ----------------------------------------------------------
    for i in range(len(d_1)):
        # Se i ultrapassar o tamanho de hkl_indices_validos_list, usamos "N/A"
        if i < len(hkl_indices_validos_list):
            hkl_valor = hkl_indices_validos_list[i]
            regras_valor = regras_correspondentes_list[i]
        else:
            hkl_valor = "N/A"
            regras_valor = "N/A"

        table.add_row([
            i + 1,           # Número do pico
            dois_theta[i],   # Valor de 2θ
            intensidade[i],  # Intensidade
            d_1[i],          # Espaçamento d
            n,               # Ordem de reflexão (1 neste exemplo)
            a,               # Constante de rede estimada
            hkl_squared[i],  # Valor inteiro de hkl² calculado
            hkl_valor,       # Índices (hkl) encontrados
            regras_valor     # As regras satisfeitas
        ])

    # ----------------------------------------------------------
    # 10) Exibir a tabela
    # ----------------------------------------------------------
    print(table.draw())

    # ----------------------------------------------------------
    # 11) Mostrar (hkl, regra) na mesma ordem que foi adicionada
    #     (ou seja, a cada pico da lista principal)
    # ----------------------------------------------------------
    print("\n***** hkl e regras para cada pico (na ordem principal) *****")
    for hkl_item, regra_item in zip(hkl_indices_validos_list, regras_correspondentes_list):
        print(f"hkl = {hkl_item} | {regra_item}")

    # ----------------------------------------------------------
    # 12) Exibir TODAS as combinações possíveis para cada valor
    #     de hkl² (armazenadas em resultados_todos)
    # ----------------------------------------------------------
    print("\n***** Todas as respostas possíveis por valor de hkl² *****")
    for hkl_sq_val, lista_resultados in resultados_todos.items():
        print(f"\nPara hkl² = {hkl_sq_val}:")
        if not lista_resultados:
            print("  Nenhuma combinação encontrada.")
        else:
            for combo in lista_resultados:
                hkl_combo = combo["hkl"]
                regras_combo = combo["regras"]
                print(f"  hkl = {hkl_combo}, Regras: {regras_combo}")

    # ----------------------------------------------------------
    # 13) Anotar  índices no gráfico, se existirem
    # ----------------------------------------------------------
    if len(hkl_indices_validos_list) > 1:
        texto = [hkl_indices_validos_list[0], hkl_indices_validos_list[1],hkl_indices_validos_list[2],hkl_indices_validos_list[3],hkl_indices_validos_list[4]]
    else:
        texto = []

    # ----------------------------------------------------------
    # 14) Plotar o difratograma (2θ vs intensidade)
    # ----------------------------------------------------------
    plt.figure(figsize=(8, 6))
    plt.scatter(dois_theta, intensidade, label="Picos simulados", color="blue")
    plt.xlabel("2θ (graus)")
    plt.ylabel("Intensidade (u.a.)")

    # Adiciona anotações apenas nos 2 primeiros picos, se existirem
    for i, txt in enumerate(texto):
        if i < len(dois_theta):
            plt.annotate(txt, (dois_theta[i], intensidade[i]), fontsize=8, color='red')

    plt.title("Difratograma de Raios X - Ag")
    plt.legend()
    plt.grid(True)
    plt.show()

# ----------------------------------------------------------
# 15) Chamando a função principal
# ----------------------------------------------------------
if __name__ == "__main__":
    identificar_picos()
