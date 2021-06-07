import requests
from utils.logger import CustomLogger

class JiraRequestor:
    def __init__(self):
        self.logger = CustomLogger(__name__)

    def do_request(self, method='GET', url='', headers={"Accept": "application/json"}, \
                    body='', auth=None, \
                    timeout=45, verbose=False):
        """Do an http request given the parameters, retunrs the request's response
        if successfull. If there is an error logs the error using the file logger
        and returns None
        """
        try:
            if verbose == True:
                self.logger.info(f"Doing [{method}] request to {url}")
                self.logger.info(f"headers: {headers}")

            resp = requests.request(
                method=method,
                url=url,
                headers=headers,
                auth=auth,
                data=body,
                timeout=timeout,
            )
            return resp
        except Exception as e:
            message = f'Exception caused when doing [{method}] request to {url}'
            message += str(e)
            self.logger.error(message)
            return None