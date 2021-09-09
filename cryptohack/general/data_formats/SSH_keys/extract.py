from Cryptodome.PublicKey import RSA

with open('bruce_rsa.pub', 'rb') as f:
    print(RSA.import_key(f.read()).n)
