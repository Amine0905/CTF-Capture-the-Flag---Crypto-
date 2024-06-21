import binascii

def custom_md5_padding(message):
    """
    Ajoute un padding personnalisé à un message MD5.
    """
    # Convertir le message en bytes
    if isinstance(message, str):
        message = message.encode('ascii')

    # Longueur originale du message en bits
    original_bit_len = len(message) * 8

    # Ajouter le bit '1' à la fin du message
    message += b'\x80'

    # Ajouter des bits '0' (sous forme de bytes '\x00') jusqu'à atteindre une longueur multiple de 64 octets - 8 octets pour la longueur
    while (len(message) + 8) % 64 != 0:
        message += b'\x00'

    # Ajouter la longueur du message original sous forme de 64 bits (big-endian pour l'exemple)
    message += original_bit_len.to_bytes(8, 'big')

    # Convertir le message paddé en une représentation hexadécimale
    hex_representation = message.hex()

    # Remplacer '00' par 'f' pour simuler votre exemple (sauf pour les 8 derniers octets représentant la longueur)
    hex_representation = hex_representation[:-16] + \
        hex_representation[-16:].replace('00', 'f')

    return hex_representation

def write_prefix_file(message, file_path):
    """
    Écrit le message dans le fichier spécifié avec un padding MD5 personnalisé.
    """
    padded_hex = custom_md5_padding(message)
    with open(file_path, 'w') as f:
        f.write(message + padded_hex[len(message)*2:])

def binary_to_hex(file_path):
    """
    Lit les données binaires d'un fichier et les convertit en hexadécimal.
    """
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    return binascii.hexlify(binary_data)

def read_file(file_path):
    with open(file_path, 'r') as f:
        prefixe = f.read()
    return prefixe

def construct_keys(prefixe, suffix, key1, key2, key3, key4):
    """
    Construit des clés en concaténant le préfixe, les parties de la clé et le suffixe.
    """
    # Convertit les données hexadécimales en chaînes de caractères
    key1 = key1.decode('utf-8')
    key2 = key2.decode('utf-8')
    key3 = key3.decode('utf-8')
    key4 = key4.decode('utf-8')

    # Affiche les clés construites
    print(prefixe + key1 + key3 + suffix)
    print(prefixe + key1 + key4 + suffix)
    print(prefixe + key2 + key3 + suffix)
    print(prefixe + key2 + key4 + suffix)

def main():
    """
    Fonction principale.
    """
    # Écriture du préfixe dans le fichier
    prefix_message = "Amine"
    prefix_file_path = 'prefixe'
    write_prefix_file(prefix_message, prefix_file_path)

    # Construction du suffixe
    suffix = "h4ckm0d3"
    suffix_hex = suffix.encode('utf-8').hex()

    # Lecture des clés depuis les fichiers binaires
    key1 = binary_to_hex('key1')
    key2 = binary_to_hex('key2')
    key3 = binary_to_hex('key3')
    key4 = binary_to_hex('key4')

    # Construction et affichage des clés
    prefixe = read_file(prefix_file_path).encode('utf-8').hex()
    construct_keys(prefixe, suffix_hex, key1, key2, key3, key4)

if __name__ == "__main__":
    main()
