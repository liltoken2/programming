tag_dict = {}
depth = 0
with open('in.txt','r') as f :
    for line in f:
        line = line.strip().replace('"','').replace('{',' {').replace(':',': ').replace('}',' } ').replace(',',' , ').split(' ')
        for tag in line:
            if tag == '}':
                depth -= 1

            elif tag != '' and tag[-1] == ':':
                if tag[0] == '{':
                    depth += 1
                    tag = tag[1:-1]
                elif tag[0] != '{':
                    tag = tag[:-1]
                
                if tag not in tag_dict:
                    tag_dict[tag] = [0,0]          
                tag_dict[tag][0] += 1
                
                tag_dict[tag][1] = max(depth ,tag_dict[tag][1])
with open('out.txt','w') as out:
    for tag in tag_dict :
        out.write('{} {} {}\n'.format(tag,tag_dict[tag][0],tag_dict[tag][1]))
with open('out1.txt','w') as out1:
    for tag in sorted(tag_dict.items(), key=lambda x: x[0], reverse=True):
            out1.write('{} {} {}\n'.format(tag[0],tag[1][0],tag[1][1]))



                




