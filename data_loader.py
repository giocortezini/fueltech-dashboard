import pandas as pd

class DataLoader:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv

    def carregar(self):
        return pd.read_csv(self.arquivo_csv, sep=";")