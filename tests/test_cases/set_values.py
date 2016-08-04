#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class SetValuesTest (RecombeeTest ):

    def create_request(self,entity_id,values):
        pass

    def test_set_values(self):

        # it 'does not fail with existing entity and property'
        req = self.create_request('entity_id',{'int_property': 5})
        resp = self.client.send(req)
        # it 'sets multiple properties'
        req = self.create_request('entity_id',{'int_property': 5,'str_property': 'test'})
        resp = self.client.send(req)
        # it 'does not fail with !cascadeCreate'
        req = self.create_request('new_entity',{'int_property': 5,'str_property': 'test','!cascadeCreate': True})
        resp = self.client.send(req)
        # it 'fails with nonexisting entity'
        req = self.create_request('nonexisting',{'int_property': 5})
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

