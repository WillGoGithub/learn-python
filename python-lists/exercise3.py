L1 = [1, 2, 3]
L2 = [4, 5, 6, *L1]
L3 = [n for n in L1]
L4 = [L1]
L5 = [*L1]
print(L2)
print(L3, L4, L5)
