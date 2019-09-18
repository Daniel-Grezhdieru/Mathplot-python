import matplotlib.pyplot as plt
import numpy as rgm
R=rgm.linspace(0,4,1000)
y=1/3
X = []
Y = []
k=1
for r in R: 
    X.append(r)
    y = rgm.random.random(10)
    for l in range(1001):
      y=r*y*(1-y)
    Y.append(y)
plt.title("Бифуркационная диаграмма")
plt.xlabel("r") 
plt.ylabel("X[0]")
plt.grid()     
plt.plot(X, Y, ",m")
plt.show()