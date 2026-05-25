
# analisis_climatico.py
# Análisis de datos de temperatura global (GISTEMP - NASA)
# UTN TUP - Organización Empresarial - Escenario A
# Ejecutar desde la raíz del repositorio: python scripts/analisis_climatico.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import urllib.request
import os

# --- Descarga del dataset ---
ruta_datos = "datos/temperatura_global.csv"
if not os.path.exists(ruta_datos):
    url = "https://datahub.io/core/global-temp/r/monthly.csv"
    urllib.request.urlretrieve(url, ruta_datos)
    print(f"Dataset descargado en {ruta_datos}")
else:
    print(f"Usando dataset existente en {ruta_datos}")

# --- Carga y limpieza ---
# La columna de fecha se llama "Year" en este dataset
df = pd.read_csv(ruta_datos)
df_gistemp = df[df["Source"] == "GISTEMP"].copy()
df_gistemp["Year"] = pd.to_datetime(df_gistemp["Year"])
df_gistemp = df_gistemp.sort_values("Year").reset_index(drop=True)

# --- Indicadores ---
temp_promedio = df_gistemp["Mean"].mean()
temp_maxima   = df_gistemp["Mean"].max()
temp_minima   = df_gistemp["Mean"].min()
fecha_max     = df_gistemp.loc[df_gistemp["Mean"].idxmax(), "Year"]
fecha_min     = df_gistemp.loc[df_gistemp["Mean"].idxmin(), "Year"]
ultimos_10    = df_gistemp[df_gistemp["Year"].dt.year >= df_gistemp["Year"].dt.year.max() - 10]["Mean"].mean()
primeros_10   = df_gistemp[df_gistemp["Year"].dt.year <= df_gistemp["Year"].dt.year.min() + 10]["Mean"].mean()
diferencia    = ultimos_10 - primeros_10

print(f"Anomalía promedio histórica  : {temp_promedio:+.4f} °C")
print(f"Anomalía máxima registrada   : {temp_maxima:+.4f} °C ({fecha_max.strftime('%Y-%m')}")
print(f"Anomalía mínima registrada   : {temp_minima:+.4f} °C ({fecha_min.strftime('%Y-%m')}")
print(f"Diferencia tendencial        : {diferencia:+.4f} °C")

# --- Gráfico ---
df_gistemp["tendencia_12m"] = df_gistemp["Mean"].rolling(window=12, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_gistemp["Year"], df_gistemp["Mean"], color="#90CAF9", linewidth=0.7, alpha=0.6, label="Anomalía mensual")
ax.plot(df_gistemp["Year"], df_gistemp["tendencia_12m"], color="#E53935", linewidth=2.2, label="Tendencia (media móvil 12 meses)")
ax.axhline(0, color="#555555", linewidth=0.9, linestyle="--", label="Línea base (0 °C)")
ax.fill_between(df_gistemp["Year"], df_gistemp["tendencia_12m"], 0, where=(df_gistemp["tendencia_12m"] > 0), alpha=0.08, color="red")
ax.set_title("Evolución de la Anomalía de Temperatura Global (GISTEMP - NASA)", fontsize=14, fontweight="bold")
ax.set_xlabel("Año")
ax.set_ylabel("Anomalía de temperatura (°C)")
ax.legend()
ax.grid(True, alpha=0.25)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%+.2f"))
plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png", dpi=150, bbox_inches="tight")
print("Gráfico guardado en resultados/grafico_temperatura.png")
