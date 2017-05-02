import yaml
import json

with open("input.json", 'r') as input_file:
    try:
        with open("output.yml", 'w+') as output_file:
            data = json.load(input_file)
            output_file.write(yaml.safe_dump(data, default_flow_style=False))
    except yaml.YAMLError as exc:
        print(exc)
