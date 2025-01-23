d = {}
with open('in.txt','r') as inf :
    with open('out.txt','w') as out:
        with open('out1.txt','w') as out1:
            for line in inf:
                expr = ''
                ans = 0
                line = line.strip().replace('-',' -').replace('+',' +').split(' ')
                if len(line) > 1 :
                    for el in line:
                        expr += el
                        el = int(el)
                        ans += el 
                    expr += '='
                    d[ans] = [expr,0]
                    out.write('{}{}\n'.format(d[ans][0],ans))
                    val = []
                    c = 0
                    for el in line:
                        val.append(int(el))
                    while sum(val) < 0 :
                        val.pop(val.index(min(val)))
                        c += 1
                    d[ans][1] += c
            for el in sorted(d.items(), key=lambda x: x[0]):
                out1.write('{}{} {}\n'.format(el[1][0],el[0],el[1][1]))






