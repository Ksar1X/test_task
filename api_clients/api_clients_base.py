
import requests
from pydantic import BaseModel


token_header = dict()

class ApiClientBase:

    default_headers = {'Content-Type': 'application/json'}
    baseUrl = "https://thinking-tester-contact-list.herokuapp.com"

    def post_req(self, data: BaseModel, postfix_url = "", token=None):
        return requests.post(url=self.baseUrl + postfix_url, headers= self.default_headers | token, data= data.model_dump_json())


    def get_req(self, postfix_url = "", token = None):
        return requests.get(url=self.baseUrl + postfix_url, headers=self.default_headers | token)


    def put_req(self, data: BaseModel, postfix_url = "", token = None):
        return requests.put(url=self.baseUrl + postfix_url, headers=self.default_headers | token, data= data.model_dump_json())


    def patch_req(self, data: BaseModel, postfix_url = "", token = None):
        return requests.patch(url=self.baseUrl + postfix_url, headers=self.default_headers | token, data= data.model_dump_json())


    def delete_req(self, postfix_url = "", token = None):
        return requests.delete(url=self.baseUrl + postfix_url, headers=self.default_headers | token)