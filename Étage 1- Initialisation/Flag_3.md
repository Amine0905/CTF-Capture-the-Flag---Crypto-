# Flag 3

Utilisation d'OpenSSL pour générer une clé privée et une clé public<br>
`openssl genpkey -algorithm RSA -out f3_private_key.pem` &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#secret key <br>
`openssl rsa -pubout -in private_key.pem -out f3_public_key.pem` &nbsp;#public_key
