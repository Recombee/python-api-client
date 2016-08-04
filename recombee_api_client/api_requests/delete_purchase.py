from recombee_api_client.api_requests.request import Request

class DeletePurchase(Request):
    """
    Deletes an existing purchase uniquely specified by `userId`, `itemId`, and `timestamp` or all the purchases with given `userId` and `itemId` if `timestamp` is omitted.

    """

    def __init__(self,user_id, item_id, optional = dict()):
        """
        Required parameters:
        @param user_id: ID of the user who made the purchase.
        
        @param item_id: ID of the item of which was purchased.
        
        
        Optional parameters (given as dictionary C{optional}):
        @param timestamp: Unix timestamp of the purchase. If the `timestamp` is omitted, then all the purchases with given `userId` and `itemId` are deleted.
        
        """
        self.user_id = user_id
        self.item_id = item_id
        self.timestamp = optional.get('timestamp')
        for par in optional:
            if not par in {"timestamp"}:
                raise ValueError("Unknown parameter %s was given to the request" % par)
        self.timeout = 1000
        self.ensure_https = False
        self.method = 'delete'
        self.path = "/{databaseId}/purchases/" % ()

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
        params['userId'] = self.user_id
        params['itemId'] = self.item_id
        if self.timestamp is not None:
            params['timestamp'] = self.timestamp
        return params
