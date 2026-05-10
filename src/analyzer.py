class Analyzer:
    def __init__(self, dados):
        self.dados = dados

    def resumo(self):
        return {
            "rpm_max": self.dados["RPM"].max(),
            "vel_max": self.dados["Velocidade"].max(),
            "temp_media": self.dados["Temperatura"].mean(),
            "consumo_medio": self.dados["Consumo"].mean()
        }

    def alerta_motor(self):
        return self.dados["Temperatura"].max() > 95
