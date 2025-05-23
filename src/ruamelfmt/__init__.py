import sys
from ruamel.yaml import YAML

yaml = YAML(typ='rt')

path = sys.argv[1]

with open(path) as f:
    data = yaml.load(f)

with open(path, 'w') as f:
    yaml.dump(data, f)
