import logging
import requests
from pydantic import BaseModel


default_headers = {'Content-Type': 'application/json'}
baseUrl = "https://thinking-tester-contact-list.herokuapp.com"
token_header = dict()

class ApiClientBase:

    @staticmethod
    def post_req(data: BaseModel, postfix_url = "", token=None):
        res = requests.post(url=baseUrl + postfix_url, headers= default_headers | token, data= data.model_dump_json())
        print(res)
        return res

    @staticmethod
    def get_req(postfix_url = "", token = None):
        res = requests.get(url=baseUrl + postfix_url, headers=default_headers | token)
        print(res)
        return res

    @staticmethod
    def put_req(data: BaseModel, postfix_url = "", token = None):
        return requests.put(url=baseUrl + postfix_url, headers=default_headers | token, data= data.model_dump_json())

    @staticmethod
    def patch_req(data: BaseModel, postfix_url = "", token = None):
        return requests.patch(url=baseUrl + postfix_url, headers=default_headers | token, data= data.model_dump_json())

    @staticmethod
    def delete_req(postfix_url = "", token = None):
        res = requests.delete(url=baseUrl + postfix_url, headers=default_headers | token)
        return res