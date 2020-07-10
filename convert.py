import sys

def write(strings_filepath='strings.txt', splits_filepath='splits.txt', out_filepath='input.json'):
    strings = open(strings_filepath, 'r')
    splits = open(splits_filepath, 'r')

    result = open(out_filepath, 'w')

    result.write('{\n\t\"data\": [')

    result.write(',\n\t\t'.join('"{0}"'.format(l)
                            for l in strings.read().splitlines()))

    result.write('],\n\n\t\"names\": [')

    names = []
    indices = []
    for line in splits.read().splitlines():
        name, idx1, idx2 = line.split(' ')
        names.append(name)
        indices.append([idx1, idx2])

    result.write(', '.join('"{0}"'.format(n) for n in names))

    result.write('],\n\n\t\"split\": [')

    result.write(', '.join(str(i).replace('\'', '') for i in indices))

    result.write(']\n}')

if __name__ == '__main__':
    write(*sys.argv[1:])