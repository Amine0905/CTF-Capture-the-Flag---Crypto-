def normalize_mod(a, n):
    """ Normalise a pour qu'il soit compris entre -n/2 et n/2. """
    a = a % n
    if 2 * a > n:
        a -= n
    return a


def modular_exponentiation(a, r, n):
    """ Réalise l'exponentiation modulaire avec normalisation. """
    result = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            result = normalize_mod(result * a, n)
        r //= 2
        a = normalize_mod(a * a, n)
    return result


def calculate_quotient(a, n):
    """ Calcule le quotient de la division de a par n, ajusté par normalisation. """
    return (a - normalize_mod(a, n)) // n


def gaussian_remainder(w, z):
    """ Calcule le reste dans les entiers gaussiens lors de la division de w par z. """
    (w0, w1) = w
    (z0, z1) = z
    n = z0**2 + z1**2
    if n == 0:
        raise ValueError("Division par zéro")
    u0 = calculate_quotient(w0 * z0 + w1 * z1, n)
    u1 = calculate_quotient(w1 * z0 - w0 * z1, n)
    return (w0 - z0 * u0 + z1 * u1, w1 - z0 * u1 - z1 * u0)


def gaussian_gcd(w, z):
    """ Calcule le plus grand diviseur commun utilisant les entiers gaussiens. """
    while z != (0, 0):
        w, z = z, gaussian_remainder(w, z)
    return w


def calculate_fourth_root(p):
    """ Calcule la racine 4ème de 1 modulo p."""
    if p <= 1:
        return "trop petit"
    if (p % 4) != 1:
        return "pas congruent à 1"
    k = p // 4
    j = 2
    while True:
        a = modular_exponentiation(j, k, p)
        b = normalize_mod(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "pas premier"
        j += 1


def decompose_prime_into_squares(p):
    """ Décompose un nombre premier p en une somme de deux carrés. """
    a = calculate_fourth_root(p)
    return gaussian_gcd((p, 0), (a, 1))


def main():
    p_hex = "de55a2f28843cddf70385afcf59586728b18d09fe2c64547d4a536bbd4ecadafbc4fba1bab638adac4407c031e943e2577afc464f03e09e48a6f12d1953f3b20586597420ff3af84a00ea1d4a4e5a1277a225e2fe1e18426d0e99be8ca3f88caaf0d8bd4cccc2cabbfa4db4209924cbfc12e5e4c5ea393517c56674c0d3df981"
    p_int = int(p_hex, 16)
    a, b = decompose_prime_into_squares(p_int)
    print(f"a = \n{a} \nb = \n{b}\n")


if __name__ == "__main__":
    main()
