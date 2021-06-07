import os
import json
from json import JSONDecodeError
import pprint

class Configuration:
    # TODO: check if is it really needed to init to read a json?
    def __init__(self):
        self.configuration = {}
        filename = os.path.join(os.path.abspath(os.path.dirname(__file__)))
        filename = os.path.join(filename, 'configs.json')
        print(f'filename: {filename}')

        with open(filename) as jsonfile:
            try:
                d = json.loads(jsonfile.read())
                self.configuration = d
            except JSONDecodeError as err:
                print(f'Error decoding json {jsonfile.name}')
                print(err)

    def get_config_var(self, var_name, default_value=None):
        return self.configuration.get(var_name, default_value)
