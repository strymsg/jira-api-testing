import json

from common.configs import Configuration
from api.api import JiraAPI

if __name__ == '__main__':
    print("API testing")

    jiraapi = JiraAPI(Configuration().configuration)

    createmeta_resp = jiraapi.createmeta()
    print(json.dumps(createmeta_resp, indent=2, sort_keys=True))
