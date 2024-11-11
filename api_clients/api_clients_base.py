import requests
from pydantic import BaseModel

from api_clients.contact_client.contact_client import base_url, headers


class ApiClientBase:
    default_headers = {'Content-Type': 'application/json'}

    baseUrl = "https://thinking-tester-contact-list.herokuapp.com/"
    def POST(self, postfix_url:str, headers:dict, token:str, data: BaseModel):

        requests.post(url=base_url + postfix_url, headers=headers | self.default_headers | "TOKEN", data= data.model_dump_json() )

    def GET(self, postfix_url: str, headers: dict, token: str, data: BaseModel):
        requests.post(url=base_url + postfix_url, headers=headers | self.default_headers | "TOKEN")

    def PUT(self, postfix_url: str, headers: dict, token: str, data: BaseModel):
        requests.post(url=base_url + postfix_url, headers=headers | self.default_headers | "TOKEN")
