import pytest
import json

from common.configuration import Configuration
from api.jira_api import JiraApiData, Dashboards

class JiraData:
    def __init__(self, configs):
        self.api_data = JiraApiData(configs=configs)

@pytest.fixture
def jira_api_data():
    configs = Configuration().configuration
    data = JiraApiData(configs)
    return data

def test_get_dashboard(jira_api_data):
    resp = Dashboards(jira_api_data).get()
    assert resp != None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert len(json_response.get('dashboards', [])) >= 1
    #assert isinstance(resp.headers, dict) == True
    #print(resp.headers)
    #print(resp.content)
    