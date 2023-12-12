data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
output = 0

for line in data:
    game_data = line.split(': ')
    id = int(game_data[0].replace('Game ', ''))
    sets_data = game_data[1].split('; ')

    set = {}

    for set_data in sets_data:
        cubes = set_data.split(', ')

        for cube in cubes:
            cube = cube.split(' ')

            if set.get(cube[1]) is None:
                set[cube[1]] = int(cube[0])
                continue
                
            if int(cube[0]) > set.get(cube[1]):
                set[cube[1]] = int(cube[0])
                continue
    
    output += (set.get('red') * set.get('green') * set.get('blue'))

print(output)