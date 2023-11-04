def initialize(api):
    return Users(api)

class Users:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "users"

    def list(self):
        """
        Retrieves a list of items from the API.

        Returns:
            A JSON object representing the list of items.
        """
        response = self._api.get(self._name)
        return response.json()

    def add(self, params):
        response = self._api.post(self._name, params)
        return response.json()

    # def delete(self, params):
    #     client = self.get_client()
    #     response = client.delete("", json=params, timeout=10)
    #     client.handle_response(response)
    #     return response.json()

    # def modify(self, params):
    #     client = self.get_client()
    #     response = client.put("", json=params, timeout=10)
    #     client.handle_response(response)
    #     return response.json()
