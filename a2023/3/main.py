import re 
import sys

def get_file_lines(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def is_symbol(c):
    return not c.isdigit() and c != '.'

def is_number(c):
    return c.isdigit()


def symbol_coords(data):
    coords = set()
    for r, line in enumerate(data.splitlines()):
        for m in re.finditer(r"[^\d\.]", line):
            coords.add((r, m.start()))
    return coords

def xyneighbors(xy):
    x, y = xy
    return [
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    ]

def iter_poss_partnums(data):
    for r, line in enumerate(data.splitlines()):
        for m in re.finditer(r"\d+", line):
            yield int(m.group()), [(r, c) for c in range(m.start(), m.end())]

def partnum_sum(data):
    total = 0
    symset = symbol_coords(data)

    def foundone(coordlist):
        for rc in coordlist:
            for nabe in xyneighbors(rc):
                if nabe in symset:
                    return True
        return False

    for partnum, coords in iter_poss_partnums(data):
        if foundone(coords):
            total += partnum
    return total

if __name__ == '__main__':

    lines = get_file_lines('input.txt')


    print('lines:', symbol_coords(lines))

    print('numbers:', list(iter_poss_partnums(lines)))

    print('partnum_sum:', partnum_sum(lines))

    sys.exit() 