import requests
import json
from requests.auth import HTTPBasicAuth

from utils.logger import CustomLogger
from utils.jira_requests import JiraRequestor

jira_requestor = JiraRequestor()

class JiraApiData:
    def __init__(self, configs={}):
        self.api_token = configs['jira-api-token']
        self.email = configs['jira-email']
        self.site = configs['jira-site']

        self.auth = HTTPBasicAuth(self.email, self.api_token)

class CreateMeta:
    def __init__(self, jira_data:JiraApiData):
        self.jira_data = jira_data

    def get(self, verbose=False):
        return jira_requestor.do_request(
            method='GET',
            url=self.jira_data.site + '/rest/api/2/issue/createmeta',
            auth=self.jira_data.auth,
            verbose=verbose
        )
         
class GetAllDashboards:
    def __init__(self, jira_data:JiraApiData):
        self.jira_data = jira_data
    
    def get(self):
        return jira_requestor.do_request(
            method='GET',
            url=self.jira_data.site + '/rest/api/3/dashboard',
            auth=self.jira_data.auth
        )

class create_dashboard:
    def __init__(self, jira_data:JiraApiData, dashboard={}):
        self.jira_data = jira_data
        self.dashboard = dashboard

    def post(self, dashboard={}):
        payload = json.dumps(dashboard)
        return jira_request.do_request(
            method='POST',
            url=self.jira_data.site + '/rest/api/3/dashboard',
            headers_dict={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body=dashboard,
            auth=self.jira_data.auth
        )


# TODO: use loggers
# TODO: split into multiple classes
# class JiraAPI:
#     ''' Helper for JIRA API requests
#     '''
#     def __init__(self, configs={}):
#         self.api_token = configs['jira-api-token']
#         self.email = configs['jira-email']
#         self.site = configs['jira-site']

#         self.auth = HTTPBasicAuth(self.email, self.api_token)

#     def createmeta(self):
#         ''' Requests to the createmeta endpoint and returns the
#         content in json format'''
#         print('[GET] createmeta')
#         headers_dict = {
#             "Accept": "application/json"
#         }
#         try:
#             url = self.site + '/rest/api/2/issue/createmeta'
#             response = requests.get(url, headers=headers_dict, auth=self.auth)
#             return response.json()
#         except Exception as e:            print('Exception occurred while doing request createmeta:')
#             print(e)

#     def get_all_dashboards(self):
#         ''' Get all dashboards from site '''
#         print('[GET] get all dashboards')
#         url = self.site + '/rest/api/3/dashboard'
#         headers_dict = {
#             "Accept": "application/json"
#         }
#         # TODO: use a request manager to handle exceptions
#         try:
#             url = 'https://rmgarcia.atlassian.net/rest/api/3/dashboard'
#             response = requests.get(url=url,
#                                     headers=headers_dict,
#                                     auth=self.auth)
#             #print(response.content)
#             #response.json()
#             return json.loads(response.text)
#         except Exception as e:
#             print('Exception occurred while doing request getalldashboards')
#             print(e)

#     def createdashboard(self, name='TEST DASHBOARD', description="test",
#                         shared_permissions=[]):
#         print(f'[POST] create the dashboard: {name}')
#         url = self.site + "/rest/api/3/dashboard"
#         headers_dict  = {
#             "Accept": "application/json",
#             "Content-Type": "application/json"
#         }
#         payload = json.dumps({
#             "name": name,
#             "description": description,
#             "sharePermissions": shared_permissions
#         })
#         try:
#             response = requests.post(url, data=payload,
#                                     headers=headers_dict, auth=self.auth)
#             return json.loads(response.text)
#         except Exception as e:
#             print('Exception while creating dashboard request')
#             print(e)        
