from OpenSSL import crypto


def createKeyPair():
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)
    return pkey

def createCertRequest(pkey, jsonArg):
    req = crypto.X509Req()
    req.get_subject().C              = jsonArg['C'] #"PL"
    req.get_subject().ST             = jsonArg['ST'] #"Western Pomerania District"
    req.get_subject().L              = jsonArg['L'] #"Szczecin"
    req.get_subject().O              = jsonArg['O'] #"Westernpomeranian University of Technology"
    req.get_subject().OU             = jsonArg['OU'] #"ZUT"
    req.get_subject().CN             = jsonArg['CN'] #"WI"
    req.get_subject().emailAddress   = jsonArg['emailAddress'] #"adres@email.com";
    req.set_pubkey(pkey)
    req.sign(pkey, 'sha1')
    return req

def createCertificate(req, issuercert, issuerkey, serial):
    cert = crypto.X509()
    cert.set_serial_number(serial)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(60*60*24*365*5) # 5 years
    cert.set_issuer(issuercert.get_subject())
    cert.set_subject(req.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(issuerkey, 'sha1')
    return cert

def runCertificataion(jsonArg):
    userKeyObj = createKeyPair()
    certReq = createCertRequest(userKeyObj, jsonArg)
    cacert=pem.parse_file("cert.pem")[0]
    newUserCertificate = createCertificate(certReq, cacert, cakey, serial)
    return None
