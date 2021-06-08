"""CreateMeta Endpoint for the Jira API."""

from api.jira_api_data import JiraApiData
from utils.jira_requestor import JiraRequestor


class CreateMeta:
    """Createmeta endpoint for the jira API."""

    def __init__(self):
        """Get the instance of JiraRequestor."""
        self.jira_requestor = JiraRequestor()
        self.jira_data = JiraApiData.get()

    def get(self, verbose=False):
        """Perform the get request for createmeta endpoint."""
        return self.jira_requestor.do_request(
            method='GET',
            url=self.jira_data['site'] + '/rest/api/2/issue/createmeta',
            auth=self.jira_data['auth'],
            verbose=verbose)