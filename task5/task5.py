import struct

def hex_to_oct(x):
    is_negative = x.startswith('-')
    if is_negative:
        x = x[1:]
    parts = x.split('.')

    integer = oct(int(parts[0], 16))[2:]
    frac = ''
    if '.' in x:
        fractional = parts[1]
        dec_frac = 0
        for i, digit in enumerate(fractional):
            dec_frac += int(digit, 16) * (16 ** -(i + 1))
        frac = ''
        while dec_frac > 0 and len(frac) < 10:
            dec_frac *= 8
            digit = int(dec_frac)
            frac += str(digit)
            dec_frac -= digit

    return f'{"-" if is_negative else ""}{integer}.{frac}'

point_counter = 0
word_quantity =[]
with open('in.txt','r') as input, open('out.txt','w') as out, open('out1.bin','wb+') as out1:
    word_counter = 0
    for line in input:
        words = line.strip().split()
        for word in words:
            num = ''
            if all(c in '0123456789abcdef.' for c in word.lower()) and word.count('.') <= 1 and word != '.':
                num = hex_to_oct(word)
                words[words.index(word)] = num
            else:
                if word[-1] in '.!?':
                    point_counter += 1
                    word_quantity.append(word_counter + 1)
                    word_counter = 0
                else:
                    word_counter += 1
        out.write(f"{' '.join(words)}\n")
    packed = struct.pack('i',point_counter)
    out1.write(packed)
    for el in word_quantity:
        packed2 = struct.pack('i',el)
        out1.write(packed2)