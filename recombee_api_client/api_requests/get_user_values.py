from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class GetUserValues(Request):
    """
    Get all the current property values of a given user.
    
    Required parameters:
    
    :param user_id: ID of the user properties of which are to be obtained.
    
    

    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'get'
        self.path = "/users/%s" % (self.user_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
