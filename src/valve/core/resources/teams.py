from valve.core.api import create_client
import valve.core.resources.users as u

__endpoint__ = "teams"

def list_teams():
    """
    Retrieves a list of teams from the API.

    Returns:
        dict: The JSON response from the API call.
    """
    client = create_client()
    response = client.get(__endpoint__)        

    return response

def get_team_by_id( id):
    """
    Retrieves a team from the API based on team ID.

    Args:
        id (str): The ID of the team to retrieve.

    Returns:
        dict: The JSON response from the API call.
    """
    endpoint = f"{__endpoint__}/{id}"
    client = create_client()
    response = client.get(endpoint)
    return response

def get_team_by_name(name):
    """
    Retrieves a team from the API based on team name.

    Args:
        name (str): The name of the team to retrieve.

    Returns:
        dict: The JSON response from the API call.
    """
    client = create_client()
    response = client.get(__endpoint__ + "?name=" + name)
    return response

def add_team(team):
    """
    Adds a team.
    POST: /api/teams

    Args:
        params (dict): The parameters for the add request.

    Returns:
        dict: The JSON response from the API call.
    """
    client = create_client()
    response = client.post(__endpoint__, json=team)
    return response

def add_to_team(team_id, email):      
    """
    Adds a user to a team.
    PUT: /api/teams/{team_id}/users/{user_id}

    Args:
        team_id (str): The ID of the team to add the user to.
        user_id (str): The ID of the user to add to the team.

    Returns:
        dict: The JSON response from the API call.
    """
    user_data = u.get_by_email(email)
    
    client = create_client()
    response = client.put(__endpoint__ + "/" + str(team_id) + "/users/", user_data["id"])
    if response.status_code < 300:
        return response
    else:
        return response.text
    
# def add_team_to_datasource(self, team_id, datasource_group_id):      
#     """
#     Adds a user to a team.
#     PUT: /api/teams/{team_id}/users/{user_id}

#     Args:
#         team_id (str): The ID of the team to add the user to.
#         user_id (str): The ID of the user to add to the team.

#     Returns:
#         dict: The JSON response from the API call.
#     """
#     response = self._api.put(self._name + "/" + str(team_id) + "/users/", user_id)
#     if response.status_code < 300:
#         return response
#     else:
#         return response.text
            
def remove_from_team(team_id, user_id):      
    """
    Remove a user from a team.
    DELETE: /api/teams/{team_id}/users/{user_id}

    Args:
        team_id (str): The ID of the team to add the user to.
        user_id (str): The ID of the user to add to the team.

    Returns:
        dict: The JSON response from the API call.
    """
    client = create_client()
    response = client.delete(__endpoint__ + "/" + str(team_id) + "/users/", user_id)
    if response.status_code < 300:
        return response
    else:
        return response.text

#Question: will we need this? I don't think we will support deleting teams, but maybe we should disable them at this endpoint?
def delete( team_id):
    """
    Deletes a team.
    DELETE: /api/teams/{team_id}

    Args:
        params (dict): The parameters for the delete request.

    Returns:
        dict: The JSON response from the API call.
    """
    client = create_client()
    response = client.delete(__endpoint__, data={"teamID": team_id})
    if response.status_code < 300:
        return response
    else:
        return response.text

## Question: will we need this? I don't think we will support updating teams
# def modify(self, params):
#     """
#     Modifies a team.
#     PUT: /api/teams/{team_id}

#     Args:
#         params (dict): The parameters for the modify request.

#     Returns:
#         dict: The JSON response from the API call.
#     """
#     response = self._api.put(self._name + "/" + str(params["team_id"]), params)
#     if response.status_code < 300:
#         return response
#     else:
#         return response.text
#     





        
      

