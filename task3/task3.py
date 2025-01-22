stack = []
tags_dict = {}
depth = 0
with open('in.txt') as f:
    for line in f:
        line = line.replace(' ', '').replace('<', '').replace('>', ' ')
        tags = line.split()
        for tag in tags:
            if tag[0] == '/':
                if stack and stack[-1] == tag[1:]:
                    depth -= 1
                    stack.pop()
            else:
                depth += 1
                if tag not in tags_dict:
                    tags_dict[tag] = [0, 0]
                tags_dict[tag][0] += 1
                tags_dict[tag][1] = max(depth, tags_dict[tag][1])
                stack.append(tag)

    with open('out.txt', 'w') as f:
        for tag in sorted(tags_dict.items(), key=lambda x: x[0], reverse=True):
            f.write(f'{tag[0]} {tag[1][0]} {tag[1][1]}\n')
