import json
from datetime import datetime

from api.dashboards import Dashboards


def test_get_dashboards():
    resp = Dashboards().get()
    assert resp is not None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert len(json_response.get('dashboards', [])) >= 1

def test_create_dashboard():
    payload = {
        "name": f"Test dashboard {datetime.now()}",
        "description": "Some test description",
        "sharePermissions": []
    }
    resp = Dashboards().create(dashboard=payload)
    assert resp is not None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)


def test_reject_create_dashbaord():
    payload = {
        "name": f"Test dashboard {datetime.now()}",
        "description": "Some test description",
        "sharePermissions": {}
    }
    resp = Dashboards().create(dashboard=payload)
    assert resp is not None
    assert resp.status_code == 400
