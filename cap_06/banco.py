#------------------------------------| BANCO DE DADOS |------------------------------------#

import sqlite3

def criar_tabelas():
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
