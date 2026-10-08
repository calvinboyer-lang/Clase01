import numpy as np
import pandas as pd

datos = {
    "Mes": [1, 2, 3, 4, 5],
    "Produccion": [100, 120, 115, 140, 160]
}

df = pd.DataFrame(datos)

print("Datos de producción:")
print(df)

print("\nProducción promedio:", np.mean(df["Produccion"]))