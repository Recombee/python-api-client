#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_property import DeletePropertyTest
from recombee_api_client.api_requests import *

class DeleteItemPropertyTestCase (DeletePropertyTest):

    def create_request(self, property_name):
        return DeleteItemProperty(property_name)
