```markdown
# 🌱 Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar

Este projeto simula o planejamento de áreas de cultivo de cana-de-açúcar, permitindo o cadastro de terrenos com formas geométricas variadas, cálculo de área, estimativa de tempo de plantio e colheita e exportação dos dados. A solução persiste os dados em um banco SQLite e fornece ferramentas para análise posterior em JSON e CSV.

---

## 🧠 Objetivo

Proporcionar uma solução prática para apoio ao planejamento agrícola com integração de:

- Programação orientada a objetos (POO)
- Manipulação de banco de dados relacional (SQLite)
- Validação de entrada
- Interface interativa no terminal
- Exportação de dados estruturados

---

## ⚙️ Funcionalidades

✅ Cálculo de área com base nas formas:
- Quadrado
- Retângulo
- Trapézio

✅ Cálculo de escalonamento de plantio e colheita com base na capacidade por máquina

✅ Armazenamento persistente dos dados:
- Tabela de áreas
- Tabela de dimensões (relacionada por ID)

✅ Menu interativo com as opções:
1. Cadastrar nova área  
2. Listar áreas cadastradas  
3. Visualizar dimensões de uma área  
4. Calcular escalonamento de plantio e colheita  
5. Exportar simulação por ID (JSON e CSV)  
6. Exportar todas as simulações (JSON e CSV)  
0. Sair

✅ Exportações:
- `relatorio_area_<id>.json` e `relatorio_area_<id>.csv`
- `relatorio_completo.json` e `relatorio_completo.csv`

---

## 🧪 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/ThiagoScutari/cap_6_python_e_alem.git
```

### 2. Acesse a pasta do projeto
```bash
cd cap_6_python_e_alem/cap_06
```

### 3. Instale as dependências (se necessário)
```bash
pip install -r requirements.txt
```

### 4. Execute o programa
```bash
python cap_06_python_e_alem.py
```

---

## 🗂 Estrutura do Projeto

```
cap_06/
│
├── banco.py                  # Persistência no SQLite
├── cap_06_python_e_alem.py   # Código principal do sistema
├── simulacoes.db             # Banco local (não versionado)
├── requirements.txt          # Bibliotecas necessárias
├── relatorio_area_<id>.json  # Exportações individuais (geradas pelo sistema)
├── relatorio_completo.json   # Exportação de todo o banco
└── README.md                 # Este arquivo
```

---

## 🖼 Exemplo de Execução

```
============================================================
MENU PRINCIPAL
============================================================
1 - Cadastrar nova área
2 - Listar áreas cadastradas
3 - Visualizar dimensões de uma área
4 - Calcular escalonamento de plantio e colheita
5 - Exportar simulação em JSON e CSV
6 - Exportar todas as simulações em JSON e CSV
0 - Sair
============================================================
```

---

## 📌 Observações

- O banco `simulacoes.db` é criado automaticamente.
- Os arquivos `.json` e `.csv` são gerados na raiz da pasta do projeto.
- O projeto está preparado para expansão futura (GUI, exportação PDF, integração com Oracle DB, etc.)

---

## 👨‍💻 Autor

**Thiago Scutari da Silva**  
Analista de Negócios e Projetos  
FIAP | Tecnologia em Inteligência Artificial
[LinkedIn](https://www.linkedin.com/in/thiago-scutari-2aa0a097)


---

```