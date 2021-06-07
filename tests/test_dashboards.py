import pytest
import json
from datetime import datetime

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

@pytest.fixture
def now_string():
    return str(datetime.now())

def test_get_dashboard(jira_api_data):
    resp = Dashboards(jira_api_data).get()
    assert resp != None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert len(json_response.get('dashboards', [])) >= 1

def test_create_dashboard(jira_api_data, now_string):
    print(f"Now string: {now_string}")
    payload = json.dumps({
        "name": f"Test dashboard {now_string}",
        "description": "Some test description",
        "sharePermissions": []
    })
    resp = Dashboards(jira_api_data).create(dashboard=payload)
    assert resp != None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)