from api.create_meta import CreateMeta


# @pytest.fixture
# def jira_api_data():
#     configs = Configuration().configuration
#     data = JiraApiData(configs)
#     return data

def test_get_create_meta():
    resp = CreateMeta().get()
    assert resp is not None
    assert resp.status_code == 200
    assert resp.headers is not None
    assert resp.content is not None
