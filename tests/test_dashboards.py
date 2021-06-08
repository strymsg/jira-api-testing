import json
from datetime import datetime

from api.dashboards import Dashboards


# @pytest.fixture
# def jira_api_data():
#     configs = Configuration().configuration
#     data = JiraApiData(configs)
#     return data

def test_get_dashboards():
    resp = Dashboards().get()
    assert resp is not None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert len(json_response.get('dashboards', [])) >= 1

# def test_get_dashboard(jira_api_data):
#     resp = Dashboards(jira_api_data).get()
#     assert resp is not None
#     assert resp.status_code == 200

#     json_response = json.loads(resp.text)
#     print(json_response, type(json_response))
#     assert isinstance(json_response, dict)
#     assert len(json_response.get('dashboards', [])) >= 1


# def test_create_dashboard(jira_api_data):
#     payload = json.dumps({
#         "name": f"Test dashboard {datetime.now()}",
#         "description": "Some test description",
#         "sharePermissions": []
#     })
#     resp = Dashboards(jira_api_data).create(dashboard=payload)
#     assert resp is not None
#     assert resp.status_code == 200

#     json_response = json.loads(resp.text)
#     print(json_response, type(json_response))
#     assert isinstance(json_response, dict)


# def test_reject_create_dashbaord(jira_api_data):
#     payload = json.dumps({
#         "name": f"Test dashboard {datetime.now()}",
#         "description": "Some test description",
#         "sharePermissions": {}
#     })
#     resp = Dashboards(jira_api_data).create(dashboard=payload)
#     assert resp is not None
#     assert resp.status_code == 400