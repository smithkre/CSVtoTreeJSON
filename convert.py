import sys
import json
from collections import OrderedDict

def main(argv):
    if len(argv) < 3:
        print('-- python convert.py <input_csv> <output_json> --\n')
        return

    argv = argv[1:]

    memory = OrderedDict()
    with open(argv[0], 'r', encoding='utf8') as f:
        data = f.readlines()
        first = True
        for row in data:
            if first:
                first = False
                continue

            items = row.split(',')

            current = memory
            for val in items:
                val = val.strip()
                if val not in current:
                    current[val] = OrderedDict()
                current = current[val]

        f.close()

    output = reduce(memory)

    with open(argv[1], 'w', encoding='utf8') as f:
        f.write(json.dumps(output))
        f.close()

def reduce(data):
    if data is {}:
        return None

    temp = []
    for obj in data:
        children = reduce(data[obj])
        if children:
            temp.append({
                'title': obj,
                'children': children
            })
        else:
            temp.append({
                'title': obj
            })
    return temp

if __name__ == '__main__':
    main(sys.argv)

