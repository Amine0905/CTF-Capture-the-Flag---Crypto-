import json
import base64
import textwrap
from hashlib import sha256
from binascii import unhexlify

class LamportPrivateKey:
    def __init__(self, key_components):
        self.key = key_components
    
    def _prefix(self):
        return "-----BEGIN LAMPORT PRIVATE KEY-----"
    
    def _suffix(self):
        return "-----END LAMPORT PRIVATE KEY-----"
    
    def dumps(self) -> str:
        # Encodes the private key components in base64 and formats them into PEM format
        payload = base64.b64encode(b''.join(self.key)).decode('utf-8')
        middle = '\n'.join(textwrap.wrap(payload, width=64))
        return f"{self._prefix()}\n{middle}\n{self._suffix()}"
    
    def sign(self, message):
        # Signs a message with the Lamport private key
        sig = b''
        h = int.from_bytes(sha256(message).digest(), byteorder='big')
        for i in range(256):
            b = (h >> i) & 1
            sig += self.key[2 * i + b]
        return sig.hex()

def reconstruct_components(messages, signatures):
    """
    Reconstructs the components of the Lamport private key from messages and signatures.
    """
    components = {}
    for message, signature in zip(messages, signatures):
        signature_bytes = unhexlify(signature)
        hash_digest = sha256(message).digest()
        h = int.from_bytes(hash_digest, byteorder='big')
        for i in range(256):
            bit = (h >> i) & 1
            index = 2 * i + bit
            components[index] = signature_bytes[i*32:(i+1)*32]
    return components

def main():
    # Load messages and signatures from the JSON file
    file_path = 'flag18.json'
    messages = []
    signatures = []
    
    with open(file_path, 'r') as file:
        data_array = json.load(file)
        for data in data_array:
            messages.append(data["message"].encode()) 
            signatures.append(data["signature"]) # signatures are already hexadecimal strings
    print("Messages and signatures loaded successfully.")

    # Reconstruct the components of the private key from messages and signatures
    components = reconstruct_components(messages, signatures)

    # Prepare the array of private key elements
    private_key_elements = [b''] * 512
    for index, component in components.items():
        private_key_elements[index] = component

    # Reconstruct the Lamport private key and write it to a PEM file
    lamport_key = LamportPrivateKey(private_key_elements)
    pem_representation = lamport_key.dumps()
    with open('flag18_lamport_private.pem', 'w') as f:
        f.write(pem_representation)
    print("The Lamport private key has been reconstructed successfully and stored in flag18_lamport_private.pem")

    # Sign a message with the Lamport private key and write the signature to a file
    msg = b"coati vigor swims stiff guava"
    signature_result = lamport_key.sign(msg)
    with open('flag18_signature.txt', 'w') as f:
        f.write(signature_result)
    print("The message has been successfully signed and the signature is stored in flag18_signature.txt")

if __name__ == "__main__":
    main()
