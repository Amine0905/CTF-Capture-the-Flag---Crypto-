import subprocess

def sign_msg_pkey(msg, skey, signature_path):
    # Commande pour signer un message avec la clé privée : openssl dgst -sha256 -sign <fichier contenant la clé privée> -out <fichier pour la signature> -hex
    args = ['openssl', 'dgst', '-sha256', '-sign', skey, '-out', signature_path, '-hex']

    # Si le message est une chaîne de caractères, le convertir en utf-8
    if isinstance(msg, str):
        msg = msg.encode('utf-8')
    
    # Exécute la commande pour signer le message
    result = subprocess.run(args, input=msg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Vérifie s'il y a des erreurs
    error_message = result.stderr.decode()
    if error_message != '':
        raise Exception(error_message)

# Utilisation de la fonction
challenge = "foots leans comfy admix kayos"         # Message à signer pour activer l'électricité
skey = "f3_private_key.pem"                             # Fichier contenant la clé privée
signature_path_2 = "signature_challenge.txt"         # Fichier contenant la signature

try:
    sign_msg_pkey(challenge, skey, signature_path_2)
    print(f"Signature du message '{challenge}' sauvegardée dans '{signature_path_2}'")
except Exception as e:
    print("Une erreur s'est produite lors de la signature:", e)
