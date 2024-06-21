import json
import binascii
from cryptography.hazmat.primitives.asymmetric import padding, ec
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import load_pem_x509_certificate
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import ExtensionOID  # Ajout de l'importation de ExtensionOID

def charger_transactions(chemin_fichier):
    with open(chemin_fichier, 'r') as f:
        donnees = json.load(f)
    return donnees['ensemble']['transactions']

def verifier_transaction(transaction_unique):
    try:
        # Charger les certificats
        cert_carte = load_pem_x509_certificate(transaction_unique['carte']['certificat'].encode(), default_backend())
        cert_banque = load_pem_x509_certificate(transaction_unique['carte']['banque']['certificat'].encode(), default_backend())

        # Vérifier la signature de la carte
        cert_carte.public_key().verify(
            binascii.unhexlify(transaction_unique['signature']),
            transaction_unique['donnees'].encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )

        # Vérifier l'extension "Basic Constraints" pour le certificat de la banque
        if not cert_banque.extensions.get_extension_for_oid(ExtensionOID.BASIC_CONSTRAINTS).value.ca:
            raise Exception("Le certificat de la banque n'a pas le 'bit CA' qui l'autorise à signer d'autres certificats.")

        # Charger le certificat CA
        with open("flag13_ca.pem", "rb") as f:
            cert_ca = load_pem_x509_certificate(f.read(), default_backend())

        # Vérifier la chaîne de certificats
        cert_ca.public_key().verify(
            cert_banque.signature,
            cert_banque.tbs_certificate_bytes,
            padding.PKCS1v15(),
            cert_banque.signature_hash_algorithm,
        )

        cert_banque.public_key().verify(
            cert_carte.signature,
            cert_carte.tbs_certificate_bytes
        )

        # Vérifier les données contenues dans la transaction
        if transaction_unique['carte']['numero'] not in transaction_unique['donnees'] or transaction_unique['carte']['banque']['nom'] not in transaction_unique['donnees']:
            raise Exception("Les données de la transaction ne correspondent pas aux informations de la carte ou de la banque.")

        # Si toutes les vérifications précédentes ont réussi pour cette transaction, retourner 1
        return 1

    except Exception as e:
        print(f"ERREUR : la transaction avec la carte {transaction_unique['carte']['numero']} est invalide")
        print(f"Raison : {e}")
        return 0

def main():
    transactions = charger_transactions('flag13_transaction.json')
    resultats = [verifier_transaction(tx) for tx in transactions]
    print("\nRésultats des vérifications des transactions :\n", resultats)

if __name__ == "__main__":
    main()
