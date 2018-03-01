import requests


class Pythercis:

    def __init__(self, ethercis_baseurl):
        self.baseurl = ethercis_baseurl

    def create_session(self, ethercis_username, ethercis_password):
        self.username = ethercis_username
        self.password = ethercis_password
        api_path = "/rest/v1/session"
        querystring = {
            "username": self.username,
            "password": self.password
            }
        headers = {
            'username': self.username,
            'password': self.password,
            'cache-control': "no-cache",
            'postman-token': "f5fefaa7-d9b4-2595-ecd6-a99dcc0f96b3"
            }
        response = requests.post(self.baseurl + api_path, headers=headers, params=querystring)
        print(response.text)
        self.session_id = response.headers['Ehr-Session']
        return response

    def delete_session(self):
        api_path = "/rest/v1/session"
        headers = {
            'Ehr-Session': self.session_id
            }
        response = requests.delete(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def list_templates(self):
        api_path = "/rest/v1/template"
        headers = {
            'Ehr-Session': self.session_id
            }
        response = requests.get(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def upload_template(self, template_relative_path):
        files = {'file': open(template_relative_path, 'rb')}
        api_path = "/rest/v1/template"
        headers = {
            'Ehr-Session': self.session_id,
            'Content-Type': 'application/xml'
            }
        response = requests.post(self.baseurl + api_path, headers=headers, files=files)
        print(response.text)
        return response

    def delete_template(self, template_id):
        # this HTTP verb doesn't seem to be implemented in EtherCIS??
        api_path = "/rest/v1/template"
        headers = {
            'Ehr-Session': self.session_id,
            }
        response = requests.post(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response

    def template_example(self, template_id):
        api_path = "/rest/v1/template"
        headers = {
            'Ehr-Session': self.session_id,
            }
        response = requests.post(self.baseurl + api_path, headers=headers)
        print(response.text)
        return response
