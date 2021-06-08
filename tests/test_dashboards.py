import json
from datetime import datetime

from api.dashboards import Dashboards
from common.payloads import DASHBOARDS

def test_get_dashboards():
    resp = Dashboards().get()
    assert resp is not None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print(json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert len(json_response.get('dashboards', [])) >= 1

def test_create_dashboard():
    # TODO: Add cleanup
    resp = Dashboards().create(dashboard=DASHBOARDS['CREATE_OK'])
    assert resp is not None
    assert resp.status_code == 200

    json_response = json.loads(resp.text)
    print('CREATE DASHBOARD', json_response, type(json_response))
    assert isinstance(json_response, dict)
    assert json_response.get('id', None) is not None
    
    # TODO: Find a better way to cleanup
    print(f'TRYING TO DELETE {json_response["id"]}')
    respd = Dashboards().delete(json_response['id'])
    assert respd is not None
    assert respd.status_code == 204

def test_reject_create_dashboard():
    resp = Dashboards().create(dashboard=DASHBOARDS['CREATE_FAIL_1'])
    assert resp is not None
    assert resp.status_code == 400
