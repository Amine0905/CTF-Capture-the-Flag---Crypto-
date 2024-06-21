import subprocess

def signer_message(message, cle_privee, chemin_signature):
   
    # Si le message est une chaîne de caractères, le convertir en bytes
    if isinstance(message, str):
        message = message.encode('utf-8')
        
    # Exécute la commande pour signer le message
    arguments = ['openssl', 'dgst', '-sha256', '-sign', cle_privee, '-out', chemin_signature]
    resultat = subprocess.run(arguments, input=message, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Vérifie s'il y a des erreurs
    message_erreur = resultat.stderr.decode()
    if message_erreur != '':
        raise Exception(message_erreur)


def afficher_signature_hexadecimal(chemin_signature):
   
    try:
        with open(chemin_signature, 'rb') as fichier_signature:
            contenu_signature = fichier_signature.read()
            print(f"Contenu de la signature en hexadécimal :\n{contenu_signature.hex()}\n")
    except Exception as erreur:
        print(f"Erreur lors de la lecture de la signature : {erreur}")

if __name__ == "__main__":
    # Signature et vérification du message 'challenge'
    challenge = "busks bores downy jings rehab"
    chemin_cle_privee = "flag9_skey.pem"
    chemin_signature = "flag16_signature_challenge.bin"
    try:
        signer_message(challenge, chemin_cle_privee, chemin_signature)
        print(f"Signature du message '{challenge}' enregistrée dans '{chemin_signature}'")
        # Afficher la signature en hexadécimal
        afficher_signature_hexadecimal(chemin_signature)
    except Exception as erreur:
        print("Une erreur s'est produite lors de la signature ou de la vérification du 'challenge' :", erreur)
