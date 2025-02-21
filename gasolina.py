(import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="dia", y="venda", marker="o", linewidth=2)

# Configurar o gráfico
plt.title("Preço Médio da Gasolina em São Paulo (Julho 2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.xticks(df["dia"])
plt.grid(True)

# Salvar o gráfico
plt.savefig("gasolina.png", dpi=300)

# Exibir o gráfico
plt.show())