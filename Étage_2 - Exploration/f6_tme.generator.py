import random
from sympy import isprime



def generate_p(a, b, q):
    
    # On recherche le premier nombre multiple de q dans l'intervalle [a, b) et le définir comme point de départ
    r = (a - 1) % q
    if r != 0:
        step = q - r
    else:
        step = 0
    start = a + step

    # Et on parcours les nombres dans l'intervalle [a, b) par pas de q à partir de ce point de départ jusqu'à trouver un nombre premier
    for p in range(start, b, q):
        if isprime(p):
            return p


def generate_g(p, q):
    
    while True:
        x = random.randint(2, p - 2)
        g = pow(x, (p - 1) // q, p)
        if g != 1:
            return g


if __name__ == "__main__":
    # Convertir les chaînes hexadécimales en entiers
    a_hex = "84d26c4a96c59010348d8a81e9e99d45e0c396e5e16ea114dc431611f32a4aa2e2e3ea89f4e22ff40589f49ce247252025a110aed3626243ef87f14f635ec5e917305b813328406cba03964ca1e7a7950aedeb2ca47b47aa970dfee2a57dafeb21e383357bf765674d4bf82d8369c2c630cdb70ed04d828b27ec008cea27a89fa0f9e11de27e39ad946e136f51f0187b03f8b5f3222ef0c5aea2d7002dbe6743b8e35494854dac4def3ce89f922fed12e28f90bc134ad54828eb17a1992dd3856d55e9c70ceb7d9c2d0b1c353dbadf2b81b29af32f0c04224a4c8d18f1fbdad5a689ebf54c2670175a08c4e2193c7ad565186ed63d63412ca98e10828a444111"
    a = int(a_hex, 16)
    b =  a + 2**1950
    q = int("8ebb1871e7fb183563f5e5a6cd7d3a9ffdaa518dbb4f84e3fce24da18e68e905", 16)

    # Générer p
    p = generate_p(a, b, q)
    assert a <= p < b, f"Erreur: p ({p}) n'est pas dans l'intervalle [a, b)"
    assert (p - 1) % q == 0, f"Erreur: p ({p}) - 1 n'est pas un multiple de q ({q})"

    # Générer g
    g = generate_g(p, q)
    assert pow(g, q, p) == 1, "Erreur: g**q == 1 mod p"

    print(f"p premier tel que (a <= p < b) et (p - 1) soit un multiple de q: \n{p}")
    print(f"g tel que g**q == 1 mod p: \n{g}")
