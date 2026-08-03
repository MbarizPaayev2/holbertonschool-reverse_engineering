# Array of target values extracted from sym.check_flag stack setup (0x00 to 0x3B)
target = [
    0x80, 0xe4, 0x08, 0x18, 0x4a, 0x58, 0xb8, 0xe4,
    0xac, 0x34, 0x58, 0xe4, 0x7e, 0xbc, 0x9e, 0x8c,
    0x7e, 0xd0, 0xc0, 0x7c, 0xac, 0xf4, 0x7e, 0x28,
    0x9e, 0x04, 0x7e, 0xbc, 0x9e, 0x8c, 0x7e, 0x5c,
    0x14, 0x4c, 0x7e, 0x5c, 0x7e, 0x6c, 0x02, 0x14,
    0xb8, 0x4c, 0x14, 0xa4, 0x9e, 0x08, 0x7e, 0xe4,
    0xf4, 0x08, 0x6a, 0x14, 0xa6, 0x5c, 0xb8, 0x7c,
    0x9e, 0x28, 0x3e, 0xac
]

def transform(c, i):
    if i % 2 == 0:
        mult = -46
        xor_val = -368
    else:
        mult = 316
        xor_val = 2528
    return ((c * mult) ^ xor_val) & 0xFF

flag = []
for i in range(len(target)):
    expected = target[i]
    candidates = []
    
    # Check all printable ASCII range (32 to 126)
    for c in range(32, 127):
        if transform(c, i) == expected:
            candidates.append(chr(c))
            
    if len(candidates) == 1:
        flag.append(candidates[0])
    else:
        # Resolve collisions based on constraints: lowercase letters, '_', or prefix/suffix matches
        filtered = [ch for ch in candidates if ch.islower() or ch in ['_', '}', '{', '!']]
        if filtered:
            flag.append(filtered[0])
        else:
            flag.append(candidates[0])

flag_str = "".join(flag)
print("Derived Flag:", flag_str)
