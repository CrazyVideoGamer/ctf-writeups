from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()

    if "error" in received:
        print("Received error. Aborting")
        break

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    to_send = {}

    import base64
    from Cryptodome.Util.number import long_to_bytes

    if received["type"] == "base64":
        to_send["decoded"] = base64.b64decode(received["encoded"].encode()).decode()
    elif received["type"] == "hex":
        to_send["decoded"] = bytes.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        rot13_decode = str.maketrans(
                  'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm',
                  'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz'
                )
        to_send["decoded"] = received["encoded"].translate(rot13_decode)
    elif received["type"] == "bigint":
        to_send["decoded"] = long_to_bytes(int(received["encoded"], 16)).decode()
    elif received["type"] == "utf-8":
        decoded = [chr(char) for char in received["encoded"]]
        to_send["decoded"] = "".join(decoded)

    json_send(to_send)

print(json_recv())
