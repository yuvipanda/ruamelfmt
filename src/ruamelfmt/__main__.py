import argparse
from ruamel.yaml import YAML

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--line-length', default=120, type=int)
    parser.add_argument('filepath')
    args = parser.parse_args()

    yaml = YAML(typ='rt')
    yaml.width = args.line_length

    with open(args.filepath) as f:
        data = yaml.load(f)

    with open(args.filepath, 'w') as f:
        yaml.dump(data, f)

if __name__ == '__main__':
    main()