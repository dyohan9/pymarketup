from pydoc import locate


class MarketUP(object):
    def __init__(self):
        self._endpoint_path = {
            "auth": "pymarketup.endpoints.auth.Auth",
        }

    def endpoint(self, endpoint):
        return locate(self._endpoint_path.get(endpoint))()
