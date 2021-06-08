"""Dashboards endpoint for the Jira API."""

from api.jira_api_data import JiraApiData
import json
from utils.jira_requestor import JiraRequestor


class Dashboards:
    """Dashboard endpint for the Jira API."""

    def __init__(self):
        self.jira_requestor = JiraRequestor()
        self.jira_data = JiraApiData.get()
    
    def get(self):
        return self.jira_requestor.do_request(
            method='GET',
            url=self.jira_data['site'] + '/rest/api/3/dashboard',
            auth=self.jira_data['auth']
        )

    def create(self, dashboard={}):
        payload = json.dumps(dashboard)
        return self.jira_requestor.do_request(
            method='POST',
            url=self.jira_data['site'] + '/rest/api/3/dashboard',
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body=payload,
            auth=self.jira_data['auth']
        )