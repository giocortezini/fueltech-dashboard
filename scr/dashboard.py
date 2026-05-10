import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Dashboard:
    def __init__(self, dados):
        self.dados = dados

    def gerar(self):
        plt.style.use("dark_background")

        fig, axs = plt.subplots(1, 2, figsize=(14, 6))

        # GRÁFICO 1 - ESTÁTICO
        axs[0].plot(
            self.dados["Velocidade"],
            self.dados["RPM"],
            linewidth=2,
            color="lime"
        )
        axs[0].set_title("RPM vs Velocidade")
        axs[0].set_xlabel("Velocidade")
        axs[0].set_ylabel("RPM")
        axs[0].grid(alpha=0.3)

        # GRÁFICO 2 - ANIMAÇÃO
        ax_rpm = axs[1]
        ax_temp = ax_rpm.twinx()
        ax_vel = ax_rpm.twinx()

        # desloca terceiro eixo
        ax_vel.spines["right"].set_position(("outward", 60))

        line_rpm, = ax_rpm.plot([], [], "r", label="RPM")
        line_temp, = ax_temp.plot([], [], "b", label="Temperatura")
        line_vel, = ax_vel.plot([], [], "g", label="Velocidade")

        ax_rpm.set_title("Telemetria em tempo real")
        ax_rpm.set_xlim(0, len(self.dados))

        ax_rpm.set_ylabel("RPM", color="red")
        ax_temp.set_ylabel("Temperatura (°C)", color="blue")
        ax_vel.set_ylabel("Velocidade (km/h)", color="green")

        ax_rpm.set_ylim(0, self.dados["RPM"].max() + 500)
        ax_temp.set_ylim(0, self.dados["Temperatura"].max() + 10)
        ax_vel.set_ylim(0, self.dados["Velocidade"].max() + 10)

        def init():
            line_rpm.set_data([], [])
            line_temp.set_data([], [])
            line_vel.set_data([], [])
            return line_rpm, line_temp, line_vel

        def update(i):
            x = self.dados.index[:i]

            line_rpm.set_data(x, self.dados["RPM"][:i])
            line_temp.set_data(x, self.dados["Temperatura"][:i])
            line_vel.set_data(x, self.dados["Velocidade"][:i])

            return line_rpm, line_temp, line_vel

        self.ani = animation.FuncAnimation(
            fig,
            update,
            frames=len(self.dados),
            init_func=init,
            interval=200,
            blit=False,
            repeat=False 
        )

        plt.tight_layout()
        plt.show()
