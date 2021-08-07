from Cryptodome.PublicKey import RSA

rsa_key = RSA.importKey(open("privacy_enhanced_mail.pem", "rb").read())

print(rsa_key)
print(rsa_key.d)
