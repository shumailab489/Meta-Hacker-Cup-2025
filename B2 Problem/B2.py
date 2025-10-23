import os
import math

MOD = 10**9 + 7

# Modular nCr using Fermat's little theorem
def nCr_mod(n, r, mod=MOD):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return num * pow(den, mod - 2, mod) % mod

def prime_factorize(n):
    pf = {}
    x = n
    for p in range(2, int(math.isqrt(x)) + 1):
        while x % p == 0:
            pf[p] = pf.get(p, 0) + 1
            x //= p
    if x > 1:
        pf[x] = pf.get(x, 0) + 1
    return pf

def generate_divisors_from_factors(factors):
    primes = list(factors.keys())
    exponents = list(factors.values())
    divisors = [1]
    for i, p in enumerate(primes):
        new_divs = []
        for d in divisors:
            for e in range(exponents[i] + 1):
                new_divs.append(d * (p ** e))
        divisors = new_divs
    return divisors

def f_N(y, N, prime_factors_B):
    # Factorization of y shares subset of B’s primes
    pf_y = {}
    temp = y
    for p in prime_factors_B:
        e = 0
        while temp % p == 0:
            temp //= p
            e += 1
        pf_y[p] = e
    # stars and bars formula per prime
    result = 1
    for p, e in pf_y.items():
        result = (result * nCr_mod(e + N - 1, N - 1)) % MOD
    return result

def solve_case(N, A, B):
    pf_B = prime_factorize(B)
    divisors = generate_divisors_from_factors(pf_B)
    total = 0
    for x in divisors:
        if x <= A and B % x == 0:
            val = f_N(x, N, pf_B) * f_N(B // x, N, pf_B)
            total = (total + val) % MOD
    return total

def solve_file(input_path, output_path):
    with open(input_path, 'r') as fin:
        T = int(fin.readline().strip())
        results = []
        for case in range(1, T + 1):
            N, A, B = map(int, fin.readline().strip().split())
            ans = solve_case(N, A, B)
            results.append(f"Case #{case}: {ans}")
    with open(output_path, 'w') as fout:
        fout.write("\n".join(results))

if __name__ == "__main__":
    base_path = r"C:\Users\Abbas Buzdar\Desktop\Meta Hacker Cup"
    input_file = os.path.join(base_path, "final_product_chapter_2_input.txt")
    output_file = os.path.join(base_path, "final_product_chapter_2_output.txt")
    solve_file(input_file, output_file)
    print(f"✅ Output written to: {output_file}")
