N = 77
a = 2

for i in range(1, 201):
    result = pow(a, i, N)
    print(f"2^{i} mod 77 = {result}")
