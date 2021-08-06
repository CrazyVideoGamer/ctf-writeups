from pwn import xor

bstr = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
original_known = b"crypto{"
start_of_key = []
for chars in zip(original_known, bstr): #note: chars contains numbers, not letters
    start_of_key.append(xor(chars[0], chars[1]))

#print("".join([char.decode() for char in start_of_key])) # gives "myXORke", key may be "myXORkey"

key = start_of_key + [b"y"]
print("[Key]", "".join([char.decode() for char in key]))
key = b"".join(key)

print("[Flag]", xor(bstr, key).decode())
