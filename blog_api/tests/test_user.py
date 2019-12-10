import unittest
import os
import json
from ..app import create_app, db


class UsersTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {
            'name': 'shannon',
            'email': 'shannon@mail.com',
            'password': 'hi'
        }

        with self.app.app_context():
            db.create_all()


    def test_user_creation(self):

        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.AssertTrue(json_data.get('jwt_token'))
        self.assertEqual(res.status_code,201)


    def test_user_creation_with_existing_email(self):
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.assertEqual(res.statis_code, 400)
        self.assertTrue(json_data.get('error'))