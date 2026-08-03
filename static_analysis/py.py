hex_str = "9E89846A786585866A977D797C8463807C7F6B67848BAB907B698370896B997C797C8D6C6F7E81AE866AB36D7B7F669D7E6A7F96678F9382898263B474"
enc_bytes = bytes.fromhex(hex_str)
key = b"mysecretkey"

plain = []
for i, c in enumerate(enc_bytes):
    k1 = key[i % len(key)]
    k2 = key[(i + 1) % len(key)]
    # Reverse operation: subtract k2, then xor with k1
    p = ((c - k2) & 0xFF) ^ k1
    plain.append(chr(p))

flag = "".join(plain)
print("Decrypted Flag:", flag)
