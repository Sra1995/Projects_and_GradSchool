from math import gcd

def factor_with_period(N, a, r):
    power = r // 2
    a_power_half_r_mod_N = pow(a, power, N)
    gcd1 = gcd(a_power_half_r_mod_N - 1, N)
    gcd2 = gcd(a_power_half_r_mod_N + 1, N)
    return gcd1, gcd2

# Example usage:
N = 77
a = 43
r = 210
result1, result2 = factor_with_period(N, a, r)
print("gcd(a^(r/2) - 1, N) =", result1)
print("gcd(a^(r/2) + 1, N) =", result2)