import yaml
import json

with open("input.yml", 'r') as input_file:
    try:
        with open("output.json", 'w+') as output_file:
            data = yaml.load(input_file)
            output_file.write(json.dumps(data))
    except yaml.YAMLError as exc:
        print(exc)
