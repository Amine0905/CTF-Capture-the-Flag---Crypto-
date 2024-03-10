# Flag 3

Utilisation d'OpenSSL pour générer une clé privée et une clé public  
openssl genpkey -algorithm RSA -out f3_private_key.pem    #secret key 
openssl rsa -pubout -in private_key.pem -out f3_public_key.pem   #public_key
