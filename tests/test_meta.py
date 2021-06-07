import pytest

from common.configuration import Configuration
from api.jira_api import JiraApiData, CreateMeta

class JiraData:
    def __init__(self, configs):
        self.api_data = JiraApiData(configs=configs)

@pytest.fixture
def jira_api_data():
    configs = Configuration().configuration
    print(f'configs jiradata: {configs}, type {type(configs)}')
    data = JiraApiData(configs)
    return data

def test_get_create_meta(jira_api_data):
    resp = CreateMeta(jira_api_data).get()
    assert resp != None
    print(resp.headers)