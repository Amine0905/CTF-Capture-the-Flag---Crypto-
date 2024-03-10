from sympy import isprime, nextprime
from concurrent.futures import ThreadPoolExecutor

def find_p_and_factorization_worker(args):
    a, b, q, lower_r, upper_r = args
    r = nextprime(lower_r)
    i = 0
    while r < upper_r:
        i += 1
        print(f"Tentative {i}")
        p = 2 * q * r + 1
        if isprime(p):
            return p, r
        r = nextprime(r)
    return None, None

def find_p_and_factorization(a, b, q, num_threads=4):
    lower_r = (a - 1) // (2 * q)
    upper_r = (b - 1) // (2 * q)

    # Diviser l'intervalle en sections pour le traitement parallèle
    ranges = [(a, b, q, lower_r + i * (upper_r - lower_r) // num_threads, lower_r + (i + 1) * (upper_r - lower_r) // num_threads) for i in range(num_threads)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(find_p_and_factorization_worker, ranges))

    for p, r in results:
        if p is not None:
            return p, r
    return None, None

def find_generator(p, q, r):
    phi = p - 1
    factors = [2, q, r]

    for g in range(2, p):
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g
    return None

if __name__ == "__main__":
    a_hex = "db94fe902ae16f0b3970a5c86441ce53e72c3999c49dc794aeee4ad83c29a588081b3f1c7941c6c856a5e365e0af76bcd8debeede79f1707a1ed3f00665bb396a2f7c568530b0156876f5ae8c693d69d7d3b944e8ca057400d6819a60d4d153b9fb79128daa04ceb7060f296ee4a523311e7a5b48b5122bab6567ec490d8def65ee6c5e41d60a33dc32f38ea4ac7f5799a7eb87f4cb88ed34fb511e28499097581bd1bf5b182763637f8efd589250bf900ea6cf19fd7e114829caa0396198f6ac202cd8078d3a00e8fc15c10ecce818714d261e6c83ef5b89ed653510d49e7fbae6de0c5230466116904b8d60a8cf2cee090a75993da742fa8bc888d5d9d7eb8"
    q_hex = "25ad107ac60cd4041b24a961f09675383f2235ca9bac9582e5652053d4dc4b8c54c928e54650068ffc91ce749d31649"
    a = int(a_hex, 16)
    b = a + 2**1950
    q = int(q_hex, 16)

    p, r = find_p_and_factorization(a, b, q)
    if p is not None:
        print(f"\nFactorisation de (p-1)/q:\n2, {r}")
    else:
        print("Aucun p valide trouvé dans l'intervalle.")

    g = find_generator(p, q, r)
    if g is not None:
        print(f"\nTrouvé g: \n{g}")
    else:
        print("Aucun générateur valide trouvé.")
