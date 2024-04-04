def calculate_private_key(N, e, p, q):
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return d

# Composantes RSA
N = 22794104685807612632692711511834253069022209021485918263580734875900680973661715591411319293050456124215524147481105023472888409805811982833391808381581920962870039942987390019797162026078690022855511718398727581593076381320187833036675302068752231666458422507888683965080457104149381355490381739024627791805676507165504413121536976999088464269319900987840624582558128370455450780409757358385662379323007508237473471404369309550126759533991252043977925448676206392232229844224687102378877157505061916960244830152443894771754392289501118607494680969059200175838580228508827248184657698662878865403341079766178669137077
e = 238449422852892891538678530003362607565489295513201179758822134480891777
p = 170363316257160371952204264909286661787707905899860786016243676866322554718275558507734733900126992508865021376308009174948289773335994122801767870770018617493657491100117170432835521892451407114239459529930934263778976146834605401895952138503001790022504181633621398059412401986307834714479911754174066057839
q = 133797023834640083063884060416746315461425125510843249427098809491734418797330797149610171090619413791669116545032609088318579650454479007222822827595479608811824868839355103971426890868224553829937975518197010086320222027330670906702446804477093270762963778611702302957224652986597764613918785164654015350043

# Calcul de la clé privée
d = calculate_private_key(N, e, p, q)

# Affichage de la clé privée
print("Clé privée (d) :", d)
