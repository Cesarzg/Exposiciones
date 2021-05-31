
import matplotlib.pyplot as plt
 
datos= [1,2,3,4,5,6,7,8,9,10,15,16,25,26,27,28,29,35,
            45,46,47,48,49,50,51,52]
div= [0,10,20,30,40,50]
 
inicio=0
fin=50
ancho=10
plt.hist(datos,5)
plt.grid()
plt.title("Histograma de edades")
plt.show()