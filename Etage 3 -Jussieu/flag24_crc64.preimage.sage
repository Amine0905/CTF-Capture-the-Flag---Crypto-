# Définition de l'environnement et des variables
polynomial_q = x^64 + x^4 + x^3 + x + 1  # Polynôme irréductible pour GF(2^64)
finite_field = GF(2)['x']  
q_polynomial = finite_field(polynomial_q)   # Convertir q en polynôme dans F

# Conversion de la valeur hexadécimale en séquence de bits
hashpwd_hex = "dd0ea82a66cf801e"
hashpwd_int = int.from_bytes(bytes.fromhex(hashpwd_hex), byteorder='big')
hashpwd_bin = bin(hashpwd_int)[2:].zfill(64)  # Binaire avec remplissage pour 64 bits

# Création du polynôme S(x) à partir de la séquence binaire
s_x = " + ".join([f"x^{i}" for i, bit in enumerate(reversed(hashpwd_bin)) if bit == '1'])
s_polynomial = finite_field(s_x)

# Calcul de l'inverse de (x^4 + x^3 + x + 1) modulo Q(x)
polynomial_to_inverse = finite_field(x^4 + x^3 + x + 1)
inverse_polynomial = polynomial_to_inverse.inverse_mod(q_polynomial)

# Calcul de P(x) comme l'inverse de Q multiplié par S
result_polynomial = inverse_polynomial * s_polynomial

# Conversion de P(x) en chaîne binaire et ensuite en hexadécimal
coef_list = [int(coef) for coef in result_polynomial.list()]
binary_str = ''.join(str(bit) for bit in coef_list[::-1])
int_value = int(binary_str, 2)
hex_value = hex(int_value)[2:].zfill(16)  # Assurez-vous que la chaîne hexadécimale a 16 caractères

# Afficher le résultat final
print("USER : MKT01")
print(f"Valeur Hexadécimale Résultante: {hex_value}")
