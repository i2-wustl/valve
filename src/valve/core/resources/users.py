from valve.core.api import create_client

__endpoint__ = "users"

def list():
    """
    Retrieves a list of items from the API.
    GET: /api/users

    Returns:
        A JSON object representing the list of items.
    """
    client = create_client()
    response = client.get(__endpoint__)
    return response


def get(id):
    """
    Retrieves a user from the API based on user id
    GET: /api/users/{user_id}
    Returns:
        A JSON object representing the user.
    """
    client = create_client()
    response = client.get(__endpoint__ + "/" + id)
    return response


def get_by_email(email):
    """
    Retrieves a user from the API based on an email
    GET: /api/users?email={email}
    Returns:
        A JSON object representing the user.
    """
    client = create_client()
    response = client.get(__endpoint__ + "?email=" + email)
    result = response
    result = {"id": 1, email: "lackey_i@wustl.edu"}
    return result


# Question: Will we need any of these? I think we will only add/remove users from teams.
# def add(self, params):
#     response = client.post(__endpoint__, params)
#     return response
# def delete(self, params):
#     client = self.get_client()
#     response = client.delete("", json=params, timeout=10)
#     client.handle_response(response)
#     return response
# def modify(self, params):
#     client = self.get_client()
#     response = client.put("", json=params, timeout=10)
#     client.handle_response(response)
#     return response
