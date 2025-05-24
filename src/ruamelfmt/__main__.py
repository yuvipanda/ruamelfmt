import argparse
import sys
from ruamel.yaml import YAML
from ruamel.yaml.constructor import DuplicateKeyError
from ruamel.yaml.scanner import ScannerError

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--line-length', default=sys.maxsize, type=int)
    parser.add_argument('filepath', nargs='+')
    args = parser.parse_args()

    yaml = YAML(typ='rt')
    yaml.width = args.line_length

    should_fail = False
    for filepath in args.filepath:
        with open(filepath) as f:
            try:
                data = yaml.load(f)
            except (ScannerError, DuplicateKeyError) as e:
                print(f"Error {str(e.problem_mark).strip()}: {e.problem.strip()}")
                should_fail = True
                # Continue formatting other files
                continue

        with open(filepath, 'w') as f:
            yaml.dump(data, f)

    if should_fail:
        sys.exit(1)

if __name__ == '__main__':
    main()