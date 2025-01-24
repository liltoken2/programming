def median(numbers):
    numbers.sort()
    n = len(numbers)
    return (numbers[n // 2 - 1] + numbers[n // 2]) / 2 if n % 2 == 0 else numbers[n // 2]

def file_to_dict(file_name):
    stack = []
    dict_stack = [{}]
    values = []
    with open(file_name) as f:
        for line in f:
            tokens = line.replace(' ', '').replace('<', ' ').replace('>', ' ').split()
            for token in tokens:
                if token.startswith('/'):
                    stack.pop()
                    dict_stack.pop()
                elif token.isdigit():
                    values.append(int(token))
                    current_dict[stack[-1]] = int(token)
                else:
                    new_dict = {}
                    current_dict = dict_stack[-1]
                    current_dict[token] = new_dict
                    stack.append(token)
                    dict_stack.append(new_dict)
    dict_stack[0]['median'] = median(values)
    return dict_stack[0]


with open('out.txt', 'w') as f:
    f.write(str(file_to_dict('in.txt')))