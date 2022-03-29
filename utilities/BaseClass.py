import requests


class BaseClass:

    def getRequest(self, url, params):
        response = requests.request("GET", url=url, params=params)
        return response
