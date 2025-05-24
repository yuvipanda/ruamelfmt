import argparse
import sys
from ruamel.yaml import YAML

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--line-length', default=sys.maxsize, type=int)
    parser.add_argument('filepath', nargs='+')
    args = parser.parse_args()

    yaml = YAML(typ='rt')
    yaml.width = args.line_length

    for filepath in args.filepath:
        with open(filepath) as f:
            data = yaml.load(f)

        with open(filepath, 'w') as f:
            yaml.dump(data, f)

if __name__ == '__main__':
    main()