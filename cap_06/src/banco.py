#------------------------------------| BANCO DE DADOS |------------------------------------#

import sqlite3, json, csv, math, random, string
from datetime import datetime, timedelta


#Cria o banco de dados e as tabelas
def criar_tabelas()-> None:
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS areas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            forma TEXT NOT NULL,
            area REAL NOT NULL,
            data_criacao TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dimensoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_area INTEGER NOT NULL,
            nome_dimensao TEXT NOT NULL,
            valor REAL NOT NULL,
            FOREIGN KEY (id_area) REFERENCES areas(id)
        );
    ''')

    conn.commit()
    conn.close()

#------------------------------------| INSERÇÃO DE DADOS |------------------------------------#
#Verifica valor digitado pelo usuario
def inserir_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

#Insere os dados no banco de dados
def inserir_area(area_obj)-> int:
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()

    forma = area_obj.forma
    area_calculada = area_obj.calcular_area()
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO areas (forma, area, data_criacao)
        VALUES (?, ?, ?)
    ''', (forma, area_calculada, data_criacao))

    conn.commit()
    area_id = cursor.lastrowid
    conn.close()
    return area_id

#Insere as dimensões no banco de dados
def inserir_dimensoes(area_id, dimensoes_dict)-> None:
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()

    for nome, valor in dimensoes_dict.items():
        cursor.execute('''
            INSERT INTO dimensoes (id_area, nome_dimensao, valor)
            VALUES (?, ?, ?)
        ''', (area_id, nome, valor))
    conn.commit()
    conn.close()

#Insere data
def inserir_data(msg: str)-> datetime:
    while True:
        data = input(f"{msg} (formato: DD/MM/AAAA): ").strip()
        try:
            return datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("Data inválida. Tente novamente.")


#Ler quantiade de máquinas
def inserir_qtd_maquinas(tipo: str) -> int:
    while True:
        try:
            qtd = int(input(f"Digite a quantidade de máquinas para {tipo}: "))
            if qtd <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
            return qtd
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def gerar_chave_aleatoria(tamanho=8):
    return ''.join(random.choices(string.digits, k=tamanho))

#------------------------------------| VISUALIZAÇÃO DE DADOS |------------------------------------#

#Lê os dados do banco de dados
def listar_areas_salvas() -> list:
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM areas")
    registros = cursor.fetchall()
    conn.close()
    if not registros:
        print("Sem registros cadastrados no banco.")
    return registros

#Função para mostrar as áreas salvas no banco de dados
def mostrar_areas_salvas():
    registros = listar_areas_salvas()
    if not registros:
        return  # evita erro ao tentar iterar None
    print("\nÁreas cadastradas:")
    for id_area, forma, area, data in registros:
        print(f"ID: {id_area} | Forma do terreno: {forma} | Área: {area:.2f} m² | Data: {data}")

#Lista dimensões de uma área
def visualizar_dimensoes():
    print("\n" + "="*60)
    mostrar_areas_salvas()
    print("\n" + "="*60)
    try:
        id_area = int(input("Digite o ID da área que deseja consultar: "))
        conn = sqlite3.connect("simulacoes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM areas")
        ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        if id_area not in ids:
            print("ID inválido.")
            return
    except ValueError:
        print("ID inválido.")
        return
    
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome_dimensao, valor FROM dimensoes WHERE id_area = ?", (id_area,))
    dados = cursor.fetchall()
    conn.close()

    if not dados:
        print("Nenhuma dimensão encontrada para essa área.")
    else:
        print(f"\nDimensões da área ID {id_area}:")
        for nome, valor in dados:
            print(f"{nome}: {valor} metros")

#------------------------------------| ESCALONAMENTO |------------------------------------#
#Calcula dias para plantio e colheita
def calcular_dias_execucao(area_total: float, capacidade_maquina: int, qtd_maquinas: int)-> float:
    total_capacidade_dia = capacidade_maquina * qtd_maquinas
    dias = area_total / total_capacidade_dia
    return round(dias, 2)

#Calcula escalonamento de plantio e colheita
def gerar_escalonamento(area_total, capacidade_dia, qtd_maquinas, tipo, data_inicio):
    total_dia = capacidade_dia * qtd_maquinas
    dias = math.ceil(area_total / total_dia)

    print(f"\n📆 Escalonamento de {tipo.capitalize()}:")

    acumulado = 0
    for i in range(dias):
        data_lote = data_inicio + timedelta(days=i)

        if acumulado + total_dia > area_total:
            restante = area_total - acumulado
        else:
            restante = total_dia

        acumulado += restante
        percentual = (acumulado / area_total) * 100

        barra = "|" * int(percentual // 5)  # 20 blocos máx (100 / 5)
        print(f"Lote {i+1:<2}: {data_lote.strftime('%d/%m/%Y')} → {int(acumulado):>5} m² / {int(area_total):>5} m² ({percentual:>6.2f}%)  |{barra}")
    data_fim = data_inicio + timedelta(days=dias - 1)
    print(f"\n📅 Previsão de término de {tipo.lower()}: {data_fim.strftime('%d/%m/%Y')} ({dias} dias no total)")

def realizar_escalonamento():
    mostrar_areas_salvas()
    try:
        id_area = int(input("Digite o ID da área para escalonamento: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT area FROM areas WHERE id = ?", (id_area,))
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        print("Área não encontrada.")
        return

    area_total = resultado[0]

    qtd_plantio = inserir_qtd_maquinas("plantio")
    capacidade_plantio = inserir_valor("Digite a capacidade de plantio por máquina (em m²/dia): ")

    qtd_colheita = inserir_qtd_maquinas("colheita")
    capacidade_colheita = inserir_valor("Digite a capacidade de colheita por máquina (em m²/dia): ")

    dias_plantio = calcular_dias_execucao(area_total, capacidade_plantio, qtd_plantio)
    dias_colheita = calcular_dias_execucao(area_total, capacidade_colheita, qtd_colheita)

    # Solicita ao usuário as datas de início
    print("\n📅 Informe a data de início do plantio:")
    data_inicio_plantio = inserir_data("Data de início do plantio")

    print("\n📅 Informe a data estimada de início da colheita:")
    data_inicio_colheita = inserir_data("Data de início da colheita")

    print(f"\n⏱ Estimativas:")
    print(f"- Plantio: {dias_plantio} dias")
    print(f"- Colheita: {dias_colheita} dias")

    gerar_escalonamento(area_total, capacidade_plantio, qtd_plantio, "plantio", data_inicio_plantio)
    gerar_escalonamento(area_total, capacidade_colheita, qtd_colheita, "colheita", data_inicio_colheita)

    # Comparação de capacidades operacionais
    total_plantio_dia = capacidade_plantio * qtd_plantio
    total_colheita_dia = capacidade_colheita * qtd_colheita

    print("\n📊 Comparativo de capacidades operacionais:")
    print(f"- Capacidade total de plantio: {total_plantio_dia:.2f} m²/dia")
    print(f"- Capacidade total de colheita: {total_colheita_dia:.2f} m²/dia")

    # Avaliação de descompasso
    if total_plantio_dia > total_colheita_dia * 1.5:
        print("\n⚠️ ALERTA OPERACIONAL: Plantio acima da capacidade de colheita.")
        deficit = total_plantio_dia - total_colheita_dia
        maquinas_necessarias = math.ceil(total_plantio_dia / capacidade_colheita)
        print(f"A colheita está defasada em {deficit:.2f} m²/dia.")
        print(f"💡 Sugestão: aumente a quantidade de máquinas de colheita para pelo menos {maquinas_necessarias}.")

    elif total_colheita_dia > total_plantio_dia * 1.5:
        print("\n⚠️ ALERTA OPERACIONAL: Colheita acima da capacidade de plantio.")
        ociosidade = total_colheita_dia - total_plantio_dia
        maquinas_necessarias = math.ceil(total_colheita_dia / capacidade_plantio)
        print(f"O plantio está limitado, gerando ociosidade de {ociosidade:.2f} m²/dia.")
        print(f"💡 Sugestão: aumente a quantidade de máquinas de plantio para pelo menos {maquinas_necessarias}.")
    
    #exporta os dados de escalonamento
    exportar_escalonamento_csv(id_area, "plantio", data_inicio_plantio, area_total, capacidade_plantio, qtd_plantio)
    exportar_escalonamento_csv(id_area, "colheita", data_inicio_colheita, area_total, capacidade_colheita, qtd_colheita)

#------------------------------------| EXPORTAÇÃO |------------------------------------#
#Exporta os dados para JSON e CSV de uma area específica
def exportar_simulacao(id_area):
    chave = gerar_chave_aleatoria()
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()

    # Consulta dados da área
    cursor.execute("SELECT forma, area, data_criacao FROM areas WHERE id = ?", (id_area,))
    area = cursor.fetchone()
    if not area:
        print("⚠️ Área não encontrada.")
        return

    forma, area_total, data = area

    # Consulta dimensões
    cursor.execute("SELECT nome_dimensao, valor FROM dimensoes WHERE id_area = ?", (id_area,))
    dimensoes = cursor.fetchall()
    conn.close()

    # Monta dicionário para exportação
    dados = {
        "id_area": id_area,
        "forma": forma,
        "area_m2": area_total,
        "data_criacao": data,
        "dimensoes": {nome: valor for nome, valor in dimensoes}
    }

    # Exporta para JSON
    with open(f"relatorios/relatorio_area_{id_area}_{chave}.json", "w", encoding="utf-8") as f_json:
        json.dump(dados, f_json, indent=4, ensure_ascii=False)
    print(f"✅ Relatório JSON exportado: relatorio_area_{id_area}.json")
 
    # Exporta para CSV
    with open(f"relatorios/relatorio_area_{id_area}_{chave}.csv", "w", newline="", encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["ID", "Forma", "Área (m²)", "Data de Criação"])
        writer.writerow([id_area, forma, area_total, data])
        writer.writerow([])
        writer.writerow(["Dimensão", "Valor (m)"])
        for nome, valor in dimensoes:
            writer.writerow([nome, valor])
    print(f"✅ Relatório CSV exportado: relatorio_area_{id_area}.csv")

#Exporta todas as simulações para JSON e CSV
def exportar_todas_simulacoes():
    chave = gerar_chave_aleatoria()
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()

    # Consulta todas as áreas
    cursor.execute("SELECT id, forma, area, data_criacao FROM areas")
    areas = cursor.fetchall()
    if not areas:
        print("⚠️ Nenhuma área cadastrada no banco.")
        return

    relatorio_json = []
    relatorio_csv = [["ID", "Forma", "Área (m²)", "Data de Criação", "Dimensão", "Valor (m)"]]

    for id_area, forma, area_total, data in areas:
        # Consulta dimensões de cada área
        cursor.execute("SELECT nome_dimensao, valor FROM dimensoes WHERE id_area = ?", (id_area,))
        dimensoes = cursor.fetchall()

        # JSON
        relatorio_json.append({
            "id_area": id_area,
            "forma": forma,
            "area_m2": area_total,
            "data_criacao": data,
            "dimensoes": {nome: valor for nome, valor in dimensoes}
        })

        # CSV
        for nome, valor in dimensoes:
            relatorio_csv.append([id_area, forma, area_total, data, nome, valor])

    conn.close()

    # Exporta JSON
    with open(f"relatorios/relatorio_completo_{chave}.json", "w", encoding="utf-8") as f_json:
        json.dump(relatorio_json, f_json, indent=4, ensure_ascii=False)
    print(f"✅ Relatório JSON exportado: relatorio_completo_{chave}.json")

    # Exporta CSV
    with open(f"relatorios/relatorio_completo_{chave}.csv", "w", newline='', encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerows(relatorio_csv)
    print(f"✅ Relatório CSV exportado: relatorio_completo_{chave}.csv")

#Exporta dados de escalonamento
def exportar_escalonamento_csv(id_area, tipo, data_inicio, area_total, capacidade_dia, qtd_maquinas):
    chave = gerar_chave_aleatoria()
    nome_arquivo = f"escalonamento_area_{id_area}_{tipo.lower()}_{chave}.csv"
    total_dia = capacidade_dia * qtd_maquinas
    dias = math.ceil(area_total / total_dia)

    acumulado = 0

    with open(nome_arquivo, "w", newline='', encoding='utf-8') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["Lote", "Data", "Tipo", "Executado (m²)", "Acumulado (m²)", "Percentual (%)"])

        for i in range(dias):
            data_lote = data_inicio + timedelta(days=i)
            if acumulado + total_dia > area_total:
                executado = area_total - acumulado
            else:
                executado = total_dia

            acumulado += executado
            percentual = (acumulado / area_total) * 100

            writer.writerow([
                f"Lote {i+1}",
                data_lote.strftime("%d/%m/%Y"),
                tipo.capitalize(),
                int(executado),
                int(acumulado),
                f"{percentual:.2f}"
            ])

    print(f"✅ Escalonamento de {tipo} exportado para {nome_arquivo}")

