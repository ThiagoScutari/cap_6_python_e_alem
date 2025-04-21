#------------------------------------| BANCO DE DADOS |------------------------------------#

import sqlite3
from datetime import datetime

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

#Lê os dados do banco de dados
def listar_areas_salvas()-> None:
    conn = sqlite3.connect("simulacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM areas")
    registros = cursor.fetchall()
    conn.close()
    return registros

