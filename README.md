# FuelTech Dashboard em Python

Este projeto simula um **dashboard estilo FuelTech** para análise de telemetria automotiva.  
Ele processa dados de um arquivo CSV e exibe métricas como RPM, velocidade, temperatura e consumo, além de alertas de motor.

---

## Funcionalidades
- Leitura de dados de telemetria via CSV (`dados_carro.csv`)
- Análises básicas:
  - RPM máximo
  - Velocidade máxima
  - Temperatura média
  - Consumo médio
- Alerta de motor em alta temperatura
- Dashboard textual e gráfico (com **Matplotlib**)

---

## Estrutura do Projeto
## 📁 Estrutura do Projeto

```
fueltech-dashboard/
│
├── data/
│   └── dados_carro.csv
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── analyzer.py
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## ⚙️ Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/giocortezini/fueltech-dashboard.git
