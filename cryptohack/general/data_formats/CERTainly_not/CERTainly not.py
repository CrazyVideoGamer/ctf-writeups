from Cryptodome.PublicKey import RSA

with open('2048b-rsa-example-cert.der', 'rb') as f:
    key = RSA.importKey(f.read());
    print(f'Modulus: {key.n}')
