data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
output = 0

for line in data:
    numbers = []

    for char in line:
        if char.isnumeric():
            numbers.append(char)
    
    output += int(f'{numbers[0]}{numbers[-1]}')

print(output)