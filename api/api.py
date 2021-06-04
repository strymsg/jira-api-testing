import requests
import json
from requests.auth import HTTPBasicAuth


class JiraAPI:
    ''' Helper for JIRA API requests
    '''
    def __init__(self, configs={}):
        self.api_token = configs['jira-api-token']
        self.email = configs['jira-email']
        self.site = configs['jira-site']

        self.auth = HTTPBasicAuth(self.email, self.api_token)

    def createmeta(self):
        ''' Requests to the createmeta endpoint and returns the
        content in json format'''
        print('[GET] createmeta')
        headers_dict = {
            "Accept": "application/json"
        }
        try:
            url = self.site + '/rest/api/2/issue/createmeta'
            response = requests.get(url, headers=headers_dict, auth=self.auth)
            return response.json()
        except Exception as e:
            print('Exception occurred while doing request createmeta:')
            print(e)

    def getalldashboards(self):
        ''' Get all dashboards from site '''
        print('[GET] get all dashboards')
        headers_dict = {
            "Accept": "application/json"
        }
        try:
            url = self.site + '/rest/api/3/dashboard'
            url = 'https://rmgarcia.atlassian.net/rest/api/3/dashboard'
            response = requests.get(url=url,
                                    headers=headers_dict,
                                    auth=self.auth)
            #print(response.content)
            #response.json()
            return json.loads(response.text)
        except Exception as e:
            print('Exception occurred while doing request getalldashboards')
            print(e)
