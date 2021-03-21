import numpy as np

# Q1
a = [1, 2, 3]
b = a
a.append(4)
print(b)

# Q2
t = (23, 'abc', 4.56, (2, 3), 'def')
print(t[1:4])

# Q3
print(t[1:-1])

# Q4
print(t[:2])

# Q5
print(t[2:])

# Q6
print(np.arange(10, 30, 5))

# Q7
a = np.arange(10) ** 3
a[:6:2] = -1000
print(a)

# Q8
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
print(x_data.shape)

# Q9
print((1, 2, 3) + (4, 5, 6))

# Q10
aa = np.array([[1, 1], [0, 1]])
bb = np.array([[2, 0], [3, 4]])
print(aa * bb)
