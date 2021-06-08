"""Helper to store configurations for the jira api."""
import os
import json
from json import JSONDecodeError
from requests.auth import HTTPBasicAuth


class JiraApiData:
    """Helper class to store configurations for jira api.

    This class has the classmethod get() in order to get the jira api
    configurations withouth for instantiation.
    """

    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    filename = os.path.join(filename, '..', 'common', 'configs.json')
    configs = {}

    print(f'config filename: {filename}')
    with open(filename) as jsonfile:
        try:
            d = json.loads(jsonfile.read())
            configs = d
        except JSONDecodeError as err:
            print(f'Error decoding json {jsonfile.name}')
            print(err)

    @classmethod
    def get(cls):
        """Return the api-data as dictionary."""
        auth = HTTPBasicAuth(
            cls.configs['jira-email'],
            cls.configs['jira-api-token'])
        return {
            'api_token': cls.configs['jira-api-token'],
            'email': cls.configs['jira-email'],
            'site': cls.configs['jira-site'],
            'auth': auth
        }
