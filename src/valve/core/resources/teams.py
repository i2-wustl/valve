class Teams:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "teams"

    def list(self):
        """
        Retrieves a list of teams from the API.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.get(self._name)
        return response.json()

    def get(self, id):
        """
        Retrieves a team from the API based on team ID.

        Args:
            id (str): The ID of the team to retrieve.

        Returns:
            dict: The JSON response from the API call.
        """
        endpoint = f"{self._name}/{id}"
        response = self._api.get(endpoint)
        return response.json()

    def get_by_name(self, name):
        """
        Retrieves a team from the API based on team name.

        Args:
            name (str): The name of the team to retrieve.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.get(self._name + "?name=" + name)
        return response.json()

    def add(self, team):
        """
        Adds a team.
        POST: /api/teams

        Args:
            params (dict): The parameters for the add request.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.post(self._name, json=team)
        return response.json()

    def add_to_team(self, team_id, user_id):      
        """
        Adds a user to a team.
        PUT: /api/teams/{team_id}/users/{user_id}

        Args:
            team_id (str): The ID of the team to add the user to.
            user_id (str): The ID of the user to add to the team.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.put(self._name + "/" + str(team_id) + "/users/", user_id)
        if response.status_code < 300:
            return response.json()
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
    #         return response.json()
    #     else:
    #         return response.text
                
    def remove_from_team(self, team_id, user_id):      
        """
        Remove a user from a team.
        DELETE: /api/teams/{team_id}/users/{user_id}

        Args:
            team_id (str): The ID of the team to add the user to.
            user_id (str): The ID of the user to add to the team.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.delete(self._name + "/" + str(team_id) + "/users/", user_id)
        if response.status_code < 300:
            return response.json()
        else:
            return response.text        

    #Question: will we need this? I don't think we will support deleting teams, but maybe we should disable them at this endpoint?
    def delete(self, team_id):
        """
        Deletes a team.
        DELETE: /api/teams/{team_id}

        Args:
            params (dict): The parameters for the delete request.

        Returns:
            dict: The JSON response from the API call.
        """
        response = self._api.delete(self._name, data={"teamID": team_id})
        if response.status_code < 300:
            return response.json()
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
    #         return response.json()
    #     else:
    #         return response.text