import struct

base = 2
exponent = 0xFFFFFFFFFFFF
modulus = 0xFFFFFFFFFFFFFFB

# 1. Fast modular exponentiation in O(log e) time
key = pow(base, exponent, modulus)

# 2. Extracted qword array from radare2 output
encrypted_flag = [
    0x6f836cb672d9828e,
    0x699a77a760da96a8,
    0x779872a077db84bc,
    0x6184778c75d182a5,
    0x5f9070ba69da83a8,
    0x61a86dba4fc198a4,
    0x00f763a763c08099
]

# 3. Decrypt bytes via XOR and unpack
flag_bytes = bytearray()
for qword in encrypted_flag:
    dec = qword ^ key
    raw = struct.pack("<Q", dec)
    for b in raw:
        if b != 0:
            flag_bytes.append(b)

print("Decrypted flag:", flag_bytes.decode('ascii'))
