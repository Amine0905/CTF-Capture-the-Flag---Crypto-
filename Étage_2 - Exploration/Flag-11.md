# Flag 11
- On trouve un Bureau RC-07 (équipe DEV): `kristi82` et `browndavid` ( leurs clés génrées avec le meme N )
- On a le `d` de `kristi82` :
 
    - username: `kristi82`
    - `d` : 32e61b784d0c7269a55f8b3a991ce8854eb7e6639741720cba7f9ad0b79b0e18ca646073918078ff8811eecd0fa6339666fbd22c2ac3db306651bd1f3c0791d1d801afef4024f559f7bcac4f61bd862425b2a058acac1452e7bf9deb7f50b93cd866bf901f5932e2cb1d9504b96534e8438a8b27167cc705112a9dc6ae6d07577df502c9b0e7780db9104d6515b71ad39f5100193445483a7bb18f5ddf2a872ce44d25257bf014a0558bd4b8f9168d5012fefe676a7ab48be26aa084b5e92b1e4d226558e52df40e6af9066fd6ca4d181998357d92e2d630a87f629856b578afa5f0c53a2571181a9a3a7b96fa9ad99eb4508826f13c02f83dda744dd8db7f31

- On fait l'extraction de `N` et `e` de la clé public de l'un des deux `kristi82` ou `browndavid` puis une factorisation avec `f11_qp.py` pour trouver les deux facteur de `N = p x q` et on a le `d` bingo on peut calculer le `d` de `browndavid` avec `calcd.py`
- On génère la clé privée avec `f11_gen_key.py`
- On signe avec le programme f9_sign en remplaçant le nécessaire ( clé privée, le contenu du fichier ch.txt)
