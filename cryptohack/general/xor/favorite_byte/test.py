#bstr = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
bstr1 = b'crypto{temp}'
bstr2 = b'crypto{'
bstr3 = b'}'

def encrypt(bstr):
    bstr_list = [ord(char) for char in bstr.decode()]

    byte = int("100000000", 2)

    new_list = []
    for num in bstr_list:
        new_list.append(num ^ byte) # encrypt char
    new_str = "".join([chr(num) for num in new_list])
    return new_str

str1 = encrypt(bstr1)
str2 = encrypt(bstr2)
str3 = encrypt(bstr3)

print(f"{str1} {str2} {str3}")

print(f"{str1.startswith(str2)} {str1.endswith(str3)} {str1.startswith(str2) and str1.endswith(str3)}")
