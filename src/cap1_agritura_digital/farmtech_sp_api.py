import csv
from datetime import datetime

import requests

# ============================================================
# FarmTech Solutions - Gestao de Plantio (Milho e Soja)
# Integrado com API meteorologica publica para Sao Paulo
# ============================================================

# Coordenadas fixas de Sao Paulo (capital)
CIDADE_FIXA = "Sao Paulo"
LATITUDE_SP = -23.5505
LONGITUDE_SP = -46.6333

# Vetores principais do projeto
culturas = []
comprimentos = []
larguras = []
areas_m2 = []
areas_ha = []
espacamentos_linha = []
espacamentos_planta = []
ruas = []
plantas = []
doses_insumo = []
insumos_totais = []

# Vetores meteorologicos
cidades = []
temperaturas = []
umidades = []
ventos = []
probabilidades_chuva = []
datas_consulta_clima = []
alertas_climaticos = []


# ============================================================
# Funcoes auxiliares de entrada e validacao
# ============================================================

def ler_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Entrada invalida. Por favor, digite um numero.")



def ler_float_intervalo(msg, minimo, maximo):
    while True:
        valor = ler_float(msg)
        if minimo <= valor <= maximo:
            return valor
        print(f"Valor fora do intervalo permitido ({minimo} - {maximo}). Tente novamente.")



def ler_float_positivo(msg):
    while True:
        valor = ler_float(msg)
        if valor > 0:
            return valor
        print("O valor deve ser maior que zero. Tente novamente.")



def validar_cultura():
    while True:
        cultura = input("Cultura (milho/soja): ").strip().lower()
        if cultura in ["milho", "soja"]:
            return cultura
        print("Cultura invalida. Digite 'milho' ou 'soja'.")



def validar_indice(tamanho):
    if tamanho == 0:
        print("Nao ha registros cadastrados.")
        return -1
    while True:
        try:
            pos = int(input(f"Digite o indice do registro (0 a {tamanho - 1}): "))
            if 0 <= pos < tamanho:
                return pos
            print(f"Indice invalido. Deve estar entre 0 e {tamanho - 1}.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


# ============================================================
# Funcoes de calculo
# ============================================================

def calcular_ruas(largura, espac_linha_cm):
    espac_linha_m = espac_linha_cm / 100.0
    if espac_linha_m > 0:
        return int(largura / espac_linha_m)
    return 0



def calcular_plantas(largura, comprimento, espac_linha_cm, espac_planta_cm):
    qtd_ruas = calcular_ruas(largura, espac_linha_cm)
    espac_planta_m = espac_planta_cm / 100.0
    if espac_planta_m > 0:
        plantas_por_rua = int(comprimento / espac_planta_m)
        return qtd_ruas * plantas_por_rua
    return 0



def calcular_insumo_total(area_m2, dose_kg_ha):
    area_ha = area_m2 / 10000.0
    return round(area_ha * dose_kg_ha, 2)


# ============================================================
# API meteorologica publica (Open-Meteo)
# ============================================================

def buscar_clima_sao_paulo():
    """Busca dados climaticos publicos de Sao Paulo."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE_SP,
        "longitude": LONGITUDE_SP,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "precipitation_probability",
        "forecast_days": 1,
        "timezone": "America/Sao_Paulo"
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        clima_atual = dados.get("current", {})
        hourly = dados.get("hourly", {})

        prob_chuva = None
        if hourly.get("precipitation_probability"):
            prob_chuva = hourly["precipitation_probability"][0]

        return {
            "cidade": CIDADE_FIXA,
            "temperatura": clima_atual.get("temperature_2m"),
            "umidade": clima_atual.get("relative_humidity_2m"),
            "vento": clima_atual.get("wind_speed_10m"),
            "probabilidade_chuva": prob_chuva,
            "data_consulta": clima_atual.get("time", datetime.now().strftime("%Y-%m-%dT%H:%M")),
            "fonte": "Open-Meteo"
        }
    except requests.RequestException as erro:
        print(f"Aviso: nao foi possivel consultar a API meteorologica. Detalhe: {erro}")
        return {
            "cidade": CIDADE_FIXA,
            "temperatura": None,
            "umidade": None,
            "vento": None,
            "probabilidade_chuva": None,
            "data_consulta": datetime.now().strftime("%Y-%m-%dT%H:%M"),
            "fonte": "Open-Meteo"
        }



def gerar_alerta_climatico(clima):
    alertas = []

    if clima["probabilidade_chuva"] is not None and clima["probabilidade_chuva"] > 70:
        alertas.append("Alta chance de chuva: considere adiar a aplicacao de insumos.")

    if clima["vento"] is not None and clima["vento"] > 20:
        alertas.append("Vento forte: cuidado com pulverizacao.")

    if clima["temperatura"] is not None and clima["temperatura"] > 32:
        alertas.append("Temperatura elevada: monitorar irrigacao e estresse hidrico.")

    if not alertas:
        return "Sem alertas climaticos no momento."
    return " | ".join(alertas)



def mostrar_clima_atual():
    print("\n--- Clima Atual de Sao Paulo ---")
    clima = buscar_clima_sao_paulo()
    print(f"Cidade..............: {clima['cidade']}")
    print(f"Consulta em.........: {clima['data_consulta']}")
    print(f"Temperatura.........: {clima['temperatura']} °C")
    print(f"Umidade.............: {clima['umidade']} %")
    print(f"Vento...............: {clima['vento']} km/h")
    print(f"Prob. de chuva......: {clima['probabilidade_chuva']} %")
    print(f"Alerta..............: {gerar_alerta_climatico(clima)}")


# ============================================================
# Funcoes de entrada de espacamento por cultura
# ============================================================

def obter_espacamentos(cultura):
    if cultura == "milho":
        espac_linha = ler_float_intervalo("Espacamento entre linhas (70 a 90 cm): ", 70, 90)
        espac_planta = ler_float_intervalo("Espacamento entre plantas (20 a 30 cm): ", 20, 30)
    else:
        espac_linha = ler_float_intervalo("Espacamento entre linhas (45 a 50 cm): ", 45, 50)
        espac_planta = 5.0

    return espac_linha, espac_planta


# ============================================================
# Funcoes do menu (CRUD)
# ============================================================

def inserir_dados():
    print("\n--- Cadastro de Terreno ---")

    cultura = validar_cultura()
    comprimento = ler_float_positivo("Comprimento do terreno (m): ")
    largura = ler_float_positivo("Largura do terreno (m): ")
    espac_linha, espac_planta = obter_espacamentos(cultura)
    dose = ler_float_intervalo("Dose de insumo (300 a 400 kg/ha): ", 300, 400)

    area = comprimento * largura
    area_ha = round(area / 10000.0, 4)
    qtd_ruas = calcular_ruas(largura, espac_linha)
    qtd_plantas = calcular_plantas(largura, comprimento, espac_linha, espac_planta)
    insumo_total = calcular_insumo_total(area, dose)

    clima = buscar_clima_sao_paulo()
    alerta = gerar_alerta_climatico(clima)

    culturas.append(cultura)
    comprimentos.append(comprimento)
    larguras.append(largura)
    areas_m2.append(area)
    areas_ha.append(area_ha)
    espacamentos_linha.append(espac_linha)
    espacamentos_planta.append(espac_planta)
    ruas.append(qtd_ruas)
    plantas.append(qtd_plantas)
    doses_insumo.append(dose)
    insumos_totais.append(insumo_total)

    cidades.append(clima["cidade"])
    temperaturas.append(clima["temperatura"])
    umidades.append(clima["umidade"])
    ventos.append(clima["vento"])
    probabilidades_chuva.append(clima["probabilidade_chuva"])
    datas_consulta_clima.append(clima["data_consulta"])
    alertas_climaticos.append(alerta)

    print(f"Registro cadastrado com sucesso! (Indice: {len(culturas) - 1})")
    print(f"Clima consultado em Sao Paulo: {clima['temperatura']} °C | Chuva: {clima['probabilidade_chuva']} %")
    print(f"Alerta: {alerta}")



def mostrar_dados():
    print("\n--- Lavouras Cadastradas ---")
    if len(culturas) == 0:
        print("Nenhum dado cadastrado.")
        return

    for i in range(len(culturas)):
        print(f"\n[Registro {i}]")
        print(f"  Cultura............: {culturas[i].capitalize()}")
        print(f"  Dimensoes..........: {larguras[i]}m x {comprimentos[i]}m")
        print(f"  Area...............: {areas_ha[i]} ha ({areas_m2[i]} m2)")
        print(f"  Espacamentos.......: Linhas: {espacamentos_linha[i]}cm | Plantas: {espacamentos_planta[i]}cm")
        print(f"  Estimativas........: {ruas[i]} ruas | {plantas[i]} plantas")
        print(f"  Insumos............: Dose: {doses_insumo[i]} kg/ha | Total: {insumos_totais[i]} kg")
        print(f"  Cidade.............: {cidades[i]}")
        print(f"  Consulta clima.....: {datas_consulta_clima[i]}")
        print(f"  Temperatura........: {temperaturas[i]} °C")
        print(f"  Umidade............: {umidades[i]} %")
        print(f"  Vento..............: {ventos[i]} km/h")
        print(f"  Prob. chuva........: {probabilidades_chuva[i]} %")
        print(f"  Alerta.............: {alertas_climaticos[i]}")



def atualizar_dados():
    print("\n--- Atualizar Registro ---")
    pos = validar_indice(len(culturas))
    if pos == -1:
        return

    print(f"Atualizando registro [{pos}] - {culturas[pos].capitalize()}")
    print("Preencha os novos valores:\n")

    cultura = validar_cultura()
    comprimento = ler_float_positivo("Novo comprimento (m): ")
    largura = ler_float_positivo("Nova largura (m): ")
    espac_linha, espac_planta = obter_espacamentos(cultura)
    dose = ler_float_intervalo("Nova dose de insumo (300 a 400 kg/ha): ", 300, 400)

    area = comprimento * largura
    area_ha = round(area / 10000.0, 4)
    qtd_ruas = calcular_ruas(largura, espac_linha)
    qtd_plantas = calcular_plantas(largura, comprimento, espac_linha, espac_planta)
    insumo_total = calcular_insumo_total(area, dose)

    clima = buscar_clima_sao_paulo()
    alerta = gerar_alerta_climatico(clima)

    culturas[pos] = cultura
    comprimentos[pos] = comprimento
    larguras[pos] = largura
    areas_m2[pos] = area
    areas_ha[pos] = area_ha
    espacamentos_linha[pos] = espac_linha
    espacamentos_planta[pos] = espac_planta
    ruas[pos] = qtd_ruas
    plantas[pos] = qtd_plantas
    doses_insumo[pos] = dose
    insumos_totais[pos] = insumo_total

    cidades[pos] = clima["cidade"]
    temperaturas[pos] = clima["temperatura"]
    umidades[pos] = clima["umidade"]
    ventos[pos] = clima["vento"]
    probabilidades_chuva[pos] = clima["probabilidade_chuva"]
    datas_consulta_clima[pos] = clima["data_consulta"]
    alertas_climaticos[pos] = alerta

    print(f"Registro [{pos}] atualizado com sucesso!")
    print(f"Novo alerta climatico: {alerta}")



def deletar_dados():
    print("\n--- Deletar Registro ---")
    pos = validar_indice(len(culturas))
    if pos == -1:
        return

    cultura_removida = culturas[pos]

    culturas.pop(pos)
    comprimentos.pop(pos)
    larguras.pop(pos)
    areas_m2.pop(pos)
    areas_ha.pop(pos)
    espacamentos_linha.pop(pos)
    espacamentos_planta.pop(pos)
    ruas.pop(pos)
    plantas.pop(pos)
    doses_insumo.pop(pos)
    insumos_totais.pop(pos)

    cidades.pop(pos)
    temperaturas.pop(pos)
    umidades.pop(pos)
    ventos.pop(pos)
    probabilidades_chuva.pop(pos)
    datas_consulta_clima.pop(pos)
    alertas_climaticos.pop(pos)

    print(f"Registro de '{cultura_removida.capitalize()}' (posicao {pos}) deletado com sucesso!")



def exportar_csv():
    if len(culturas) == 0:
        print("Nao ha dados para exportar.")
        return

    nome_arquivo = "dados_farmtech_sao_paulo.csv"
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "cultura", "comprimento_m", "largura_m",
            "area_m2", "area_ha",
            "espacamento_linha_cm", "espacamento_planta_cm",
            "ruas", "plantas",
            "dose_insumo_kg_ha", "insumo_total_kg",
            "cidade", "data_consulta_clima",
            "temperatura_c", "umidade_relativa_pct",
            "vento_kmh", "probabilidade_chuva_pct", "alerta_climatico"
        ])
        for i in range(len(culturas)):
            writer.writerow([
                culturas[i], comprimentos[i], larguras[i],
                areas_m2[i], areas_ha[i],
                espacamentos_linha[i], espacamentos_planta[i],
                ruas[i], plantas[i],
                doses_insumo[i], insumos_totais[i],
                cidades[i], datas_consulta_clima[i],
                temperaturas[i], umidades[i],
                ventos[i], probabilidades_chuva[i], alertas_climaticos[i]
            ])

    print(f"Arquivo '{nome_arquivo}' exportado com sucesso para analise em R!")


# ============================================================
# Menu principal
# ============================================================

def menu():
    while True:
        print("\n" + "=" * 55)
        print("  FARMTECH SOLUTIONS - Menu Principal")
        print("=" * 55)
        print("1 - Entrada de dados (Cadastrar terreno)")
        print("2 - Saida de dados (Listar terrenos)")
        print("3 - Atualizacao de dados (Editar terreno)")
        print("4 - Delecao de dados (Excluir terreno)")
        print("5 - Exportar dados para R (CSV)")
        print("6 - Consultar clima atual de Sao Paulo")
        print("7 - Sair do programa")
        print("=" * 55)

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            mostrar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            exportar_csv()
        elif opcao == "6":
            mostrar_clima_atual()
        elif opcao == "7":
            print("Encerrando o sistema FarmTech. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu()
