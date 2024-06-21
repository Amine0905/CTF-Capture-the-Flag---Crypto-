from hashlib import sha256

# Identifiant pour l'algorithme de hachage SHA-256 dans EMSA PKCS1
HASH_ID = b'010\r\x06\t`\x86H\x01e\x03\x04\x02\x01\x05\x00\x04 '

def integer_to_octet_string(x: int, k: int) -> bytes:
    """
    Convertit l'entier x en une séquence de k octets
    """
    return x.to_bytes(k, byteorder='big')

def octet_string_to_integer(x: bytes) -> int:
    """
    Convertit la séquence d'octets x en un entier
    """
    return int.from_bytes(x, byteorder='big')

def encode_message_for_rsa_signature(message: bytes, k: int) -> bytes:
    """
    Encode un message en k octets pour une signature RSA
    """
    h = sha256(message)
    T = HASH_ID + h.digest()
    if len(T) + 11 > k:
        raise ValueError("Message trop long")
    PS = bytes([0xff] * (k - len(T) - 3))
    EM = bytes([0x00, 0x01]) + PS + bytes([0x00]) + T
    return EM

def decode_message_from_rsa_signature(signature: bytes, k: int) -> bytes:
    """
    Étant donnée une signature RSA, retourne le hachage
    
    >>> x = encode_message_for_rsa_signature("toto", 128)
    >>> decode_message_from_rsa_signature(x, 128) == sha256("toto".encode()).digest()
    True
    """
    if len(signature) != k:
        raise ValueError("Taille incorrecte")
    if signature[:2] != bytes([0x00, 0x01]):
        raise ValueError("En-tête incorrecte")
    i = 2
    while signature[i] != 0:
        if signature[i] != 0xff:
            raise ValueError("Remplisseur incorrecte")
        i += 1
        if i == k:
            raise ValueError("Seulement du remplisseur")
    if i < 10:
        raise ValueError("Pas assez de remplisseur")
    T = signature[i+1:]
    if T[:len(HASH_ID)] != HASH_ID:
        raise ValueError("Mauvais ID de hachage")
    H = T[len(HASH_ID):]
    return H

def calculate_key_length(n: int) -> int:
    """
    Calcule la longueur de clé en octets
    """
    return (n.bit_length() + 7) // 8

def rsa_pkcs_sign(n: int, d: int, message: bytes):
    """
    Signature RSA utilisant le codage PKCS#1 v1.5
    """
    k = calculate_key_length(n)
    EM = encode_message_for_rsa_signature(message, k)
    m = octet_string_to_integer(EM)
    s = pow(m, d, n)
    S = integer_to_octet_string(s, k)
    return S

def rsa_pkcs_verify(n: int, e: int, message: bytes, signature: bytes) -> bool:
    """
    Vérifie les signatures RSA PKCS#1 v1.5
    """
    k = calculate_key_length(n)
    if len(signature) != k:
        raise ValueError("Mauvaise longueur")
    s = octet_string_to_integer(signature)
    m = pow(s, e, n)
    EM = integer_to_octet_string(m, k)
    H = decode_message_from_rsa_signature(EM, k)
    return (H == sha256(message).digest())


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from Crypto.Util.number import inverse

def load_rsa_public_key_from_file(file_path):
    """
    Charge la clé publique RSA depuis un fichier PEM.
    """
    with open(file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key.public_numbers().n, public_key.public_numbers().e

def simulate_rsa_signature(message_encoded: int, e: int, n: int, x: int):
    """
    Simule une signature RSA en utilisant un masquage.
    """
    message_masquée = (message_encoded * pow(x, e, n)) % n
    return message_masquée


def main():
    # Charge la clé publique RSA
    public_key_path = "flag12_director_pkey.pem"
    n, e = load_rsa_public_key_from_file(public_key_path)

    # Message à signer
    message = b"I, the lab director, hereby grant Amine permission to take the BiblioDrone-NG."
    k = (n.bit_length() + 7) // 8  # Calcule la longueur de la clé en octets

    # Encode le message
    m = encode_message_for_rsa_signature(message, k)
    m_int = octet_string_to_integer(m)  # Convertit le message encodé en entier

    # Masque le message
    x = 2  # Choix arbitraire de x
    message_masquée = (m_int * pow(x, e, n)) % n
    print(f"Message masqué (hex) :\n{hex(message_masquée)}")
    # Le préfixe '0x' devrait être supprimé lors de l'envoi

    # Signature du message masqué reçue de l'ordinateur portable
    signature_reçue = int("b65458446ec9c9fd4392fc8efbe81ae605e014a8438b2fe0a89af62e5b33fad51dfaa1f01ec76e8b7a7594c9674fc98565fd2394378f32393b60391bac0eb3441b672138e9fef5e0aad090748a832101dfbb1876e571c94f26bac6c1863d43c49e4e4499f9a21caaf86843998241ef5cff77e5981bd24c75f18537b2a0c0f7a5abd0187d1c0a6aae5ba00e60d5609570acf57c07a3113d78db3df6b3c18d5cb8b9fbc615e0ce022a578e3857bd2e1ae0e0c1d5fae4613c139d6c0ee1aa3c2c657d805f622bd9785ce9c083f0d56708c6fc719ae19f03a34948f14354621d8dd0275b1f67147c3f57582d4842bd2b39d585ea88c64948a103ca424c986dbb65b3", 16)

    # Démascage de la signature
    tmp = (signature_reçue) * (inverse(x, n)) % n
    signature_originale = hex(tmp)
    print(f"Signature originale (hex) :\n{signature_originale}")
    # Le préfixe '0x' devrait être supprimé lors de l'envoi

if __name__ == "__main__":
    main()