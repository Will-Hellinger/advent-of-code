data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
output = 0


for l in range(len(data)):
    numbers = []
    number_indexes = []

    number = ''
    start_index = [0, 0]
    
    for c in range(len(data[l])):
        if data[l][c].isnumeric():
            if number == '':
                start_index = [l, c]

            number += data[l][c]

        elif number != '' and not data[l][c].isnumeric():
            numbers.append(number)
            
            for i in range(len(number)):
                number_indexes.append([start_index[0], start_index[1] + i])
            
            number = ''
    
    start_index = 0
    for number in numbers:
        indexes = []

        for i in range(len(number)):
            indexes.append(number_indexes[i + start_index])

        start_index += len(number)

        number_works = False
        for index in indexes:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        if not data[index[0]+i][index[1]+j].isnumeric() and data[index[0]+i][index[1]+j] != '.':
                            number_works = True
                    except:
                        print('lmao')
        
        if number_works:
            output += int(number)

print(output)