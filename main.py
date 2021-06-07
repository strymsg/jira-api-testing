import json
from datetime import datetime

from common.configuration import Configuration
from api.jira_api import JiraApiData

if __name__ == '__main__':
    print("API testing")

    print(Configuration().configuration)
    #jiraapi = JiraAPI(Configuration().configuration)

    createmeta_resp = jiraapi.createmeta()
    print(json.dumps(createmeta_resp, indent=2, sort_keys=True))

    dashboards_resp = jiraapi.getalldashboards()
    print(json.dumps(dashboards_resp, indent=2, sort_keys=True))

    createdashboard_resp = jiraapi.createdashboard(
        name="AT-test" + str(datetime.now()),
        description = "Some description here.")
    print(json.dumps(createdashboard_resp, indent=2, sort_keys=True))
