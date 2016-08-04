from recombee_api_client.api_requests.request import Request

class AddCartAddition(Request):
    """
    Adds a cart addition of a given item made by a given user.

    """

    def __init__(self,user_id, item_id, optional = dict()):
        """
        Required parameters:
        @param user_id: User who added the item to the cart
        
        @param item_id: Item added to the cart
        
        
        Optional parameters (given as dictionary C{optional}):
        @param timestamp: UTC timestamp of the cart addition as ISO8601-1 pattern or UTC epoch time. The default value is the current time.
        
        @param cascadeCreate: Sets whether the given user/item should be created if not present in the database.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = optional.get('timestamp')
        self.cascade_create = optional.get('cascadeCreate')
        for par in optional:
            if not par in {"timestamp","cascadeCreate"}:
                raise ValueError("Unknown parameter %s was given to the request" % par)
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/{databaseId}/cartadditions/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.user_id
        p['itemId'] = self.item_id
        if self.timestamp is not None:
            p['timestamp'] = self.timestamp
        if self.cascade_create is not None:
            p['cascadeCreate'] = self.cascade_create
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
