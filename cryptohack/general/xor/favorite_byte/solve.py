from pwn import xor

bstr = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

single_bytes = range(1, 256)

for byte in single_bytes:
    try:
        new_str = xor(bstr, byte).decode()
    except UnicodeDecodeError:
        continue
    if new_str[:6] == "crypto":
        print(f"[Byte] Decimal {byte}, Binary {format(byte, 'b')}, Hex {hex(byte)}")
        print(f"[Flag] {new_str}")
