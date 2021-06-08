"""Dashboards endpoint for the Jira API."""

from api.jira_api_data import JiraApiData
import json
from utils.jira_requestor import JiraRequestor
from common.constants import JIRA_ENDPOINTS

class Dashboards:
    """Dashboard endpint for the Jira API."""

    def __init__(self):
        self.jira_requestor = JiraRequestor()
        self.jira_data = JiraApiData.get()
    
    def get(self):
        return self.jira_requestor.do_request(
            method='GET',
            url=self.jira_data['site'] + JIRA_ENDPOINTS['DASHBOARD']['GET'],
            auth=self.jira_data['auth']
        )

    def create(self, dashboard={}):
        payload = json.dumps(dashboard)
        return self.jira_requestor.do_request(
            method='POST',
            url=self.jira_data['site'] + JIRA_ENDPOINTS['DASHBOARD']['GET'],
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body=payload,
            auth=self.jira_data['auth']
        )

    def delete(self, dashboard_id):
        url = self.jira_data['site'] + JIRA_ENDPOINTS['DASHBOARD']['DELETE']
        url += dashboard_id
        return self.jira_requestor.do_request(
            method='DELETE',
            url=url,
            auth=self.jira_data['auth']
        )