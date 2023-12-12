data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
output = 0
number = ''
use_number = False
s
for l in range(len(data)):
    line = data[l]

    for c in range(len(line)):
        if line[c].isnumeric():
            number += line[c]

            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if (0 <= l + j < len(data)) and (0 <= c + k < len(line)):
                        if not data[l + j][c + k].isnumeric() and data[l + j][c + k] != '.':
                            use_number = True

        elif not line[c].isnumeric() or c == len(line) - 1:
            if use_number:
                output += int(number)
                
            use_number = False
            number = ''

print(output)