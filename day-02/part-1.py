data = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
cube_requirement = input('(count color)(, ): ')

requirement_dict = {}

for requirement in cube_requirement.split(', '):
    cube = requirement.split(' ')
    requirement_dict[cube[1]] = int(cube[0])

output = 0

for line in data:
    game_pass = True

    game_data = line.split(': ')
    id = int(game_data[0].replace('Game ', ''))
    sets_data = game_data[1].split('; ')

    for set_data in sets_data:
        cubes = set_data.split(', ')
        set = {}

        for cube in cubes:
            cube = cube.split(' ')

            set[cube[1]] = int(cube[0])
    
        for requirement in set:
            if requirement_dict.get(requirement) is None:
                game_pass = False
                continue
            
            if set.get(requirement) > requirement_dict.get(requirement):
                game_pass = False
                continue
        
        if not game_pass:
            break
    
    if game_pass == True:
        output += id

print(output)