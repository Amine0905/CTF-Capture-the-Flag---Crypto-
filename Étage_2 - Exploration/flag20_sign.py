import subprocess

class OpensslError(Exception):
    pass

def get_signature(message, private_key):
    """Génère la signature d'un message avec la clé privée."""
    
    args = ['openssl', 'dgst', '-sha256', '-sign', private_key, '-out', 'flag14_signature.bin']

    if isinstance(message, str):
        message = message.encode('utf-8')

    result = subprocess.run(args, input=message, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Vérification des erreurs
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)
    
def get_signature_of_public_key(public_key, private_key):
    """Génère la signature de la clé publique avec une clé privée."""
    
    args = ['openssl', 'dgst', '-sha256', '-sign', private_key, '-out', 'flag14_signature.bin', public_key]
    subprocess.run(args)

def verify_signature(message, public_key):
    """Vérifie la signature d'un message avec une clé publique."""
    
    args = ['openssl', 'dgst', '-sha256', '-verify', public_key, '-signature', 'flag14_signature.bin', message]
    subprocess.run(args)

def create_hex(file):
    """Génère un fichier hexadécimal sans sauts de ligne."""
    
    with open(file, 'rb') as infile, open('flag14_signature.hex', 'w') as outfile:
        hex_data = infile.read().hex()
        outfile.write(hex_data)

def create_csr(private_key, csr):
    """Génère un fichier CSR (Certificate Signing Request)."""
    
    args = ['openssl', 'req', '-new', '-key', private_key, '-out', csr, '-subj', '/CN=rania']
    subprocess.run(args)


pkey = "flag99_pkey.pem"
get_signature_of_public_key(pkey, "flag9_skey.pem")

create_hex("flag14_signature.bin")

