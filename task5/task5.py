import struct
def infr(x):
    int_part = ''
    frac_part = ''
    fl = False
    for i in x:
        if i == '.':
            fl = True 
            continue
        if not(fl):
            int_part += i
        if fl :
            frac_part += i
    return int_part , frac_part
    
def convert_to_oct(x,func):
    int_part,frac_part = func(x)
    x = 0
    for i in range(1,len(frac_part)+1):
        x += (int(frac_part[i-1],16))*16**(-i)
    x = str(x)[1:]
    x = str(int(int_part,16)) + x

    int_part,frac_part = func(x)
    x = '.'
    frac_part = float('0.'+frac_part)
    while True :
        frac_part = frac_part * 8
        if frac_part == int(frac_part):
            x += str(int(frac_part))
            break
        else:
            x += str(frac_part)[:1]
            frac_part = frac_part - int(str(frac_part)[:1])    
    x = oct(int(int_part))[2:] + x

    return x

point_counter = 0
word_quantity =[]
with open('in.txt','r') as inf:
    with open('out.txt','w') as out:
        word_counter = 0
        for line in inf :
            line = line.strip().split(" ")
            
            for el in line :
                num = ''
                try:
                    num = convert_to_oct(el,infr)
                    line[line.index(el)] = num
                except Exception:
                    if el == '.' :
                        point_counter += 1
                        word_quantity.append(word_counter)
                        word_counter = 0
                    else :
                        word_counter += 1
            for i in range(len(line)) :
                if i == len(line)-1:
                    out.write('{}\n'.format(line[i]))
                else:
                    out.write('{} '.format(line[i]))
with open('out1.bin','wb+') as out1:
    packed1 = struct.pack('i',point_counter)
    out1.write(packed1)
    for el in word_quantity:
        packed2 = struct.pack('i',el)
        out1.write(packed2)
    
    # out1.seek(0)
    # p = struct.unpack("i", out1.read(4))
    # print(p[0])
    # results = []
    # for _ in range(len(word_quantity)):
    #     value = struct.unpack("i", out1.read(4))[0]
    #     results.append(value)

    # print(f"word_quantity: {results}")



                


                


            



    


    