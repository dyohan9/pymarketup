from pydoc import locate


class MarketUP(object):
    def __init__(self):
        self._endpoint_path = {
            "addresstype": "pymarketup.endpoints.addresstype.AddressType",
        }

    def endpoint(self, endpoint):
        return locate(self._endpoint_path.get(endpoint))()

