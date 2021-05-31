import csv
import matplotlib.pyplot as plt
import numpy as np
costo=[]
cambio_aceite=[]
with open("1.csv",encoding='utf-8',newline='') as f:

    Reader= enumerate(csv.reader(f))

    for i, row in Reader:
        if i>0:
            try:
                costo.append(int(row[0]))
                cambio_aceite.append(int(row[1]))
            except Exception:
                print(Exception)
plt.scatter(cambio_aceite,costo,c="g",alpha=0.5,s=100)
plt.title("Grafico de Dispersion")
plt.xlabel("Cambio de aceite")
plt.ylabel("Costo")
plt.show()