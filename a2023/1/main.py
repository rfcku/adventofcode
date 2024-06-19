


INPUT_FILE = '1/input.txt'

# numbers in text form
NUMBERS = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten',
}

def get_number(line, matches):
    indices = [match['index'] for match in matches]
    numbers = []
    for character_index in range(len(line)):
        character = line[character_index]
        if character_index in indices:
            m = matches[indices.index(character_index)]
            numbers.append(m['number'])
            character_index += len(m['number_text'])
            continue
        if character.isdigit():
            numbers.append(character)
    return numbers

def get_line_matches(line):
    matches = []
    for number in NUMBERS:
        number_text = NUMBERS[number]
        if str(number_text) in line:
            indices = [
                index for index in range(len(line))
                if line.startswith(str(number_text), index)
            ]
            for index in indices:
                matches.append({"index": index, "number_text": number_text, "number": str(number)})

    return get_number(line, matches )

def first_and_last(line):
    first = line[0]
    last = line[-1]
    return first, last

if __name__ == '__main__':
    all = []
    # Read input file
    with open(INPUT_FILE, 'r') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            line_numbers = get_line_matches(data[i])
            # print('LineI:', i, 'Line:', data[i], 'Numbers:', line_numbers)
            first, last = first_and_last(line_numbers)
            all.append(int(str(first) + str(last)))
    print('Sum:', sum(all))