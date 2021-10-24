from sklearn.linear_model import LinearRegression

l1 = []
l2 = []
for i in range(1, 1001):
    a = []
    a.append(i)
    l1.append(a)
for j in range(1, 1001):
    b = []
    b.append(j/2)
    l2.append(b)
reg = LinearRegression().fit(l1, l2)
print(reg.predict([[85.43232]]))
