#
# This file is auto-generated, do not edit
#

from tests.test_cases.set_values import SetValuesTest
from recombee_api_client.api_requests import *

class SetItemValuesTestCase (SetValuesTest):

    def create_request(self, item_id, values):
        return SetItemValues(item_id, values)
