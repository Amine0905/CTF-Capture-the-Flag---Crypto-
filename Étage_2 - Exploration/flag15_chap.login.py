import subprocess

def decrypt_message(message_chiffre, mot_de_passe, chiffrement='aes-128-cbc'):
    """
    Déchiffre un message avec une clé symétrique.
    Paramètres :
        - message_chiffre : le message chiffré
        - mot_de_passe : la clé symétrique
        - chiffrement : algorithme de chiffrement (par défaut : aes-128-cbc)
    """
    # Commande pour déchiffrer un message avec une clé symétrique : openssl enc -d -base64 -aes-128-cbc -pbkdf2 -pass pass:<clé>
    arguments = ['openssl', 'enc', '-d', '-base64', '-' + chiffrement, '-pbkdf2', '-pass', 'pass:' + mot_de_passe]

    # Si le message est une chaîne de caractères, le convertir en utf-8
    if isinstance(message_chiffre, str):
        message_chiffre = message_chiffre.encode('utf-8')
        
    # Exécute la commande pour déchiffrer le message
    resultat = subprocess.run(arguments, input=message_chiffre,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Vérifie s'il y a des erreurs
    if resultat.stderr:
        message_erreur = resultat.stderr.decode()
        raise Exception(f"Erreur lors du déchiffrement : {message_erreur}")

    return resultat.stdout.decode()

if __name__ == "__main__":
    # Données du challenge
    message_chiffre = """U2FsdGVkX18bqa4PrfSBqMdKEnLVIHxGq+B3xtyY8YkL34oOvYYOJgC+oetyEjx2\n"""
    mot_de_passe = "16021965*" 

    try:
        message_dechiffre = decrypt_message(message_chiffre, mot_de_passe)
        print(message_dechiffre)
    except Exception as erreur:
        print(erreur)
