import re

numbers_dict = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
output = 0

for line in data:
    line_dict = {}

    for number in numbers_dict:
        if line.find(number) != -1:
            founds = [m.start() for m in re.finditer(number, line)]

            for found in founds:
                line_dict[found] = numbers_dict[number]
    
    for c in range(len(line)):
        if line[c].isnumeric():
            line_dict[c] = line[c]
        
    output += int(f'{line_dict[min(line_dict.keys())]}{line_dict[max(line_dict.keys())]}')

print(output)