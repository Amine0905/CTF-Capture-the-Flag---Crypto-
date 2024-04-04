import sys
import os
import subprocess

def sign_msg_skey(msg, skey, signature_path):
  
    
    # Si le message est une chaîne de caractères, le convertir en bytes
    if isinstance(msg, str):
        msg = msg.encode('utf-8')
        
    # Exécute la commande pour signer le message
    args = ['openssl', 'dgst', '-sha256', '-sign', skey, '-out', signature_path]
    result = subprocess.run(args, input=msg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Vérifie s'il y a des erreurs
    error_message = result.stderr.decode()
    if error_message != '':
        raise Exception(error_message)


def display_signature_hex(signature_path):
    
    try:
        with open(signature_path, 'rb') as signature_file:
            signature_content = signature_file.read()
            print(f"Contenu de la signature en hexadécimal: \n{signature_content.hex()}\n")
    except Exception as e:
        print(f"Erreur lors de la lecture de la signature: {e}")

if __name__ == "__main__":
    # Messages à signer et à vérifier, et chemins des fichiers
    
    
    challenge_path = "ch.txt"
    
    try:
        with open(challenge_path, 'rb') as file:
            challenge = file.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du message dans '{challenge_path}': {e}")
        sys.exit(1)
    
    skey_path = "flag9_skey.pem"
    signature_path = "flag9_signature_challenge.bin"

    # Signature et vérification du message 'challenge'
    try:
        sign_msg_skey(challenge, skey_path, signature_path)
        print(f"Signature du message '{challenge}' sauvegardée dans '{signature_path}'")
        # Afficher la signature en hexadécimal
        display_signature_hex(signature_path)
    except Exception as e:
        print("Une erreur s'est produite lors de la signature ou de la vérification de 'challenge':", e)