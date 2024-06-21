# TME #3 

                                               
import random
from sympy import factorint
import json

# Fonction pour multiplier tous les éléments d'une liste
def multiply_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result

# Test de primalité de Miller-Rabin
def miller_rabin_test(n, k):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Calcul de la taille en bits d'un entier
def bit_size(n):
    return (n.bit_length() + 7) // 8

# Trouver un générateur pour un nombre premier donné
def find_generator(p, divisors):
    while True:
        g = random.randrange(2, p-1)
        if all(pow(g, (p-1)//q, p) != 1 for q in divisors):
            return g

# Construction récursive du certificat de Pratt pour les diviseurs
def recursive_pratt_cert(divisors):
    result = []
    for div in divisors:
        cert_div = {'p': div}
        if div >= 1024:
            divisor_factors = []
            factors = factorint(div - 1)
            for d, exp in factors.items():
                divisor_factors.extend([d] * exp)
            cert_div['g'] = find_generator(div, divisor_factors)
            cert_div['pm1'] = recursive_pratt_cert(divisor_factors)
        result.append(cert_div)
    return result

# Fonction principale pour générer le certificat de primalité de Pratt
def generate_pratt_cert():
    # Valeurs initiales
    a = int("941eb635d05db30d08f5fa654e1a9c805e205ab533ad2c553b153e24ef6b0397ac63316d464dad182d35000fd4b34100733a24a72a88083a446745f072ca8a952561dc6ec9098712589b99d1ae06af453329781a2f359fd25c60f0749c4cbb6c8b989522f890d37783bed95e43979c1750858d907065ceacf9361c111bcc4283", 16)
    b = a + 2**960

    prime_factors = [2]
    Q_prime = 2
    c = 20000
    len_b = bit_size(b)
    maxQprim = (b-a) // (c * len_b**2)

    # Génération des diviseurs premiers
    while bit_size(maxQprim) != bit_size(Q_prime):
        pi = random.randrange(2, min(pow(2, 160), pow(2, 8 * (bit_size(maxQprim) - bit_size(Q_prime)))))
        if miller_rabin_test(pi, 10):
            Q_prime *= pi
            prime_factors.append(pi)

    p_k = random.randrange(a//Q_prime, b//Q_prime)
    while not miller_rabin_test(p_k, 1) or not miller_rabin_test(Q_prime*p_k+1, 1):
        p_k = random.randrange(a//Q_prime, b//Q_prime)

    prime_factors.append(p_k)
    p = multiply_list(prime_factors) + 1
    g = find_generator(p, prime_factors)

    cert_pratt = {'p': p, 'g': g, 'pm1': recursive_pratt_cert(prime_factors)}

    with open('flag22_tme.pratt.json', 'w') as file:
        json.dump(cert_pratt, file)

    print("Certificat généré et sauvegardé dans flag22_tme.pratt.json")

if __name__ == '__main__':
    generate_pratt_cert()
