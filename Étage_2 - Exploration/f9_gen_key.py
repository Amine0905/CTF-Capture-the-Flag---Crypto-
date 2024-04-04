from Crypto.PublicKey import RSA
import base64

def generate_rsa_keys(base64_string, public_key_file, private_key_file):
   
    # Décodage de e en base64
    decoded_bytes = base64.b64decode(base64_string)
    print("e (en bytes) : ", decoded_bytes)

    # Conversion en valeur décimale
    decimal_value = int.from_bytes(decoded_bytes, byteorder='big')
    print("e (en décimal) : ", decimal_value)

    # Génération de la paire de clés RSA avec e comme exposant public
    key = RSA.generate(bits=2048, randfunc=None, e=decimal_value)

    # Sauvegarde des clés dans des fichiers  
    with open(private_key_file, 'wb') as f:
        f.write(key.export_key('PEM'))
    with open(public_key_file, 'wb') as f:
        f.write(key.publickey().export_key('PEM'))

# Utilisation de la fonction
if __name__ == "__main__":
    base64_string = "ee+++ATRIUM+++ed"
    public_key_file = "flag9_pkey.pem"
    private_key_file = "flag9_skey.pem"

    generate_rsa_keys(base64_string, public_key_file, private_key_file)