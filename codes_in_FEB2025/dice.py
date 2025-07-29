import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])
# c = np.array([1,2,3,4,5,6])

k = [(x,y) for x in a for y in b]
print(k)
# print(len(k))
l = [(x+y) for x in a for y in b]
print(l)
m = l.count(6)
print(m)

# g = len(k)
prob1 = (m/len(k))

print(f'probability of getting sum equals 6 when two identical dices are rolled is:{prob1}')
# d = [(1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6)]

# e = set(d).intersection(k)
# [int(1,2,3,4,5,6)]
# print(e)
# print(len(e))
