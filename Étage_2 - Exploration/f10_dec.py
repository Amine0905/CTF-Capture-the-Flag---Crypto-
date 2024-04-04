from Crypto.PublicKey import RSA
import sympy

def decrypt_shared_message(public_key_file1, public_key_file2, ciphertext_hex1, ciphertext_hex2):

    # Chargement des clés publiques
    with open(public_key_file1, 'r') as f:
        pkey1 = RSA.import_key(f.read())

    with open(public_key_file2, 'r') as f:
        pkey2 = RSA.import_key(f.read())

    # Extraire e et N de chaque clé
    e1, N1 = pkey1.e, pkey1.n
    e2, N2 = pkey2.e, pkey2.n

    # Vérification que N est le même pour les deux clés
    assert N1 == N2, "Les modules des deux clés publiques ne sont pas égaux"

    # Conversion des ciphertexts en entiers
    c1_int = int(ciphertext_hex1, 16)
    c2_int = int(ciphertext_hex2, 16)

    # Calcul de u et v à l'aide de l'extension de l'algorithme d'Euclide
    u, v = sympy.gcdex(e1, e2)[0:2]
    u, v = int(u), int(v)

    # Calcul du message m
    N = N1  # Identique à N2
    m = (pow(c1_int, u, N) * pow(c2_int, v, N)) % N

    # Conversion du message en bytes puis en texte
    m_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    print(f"Message déchiffré (bytes) : {m_bytes}")

if __name__ == "__main__":
    public_key_file1 = 'f10_westsuzanne.pem'
    public_key_file2 = 'f10_tiffany72.pem'
    ciphertext_hex_westsuzanne = "c48865569f1c65c50d69cff32bb0bc241b7c4c8f1b0c40154033e78e1ece59ed501da1ab499e4d0617f8e6df079d19a4cb1069d925097242f1f67216da9ded9b0efc50386a292f060d7d681be63d78d6b3e6db704ff4f86e6bd52f1afb68184e70a0cbd2c211e85376a48bc53a97a0f46c81acb523aa07b055df60ae4cf99c5762887ad9590d71ce11b08517d10e9f0945eb89035eaa7159b97f2ac502676763aa0cb7e3c5c5c93fbeb5b9f3bb034d530af1d26e8452e765a52e9da231565825a52ae0dc58e892516268957a80ef1bdcade907562f1f26ff955957382ad6492d12b163fcb9aa49031aaaf288f871b7d6dde3143f036121a3ef004ce9c231e262"
    ciphertext_hex_tiffany72 = "75a1381d518174f0d9838d9a23cccfa9527dc8a0bb4028775679e72fc915aad15550dc7527622c13651dde63895f6722b089b3b58081f6a104ad884390bb6d0a9f3fadd188c340e155e3fec77294822ddb56e6e2775b554155564e7daba17aa42b0e34772606746edab2ece240524968c7da1c8aa51b3f272ca3148b485e9629d3fdeb2b69466ab612359e504fc8f6cf2dd55802d91f12a5e1b8764f8046edc4216697687714dcea288a9031b309708aa8e25283bed3e9320766d55a04da6930e66219702668fcff3dcf2e4124df899eea9175e4be3ee49cd1634c90dd386cdc14ad147a86253c2609e0a433b6f00a50a75f60df4afdee4f9ea9cd0e46d62d9e"

    decrypted_message = decrypt_shared_message(public_key_file1, public_key_file2, ciphertext_hex_westsuzanne, ciphertext_hex_tiffany72)

if decrypted_message is not None:
    decoded_message = decrypted_message.decode('utf-8')
    print("Message déchiffré : ", decoded_message)
else:
    print("Erreur: Impossible de déchiffrer le message.")

