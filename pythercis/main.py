import requests
import urllib

class Pythercis:

    def __init__(self, baseurl, username, password):
        self.baseurl = baseurl
        # create new session
        self.create_session(username, password)
        self.default_headers = {
            'Ehr-Session': self.session_id
            }

    def create_session(self, username, password):
        self.username = username
        self.password = password
        api_path = "/rest/v1/session"
        querystring = {
            "username": self.username,
            "password": self.password
            }
        headers = {
            'username': self.username,
            'password': self.password,
            'cache-control': "no-cache",
            }
        response = requests.post(self.baseurl + api_path, headers=headers, params=querystring)
        self.session_id = response.headers['Ehr-Session']
        print(response.text)
        return response

    def delete_session(self):
        api_path = "/rest/v1/session"
        headers = self.default_headers
        response = requests.delete(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def list_templates(self):
        api_path = "/rest/v1/template/"
        headers = self.default_headers
        response = requests.get(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def upload_template(self, template_relative_path):
        files = {'file': open(template_relative_path, 'rb')}
        api_path = "/rest/v1/template/"
        headers = self.default_headers
        headers['Content-Type'] = 'application/xml'
        response = requests.post(self.baseurl + api_path, headers=headers, files=files)
        print(response.text)
        return response

    def delete_template(self, template_id):
        # this HTTP verb doesn't seem to be implemented in EtherCIS??
        api_path = "/rest/v1/template/"
        headers = self.default_headers
        response = requests.post(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def template_example(self, template_id):
        api_path = "/rest/v1/template/"
        headers = self.default_headers
        payload = urllib.parse.quote(template_id) + "/example"
        print(payload)
        params = {
            "format": "FLAT",
            "exampleFilter": "INPUT"
        }
        response = requests.get(self.baseurl + api_path + payload, headers=headers, params=params)
        print(response.text)
        return response
