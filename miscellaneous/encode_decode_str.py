def encode_decode(strs):
    decoded, sizes = encode(strs)
    return decode(decoded, sizes)

def encode(strs):
    sizes = []
    encode = ''
    for string in strs:
        sizes.append(len(string))
        encode += string
    print(encode)
    return encode, sizes

def decode(s, sizes):
    decode = []
    start = 0
    end = 0
    for size in sizes:
        end = start + size
        string = s[start:end]
        decode.append(string)
        start = end
    print(decode)
    return decode

encode_decode(["hello","world","come","on","lets","work","out", "1234589*&¨$%", ")(*TYGVB"])
