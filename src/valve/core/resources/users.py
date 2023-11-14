def initialize(api):
    return Users(api)

class Users:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "users"

    def list(self):
        """
        Retrieves a list of items from the API.
        GET: /api/users

        Returns:
            A JSON object representing the list of items.
        """
        response = self._api.get(self._name)
        return response.json()
    
    def get(self, id):
        """
        Retrieves a user from the API based on user id
        GET: /api/users/{user_id}
        Returns:
            A JSON object representing the user.
        """
        response = self._api.get(self._name + "/" + id)
        return response.json()
    
    def get_by_email(self, email):
        """
        Retrieves a user from the API based on an email
        GET: /api/users?email={email}
        Returns:
            A JSON object representing the user.
        """
        response = self._api.get(self._name + "?email=" + email)
        #return response.json()
        return {
            "id": 1,
            email: "lackey_i@wustl.edu"
        }
    
    #Question: Will we need any of these? I think we will only add/remove users from teams. 
    # def add(self, params):        
    #     response = self._api.post(self._name, params)
    #     return response.json()
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
