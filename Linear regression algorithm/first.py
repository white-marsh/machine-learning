from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

l1 = []
l2 = []
for i in range(1, 1001, 20):
    a = []
    a.append(i)
    l1.append(a)
for j in range(1, 1001, 20):
    b = []
    b.append(j/2)
    l2.append(b)
reg = LinearRegression().fit(l1, l2)
plt.plot(l1,l2,'g-')
plt.plot(l1,l2,'bo',marker = '2')
plt.plot(85.43232,42.71616,'r',marker = 'o')
plt.xlabel('num')
plt.ylabel('num/2')
plt.show()
print(85.43232,reg.predict([[85.43232]]))
input('<enter>')
