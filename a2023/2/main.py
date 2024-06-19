



INPUT_FILE = '2/input.txt'

# input format: 
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

def parse_line(line):
    game, gems = line.split(':')
    print('Game:', game )
    # print('Gems:', gems)

    rounds = gems.split(';')
    print('Rounds:', len(rounds))

    g = []
    for round in rounds:
        r = round.strip().split(',')
        for i in range(len(r)):
            num, color = r[i].strip().split(' ')
            print('Round:', num, color)
            



if __name__ == '__main__':
    
    # Read input file
    with open(INPUT_FILE, 'r') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            
            line = parse_line(data[i]) 