
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌾 Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar

## 📌 Nome do grupo: *A definir*

## 👨‍🎓 Integrantes:
- Thiago Scutari - RM562831  
- Marcos Fernandes - RM...  
- Henrique - RM...  
- Victor - RM...  
- Mariana - RM...

## 👩‍🏫 Professores:

### Tutor  
- Leonardo Ruiz Orabona

### Coordenador  
- Andre Godoi Chiovato

---

## 📜 Descrição

Este projeto tem como objetivo desenvolver uma solução prática e funcional para o **planejamento de plantio e colheita da cultura da cana-de-açúcar**, com base nas necessidades reais do agronegócio brasileiro, sobretudo na **redução de perdas por colheita mecanizada desorganizada**.

A aplicação contempla:

- Cálculo da área do terreno a partir da forma geométrica (quadrado, retângulo, trapézio)
- Escalonamento de plantio e colheita com datas definidas pelo usuário
- Entrada de dados personalizados: número de máquinas e produtividade diária
- Geração de indicadores por lote com percentual de execução
- Alertas operacionais com sugestões de ajuste na capacidade
- Exportação de relatórios em JSON e CSV com chave única
- Interface em terminal com validação de entradas e usabilidade simples
- Banco de dados SQLite para persistência de informações

---

## 📁 Estrutura de pastas

```
.
├── assets/                 # Imagens e elementos visuais
├── document/               # Documentação de apoio (pode incluir PDF, outros arquivos)
├── src/                    # Código-fonte do projeto
│   ├── main.py             # Arquivo principal
│   └── banco.py            # Funções de banco de dados
├── relatorio_area_*.json  # Exportações em JSON por simulação
├── relatorio_area_*.csv   # Exportações em CSV por simulação
├── escalonamento_area_*.csv  # Exportações específicas de plantio e colheita
├── requirements.txt        # Bibliotecas utilizadas
└── README.md               # Guia do projeto
```

---

## 🔧 Como executar o projeto

### ✔️ Requisitos:
- Python 3.10+
- Biblioteca padrão do Python (`sqlite3`, `csv`, `json`)
- Sistema operacional: Windows/Linux/Mac

### ▶️ Passo a passo:

1. **Clone o repositório:**

```bash
git clone https://github.com/ThiagoScutari/cap_6_python_e_alem.git
cd cap_6_python_e_alem
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o programa:**

```bash
python main.py
```

---

## 🗃 Histórico de Lançamentos

* 1.0.0 - 22/04/2025  
  - Versão final com escalonamento, exportação, banco de dados, alertas e interface interativa

* 0.9.0 - 20/04/2025  
  - Implementação de barra de progresso, datas configuráveis e alertas de capacidade

* 0.8.0 - 18/04/2025  
  - Exportação CSV e JSON com chave única por execução

* 0.6.0 - 15/04/2025  
  - Persistência com SQLite e visualização de dimensões

---

## 📋 Licença

Este projeto foi desenvolvido como parte do curso da FIAP e está licenciado sob [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1).

---
