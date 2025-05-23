
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="cap_06/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%">
  </a>
</p>

<br>

# 🌾 Sistema de Planejamento e Escalonamento de Plantio e Colheita da Cana-de-Açúcar

## 📌 Grupo: 81

## 👨‍🎓 Integrantes:
- Thiago Scutari - RM562831 | thiago.scutari@outlook.com 
- Marcos Fernandes - RM564998 | mareligumarcos@gmail.com
- Henrique Ribeiro Siqueira - RM565044 | henrique.ribeiro1201@gmail.com
- Victor Emmanuel Lucioli Barbosa - RM562884 | victorluciolibarbosa.2004@gmail.com
- Mariana Cavalcante Oliveira - RM561678 | mari.kvalcant@gmail.com

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
cap_06/
├── src/
│   ├── main.py
│   └── banco.py
├── relatorios/
│   ├── relatorio_area_1.csv
│   └── relatorio_area_1.json
├── escalonamentos/
│   ├── escalonamento_area_1_colheita_*.csv
│   └── escalonamento_area_1_plantio_*.csv
├── document/
│   ├── Simplificado.docx
│   └── variaveis plantacao de Cana-de-Açúcar[1].docx
├── simulacoes.db
├── requirements.txt
└── README.md

```

---

## 🔧 Como executar o projeto

### ✔️ Requisitos:
- Python 3.10+
- Biblioteca padrão do Python (`sqlite3`, `csv`, `json`, `math`, `random`, `string`, `datetime`)
- Sistema operacional: Windows/Linux/Mac

### ▶️ Passo a passo:

1. **Clone o repositório:**

```bash
git clone https://github.com/ThiagoScutari/cap_6_python_e_alem.git
cd cap_6
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

[LinkedIn](https://www.linkedin.com/in/thiago-scutari-2aa0a097)
[Github](https://github.com/ThiagoScutari)

---

```