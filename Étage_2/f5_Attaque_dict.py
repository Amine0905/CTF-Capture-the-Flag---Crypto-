import os
import sys


current_directory = os.path.dirname(__file__)
ET1_directory = os.path.join(current_directory, '..', 'ET1')
ET1_directory = os.path.normpath(ET1_directory)
if ET1_directory not in sys.path:
    sys.path.append(ET1_directory)
    
from Decrypt_ import decrypt_sym_key






def find_matching_password(encrypted_text, expected_result):
    """
    Algorithme de recherche de mot de passe
    paramètres: encrypted_text -> texte chiffré
                expected_result -> texte attendu après déchiffrement
    """
    line_count = 0
    try:
        # Ouvre le fichier contenant les mots
        with open("words.txt", "r") as file:
            lines = file.readlines()
            # Parcourt chaque ligne du fichier
            for line in lines:
                line_count += 1
                if line_count % 100 == 0:
                    print(line_count)
                try:
                    # Déchiffre le texte avec le mot actuel sans le caractère de fin de ligne
                    decrypted = decrypt_sym_key(encrypted_text, line.rstrip()) 
                    if decrypted == expected_result:
                        print("Ligne correspondante {}:".format(line_count), line.rstrip())
                        return line.rstrip()
                # Gère les erreurs lors du déchiffrement
                except Exception as e:
                    continue
    # Gère les erreurs lors de l'ouverture du fichier
    except IOError:
        print("Fichier introuvable ou impossible à ouvrir")
    return None

if __name__ == "__main__":
    # Données du challenge
    encrypted_text = "U2FsdGVkX1+1Kc25DMrBi6T2lC8FZONWfwti5miIHv0xb6dDXVIrOHTJemG++5yy\n"
    expected_result = "twain rimer magna waker skiff"
    
    # Cherche le mot de passe correspondant
    find_matching_password(encrypted_text, expected_result)
    
# Résultat seacoast à la ligne 21133
