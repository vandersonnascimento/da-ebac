import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="dia", y="venda", marker="o", label="Preço da Gasolina")

# Personalizar o gráfico
plt.title("Preço Médio da Gasolina em São Paulo (Julho de 2021)", fontsize=14)
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Preço (R$)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Salvar o gráfico
plt.savefig("gasolina.png", dpi=300, bbox_inches="tight")
plt.show()
