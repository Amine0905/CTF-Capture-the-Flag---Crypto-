from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from sympy import root
from sympy.ntheory.modular import crt

def load_public_key_from_file(file_path):
    """
    Charge une clé publique RSA depuis un fichier PEM.
    """
    with open(file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key.public_numbers().n, public_key.public_numbers().e

def main():
    # Charger les modules et les exposants des clés publiques
    n_daniel14, e_aniel14 = load_public_key_from_file('flag19_daniel14_pkey.pem')
    n_justin66, e_justin66 = load_public_key_from_file('flag19_justin66_pkey.pem')
    n_tperry, e_tperry = load_public_key_from_file('flag19_tperry_pkey.pem')

    # Messages chiffrés convertis en entiers
    daniel14 = int("62b5c2f3526a38c3b07d047c95ed25c522d70c2406798afcad1cbfd723855514dceb3cebedce10a88b50d1022ccf0d55afeec9543f9640b7cbc450733e3621ade02c52d374905c08e40385cedab92d6e969098654885ee7dd2a985eaf9b7fc8ccd4092ed291dc1fa3179ff44a7aebd32a9252498c57bcefc51b325ddeef52c17bdfbd8d3531bfeda472c66e014b5cbd916787c340f0b4dd6bf2760085a36b87dda1a81c67c457379350f53b32ccc330667285ca0d51152ffc4b15bf05bd18d7eae2da5303385125340140c08af847d2a07e2329ba3b160042f17006b0518abbfaf483466886d9708dd2c28d61facc2695ecce51c4e94fe1c020d337f8350a217", 16)
    justin66 = int("2d44bec07d1231e8f52e247ac6f0b9d17f0624feddc2c67a3f3366c3ba026478f4f7b20427e92c2272c6bfc7dbb3bfb739394d4b4778bd7fb1ec3f9d626d4cf6e252a8f09cf36f820b5cfc9ed6e672be9b2da251614e7d114ff9d0be8a3ca4323d2d0cd7909337fdfdf9de0ac00467516df491961750f72ba7db9c742d44448471d1aad9d048a3363b92477584d006e942fe549663127c9201da6834bed9bf5d3cee0b04f828d3979e5f9f5af3819c94e57a38a493d568ce4cf72b7a5db68ca35e6fc5da245c37adf4c556b2532e72c077c2c5967650c98166e934942dc4a344af1ab517b3447508e62a951775c1e871f41564fb9a731bd169f36b2671c52116", 16)
    tperry = int("300041acdabbd619663186b25bcbfb9c055afa296f4be0acd32d0e431673351ea972ed684e3d4b4a88196b936ee0dba8d712f45ee3a35672cb83d2191285ceffc0324297908d48ac3eb50e376e458bc0f32821d90dcf74ed9b1c8dff9d2a5fd522576e532e3fda691fc24f295db02cde5bc8f19dd05e17b663ae376e482be60ef2ae4894acc34da43ac4cff97113a9a7f0d1dee0a3de2bf928f656f5c61d9db34da1a63f2b7aa4be160ccc5a31b285337e53e1c34cf75fbf249ab9af465b69dfadbacdc1f2c7eb4a60f3f26dc06f0f811db57f3fc0f4d454337e464f6af3632c60c4498a02e943f44714c56b1d98b219f3e3119dc7e2d38fbb75e084f798d279", 16)

    # Utiliser CRT pour trouver M = m^3
    M = crt([n_daniel14, n_justin66, n_tperry], [daniel14, justin66, tperry])[0]

    # Calculer la racine cubique de M
    m = root(M, 3)

    # Conversion du message original en bytes
    message_original = int(m).to_bytes((int(m).bit_length() + 7) // 8, 'big')
    print("Mot de passe déchiffré:", message_original)

if __name__ == "__main__":
    main()
