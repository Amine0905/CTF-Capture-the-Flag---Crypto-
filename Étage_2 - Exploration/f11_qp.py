import math
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def extract_rsa_components_from_pem(pem_file):
    with open(pem_file, 'rb') as f:
        pem_data = f.read()

    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    # Extrait N et e de la clé RSA
    n = public_key.public_numbers().n
    e = public_key.public_numbers().e

    return n, e




def find_factors(N, e, d):
    # Calculer l'exposant ed - 1
    exponent = e * d - 1

    # Trouver la plus grande puissance de 2 qui divise (ed - 1)
    s = 0
    while exponent % 2 == 0:
        exponent //= 2
        s += 1

    # Initialiser x
    x = 2

    # Répéter jusqu'à ce qu'un facteur soit trouvé ou que toutes les tentatives soient épuisées
    for _ in range(100):
        # Calculer y1
        y1 = pow(x, exponent, N)

        # Vérifier si y1 est valide (y1 != 1 mod N)
        if y1 != 1:
            # Trouver un facteur commun
            gcd = math.gcd(y1 - 1, N)

            # Si le facteur trouvé est différent de N, retourner les facteurs
            if gcd != 1 and gcd != N:
                return gcd, N // gcd

        # Incrémenter x pour la prochaine itération
        x += 1

    # Si aucun facteur n'est trouvé après un certain nombre d'itérations, retourner None
    return None, None




def main():
    # Valeurs données
    # Utilisation de la fonction pour extraire les composantes de la clé publique
    fichier_pem = "f11_br.pem"
    N, e = extract_rsa_components_from_pem(fichier_pem)

    print("N (modulus) de la clé RSA :", N)
    print("e (exponent) de la clé RSA :", e)    
    
    d = int("15946172446865874328064585521616895951242190491138323236406872170132698003600588473041589962078809188181739816299035022653722697369001675793734938523768730072860636230742207912824449530589766083514195391192382818451273420114835547182537108946912325959863548605926084278436312288647730207304028761547138331578826092884906695089488317248636778642026935164154242620865232042822316444429123057894950626318334300334053851178593937771974836120460430065725618154053101788419914349844281995482345082368036402754976274106449385906663689492200667089054263517119973080150505019667816741203510022717977466781659939568419356256505", 16)

    # Trouver les facteurs de N
    p, q = find_factors(N, e, 15946172446865874328064585521616895951242190491138323236406872170132698003600588473041589962078809188181739816299035022653722697369001675793734938523768730072860636230742207912824449530589766083514195391192382818451273420114835547182537108946912325959863548605926084278436312288647730207304028761547138331578826092884906695089488317248636778642026935164154242620865232042822316444429123057894950626318334300334053851178593937771974836120460430065725618154053101788419914349844281995482345082368036402754976274106449385906663689492200667089054263517119973080150505019667816741203510022717977466781659939568419356256505)

    if p and q:
        print("Facteurs trouvés :")
        print("p =", p)
        print("q =", q)
    else:
        print("Impossible de trouverles facteurs.")

if __name__ == "__main__":
    main()
