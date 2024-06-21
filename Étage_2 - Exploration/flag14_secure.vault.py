import hashlib
import binascii
import subprocess

def generer_cle(seed: bytes) -> bytes:
    """
    Génère une clé de 256 bits pseudo-aléatoires à partir de la graine.
    """
    etat = seed
    sortie = b''
    for i in range(8):
        etat = hashlib.sha256(etat).digest()
        sortie += etat[:4]
    return sortie

def trouver_cle(ivv):
    """
    Trouve la clé pour un vecteur d'initialisation donné.
    """
    for a in range(256):
        for b in range(256):
            materiau_cle = generer_cle(bytes([a, b]))
            K = materiau_cle[0:16]
            IV = materiau_cle[16:32]
            IVVV = binascii.hexlify(IV).decode()
            if IVVV == ivv:
                print("Clé trouvée :", binascii.hexlify(K).decode())
                return binascii.hexlify(K).decode(), IVVV
    return None, None

def dechiffrer(cle, iv, donnees_chiffrees):
    """
    Déchiffre un fichier chiffré avec la clé et le vecteur d'initialisation fournis.
    """
    args = [
        'openssl', 'enc', '-d', '-aes-128-cbc', '-K', cle, '-base64',
        '-iv', iv, '-in', donnees_chiffrees, '-out', 'flag15_decrypted.txt'
    ]
    subprocess.run(args, check=True)

def main():
    ivv = "689aada2cd131312d5da00e69f9b6d15"
    chiffre = "flag14_encrypted.txt"
    cle, iv = trouver_cle(ivv)

    if cle and iv:
        dechiffrer(cle, iv, chiffre)
    else:
        print("Impossible de trouver la clé.")

if __name__ == '__main__':
    main()
