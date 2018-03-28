import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pythercis


# current assumptions:
# 1) you have a running EtherCIS server at localhost:8080
# 2) username: root and password: secret will work

class TestAuthentication(unittest.TestCase):

    def test_create_session(self):
        # set up the etherCIS connection
        ehr = pythercis.Pythercis('http://localhost:8080')
        response = ehr.create_session("root", "secret")
        # assume a response code of 200 to this method = success
        self.assertEqual(response.status_code, 200)
        # assume an action of "CREATE" means a session has been created
        self.assertEqual(response.json()["action"], "CREATE")


if __name__ == '__main__':
    unittest.main()
