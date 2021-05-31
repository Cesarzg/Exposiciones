import numpy as np
import matplotlib.pyplot as plt

data1=(50,40,30,70,140,200)
data2=(50,50,50,50,50,50)
data3=(50,100,150,150,100,50)
year=("2016", "2017", "2018", "2019","2020", "2021")
plt.figure(figsize=(9,8))
plt.bar(year,data3,color="red",label="Dante")
plt.bar(year,data2,color="blue",bottom=np.array(data3),label="Alysson")
plt.bar(year,data1,color="green",bottom=np.array(data3)+np.array(data2),label="Pablo")
plt.title("Grupo Vagabond")
plt.ylabel("Investigacion")
plt.xlabel("Años")
plt.legend(loc="lower left",bbox_to_anchor=(0.9,1.0))
plt.show()