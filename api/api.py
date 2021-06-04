import requests
from requests.auth import HTTPBasicAuth

class JiraAPI:
    ''' Helper for JIRA API requests
    '''
    def __init__(self, configs={}):
        self.api_token = configs['jira-api-token']
        self.email = configs['jira-email']
        self.site = configs['jira-site']

    def createmeta(self):
        ''' Requests to the createmeta endpoint and returns the
        content in json format'''
        print('[GET] createmeta')
        auth = HTTPBasicAuth(self.email, self.api_token)
        headers_dict = {
            "Accept": "application/json"
        }
        try:
            url = self.site + '/rest/api/2/issue/createmeta'
            response = requests.get(url, headers=headers_dict, auth=auth)
            return response.json()
        except Exception as e:
            print('Exception occurred while doing request createmeta:')
            print(e)
