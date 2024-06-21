# 17 flags obtenus
flags_mac = [
	"c8729bff6c8d6ee0188400e8d62fa1f7cd3d774adcc809b3e90e4a0530a6ef47",
	"3b049829dc33ee08f38a3da252ee193bce96e330dd644a0d7f1e10562cd87c59",
	"1661d02a07a133a39e172696649768a8ac5f480deeaac9c76acef66c2ec8d0c5",
	"25483b2f1bf15d595da015233dbffb008620ce6b42d076dd59ecc75798fce788",
	"7a3be946e705eea794054c5dc325ba7bc18c63a08fdc214989db320ae9d306c5",
	"32df654480d043b1dcb3f26bbb8967887b802bb049ed59d0bdc8ce042d986719",
	"0258cc92c6f1fc2828b1b348c02e5a63e50acb0315d5bc9af22dca88dc34e697",
	"88226aacf42773c4527938fe69b249594a7e7f9a8bcab7320470944c25709ae3",
	"547bc5c4c115791987376af1d2b9a1ac591daa9e06776d3f8d32813a0173e735",
    "2abf33f888a42b1afa6fe4ddca0045347dd083eeef40307a946be5031c8920d4",
    "7a65b49053ad2d5e8611aaf9f61ba579a2a252d928e65e1091c224016864a3bf",
    "45a5641d8dddc04b76aba182a43964f4f73f8b55c28238995461c6dff70560a5",
    "2f4f785e57be56f484facb2caac388aaf0fe6e90f68c44922e516cefceb3bc5c",
    "84d72be8a563821fa3fc31635518c849989b5aeb037485d329c9b4169456996b",
    "a10f3371f2f2dda568c4a5b9130b6df01f1eca9ad30573ef535132dced2d7747",
    "3e178ea137321efa7a263895cc9d9aee5fb4aeabc3d1e8c3d9af53743580ca6f",
    "e298a7310c008833310a6ce94ccb1cec9cc04415d2c64963fa3921ed28bc129e"
]



def hex_vers_binaire(hex_string):
    """
    Convertit une chaîne hexadécimale en une chaîne binaire.
    """
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def extraire_X_A_B_C_de_MAC(mac):
    """
    Extrait les valeurs X, A, B et C à partir d'un MAC donné.
    """
    mac_binaire = hex_vers_binaire(mac)
    X = int(mac_binaire[0:64], 2)
    A = int(mac_binaire[64:128], 2)
    B = int(mac_binaire[128:192], 2)
    C = int(mac_binaire[192:256], 2)
    return X, A, B, C

# Listes pour stocker les valeurs X, A, B et C extraites
liste_X = []
liste_A = []
liste_B = []
liste_C = []

# Boucle sur les MAC pour extraire X, A, B et C
for mac in flags_mac:
    X, A, B, C = extraire_X_A_B_C_de_MAC(mac)
    liste_X.append(X)
    liste_A.append(A)
    liste_B.append(B)
    liste_C.append(C)

# Affiche les listes X, A, B et C
print("X =", liste_X)
print("A =", liste_A)
print("B =", liste_B)
print("C =", liste_C)
