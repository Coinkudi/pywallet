try:
    from pywallet.crypto import ecdsa_openssl as _ecdsa
except:
    from pywallet.crypto import ecdsa_python as _ecdsa

ECPointAffine = _ecdsa.ECPointAffine
EllipticCurve = _ecdsa.EllipticCurve
secp256k1 = _ecdsa.secp256k1
