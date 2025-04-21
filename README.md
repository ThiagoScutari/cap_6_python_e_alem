---

## 🧱 Estrutura recomendada para seu projeto

Aqui está um modelo de README adaptado ao seu sistema:

```markdown
# 🌱 Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar

Este projeto simula o planejamento e cálculo da área de cultivo de cana-de-açúcar, com base em formas geométricas comuns (quadrado, retângulo e trapézio). Também realiza o registro das simulações em banco de dados local (SQLite), permitindo o acompanhamento histórico das áreas cadastradas.

---

## 🧠 Objetivo

Criar uma solução em Python que simule a realidade do agronegócio — com foco no plantio de cana — integrando conceitos de:

- Programação orientada a objetos
- Validação de dados
- Manipulação de banco de dados SQLite
- Estrutura modular e reutilizável

---

## ⚙️ Funcionalidades

- Cálculo de área de cultivo com diferentes formas geométricas
- Validação de entradas numéricas do usuário
- Registro automático da área e suas dimensões no banco de dados `simulacoes.db`
- Consulta de áreas cadastradas
- Preparado para futura expansão (ex: escalonamento, exportação, migração para Oracle)

---

## 🛠 Tecnologias e Recursos Utilizados

- Python 3.13+
- SQLite3 (banco de dados local)
- VSCode + Extensão SQLite Viewer
- Controle de versão com Git/GitHub

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

### 4. Execute o programa principal
```bash
python cap_06_python_e_alem.py
```

> O banco de dados `simulacoes.db` será criado automaticamente com as tabelas necessárias.

---

## 🗂 Estrutura de Diretórios

```
cap_06/
│
├── banco.py                  # Módulo de persistência (SQLite)
├── cap_06_python_e_alem.py   # Lógica principal e interface com o usuário
├── requirements.txt          # Dependências do projeto
├── simulacoes.db             # (ignorado no Git) Banco local com simulações
└── README.md                 # Este arquivo
```

---

## 🖼 Exemplo de Execução

```
Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar

Escolha a forma da área:
1 - Quadrado
2 - Retângulo
3 - Trapézio
4 - Listar áreas cadastradas
0 - Sair

Áreas cadastradas:
ID: 1 | Forma: Quadrado | Área: 10000.00 m² | Data: 2025-04-21 19:11:01
```

---

## 📌 Observações

- O projeto está preparado para evoluções como:
  - Cálculo de escalonamento de plantio e colheita
  - Exportação em JSON
  - Integração com Oracle DB
- O banco de dados `simulacoes.db` **não é versionado**. Ele será recriado automaticamente na primeira execução.

---

## 👨‍💻 Autor

**Thiago Scutari da Silva**  
Analista de Negócios e Projetos  
FIAP | Tecnologia em Inteligência Artificial
[LinkedIn](https://www.linkedin.com/in/thiago-scutari-2aa0a097)

---
```