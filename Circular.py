
import matplotlib.pyplot as plt
turistas=[86.9,81.8,75.9,60.7,58.2,39.3,37.7,37.6,37.5,37.4]
paises=[ 'Francia','España','EEUU','China','Italia','Mexico','Reino Unido','Turquia','Alemania','Tailandia']
explode=[0,0.2,0,0,0,0.4,0,0,0,0]
plt.pie(turistas, labels=paises,explode=explode,autopct='%1.1f%%',shadow=False ,radius=1,startangle=90)
plt.title('TOP 10 DESTINOS TURISTICOS 2017')

plt.show()