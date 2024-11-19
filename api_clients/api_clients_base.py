
import requests
from pydantic import BaseModel

user_token = dict()
class ApiClientBase:

    default_headers = {'Content-Type': 'application/json'}
    baseUrl = "https://thinking-tester-contact-list.herokuapp.com"

    def post_req(self, data: BaseModel, token = "", postfix_url = ""):
        if token != "":
            user_token['Authorization'] = f'Bearer {token}'
        return requests.post(url=self.baseUrl + postfix_url, headers= self.default_headers | user_token, data= data.model_dump_json())


    def get_req(self, token = "", postfix_url = ""):
        if token != "":
            user_token['Authorization'] = f'Bearer {token}'
        return requests.get(url=self.baseUrl + postfix_url, headers=self.default_headers | user_token)


    def put_req(self, data: BaseModel, token = "", postfix_url = ""):
        if token != "":
            user_token['Authorization'] = f'Bearer {token}'
        return requests.put(url=self.baseUrl + postfix_url, headers=self.default_headers | user_token, data= data.model_dump_json())


    def patch_req(self, data: BaseModel,token = "", postfix_url = ""):
        if token != "":
            user_token['Authorization'] = f'Bearer {token}'
        return requests.patch(url=self.baseUrl + postfix_url, headers=self.default_headers | user_token, data= data.model_dump_json())


    def delete_req(self,token = "", postfix_url = ""):
        if token != "":
            user_token['Authorization'] = f'Bearer {token}'
        return requests.delete(url=self.baseUrl + postfix_url, headers=self.default_headers | user_token)