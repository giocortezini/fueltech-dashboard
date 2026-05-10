from data_loader import DataLoader
from analyzer import Analyzer
from dashboard import Dashboard

def main():
    # Carregar dados
    loader = DataLoader("data/dados_carro.csv")
    dados = loader.carregar()

    # Análise
    analyzer = Analyzer(dados)

    resumo = analyzer.resumo()

    print("\n" + "=" * 50)
    print(" DASHBOARD DE TELEMETRIA - RESUMO")
    print("=" * 50)

    print(f"RPM máximo        : {resumo['rpm_max']:.0f} rpm")
    print(f"Velocidade máxima : {resumo['vel_max']:.0f} km/h")
    print(f"Temperatura média : {resumo['temp_media']:.1f} °C")
    print(f"Consumo médio     : {resumo['consumo_medio']:.2f}")

    print("=" * 50)

    if analyzer.alerta_motor():
        print("⚠  ALERTA: MOTOR OPERANDO EM ALTA TEMPERATURA!")
    else:
        print("Motor em condições normais")

    print("=" * 50 + "\n")

    # Dashboard gráfico
    dashboard = Dashboard(dados)
    dashboard.gerar()


if __name__ == "__main__":
    main()