import matplotlib.pyplot as plt

x1=(3,4,5,6)
y1=(5,6,3,4)
x2=(2,5,8)
y2=(3,4,3)

plt.plot(x1,y1, label="Linea1",linewidth=2, marker="o",color="green")
plt.plot(x2,y2, label="Linea2",linewidth=2, marker="o",color="blue")
plt.title("Diagrama de Lineas")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.grid()
plt.legend()
plt.show()