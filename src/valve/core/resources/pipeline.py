def initialize(api):
    return Pipeline(api)

class Pipeline:
    def __init__(self, api) -> None:
        self._api = api
        self._name = "pipeline"

    def list(self):
        """
        Retrieves a list of pipelines from the API.
        GET: /api/pipelines

        Returns:
            A JSON object representing the existing list of pipelines.
        """
        response = self._api.get(self._name)
        return response.json()

    def add(self, pipeline):
        """
        Creates a new pipeline.
        POST: /api/pipelines

        Args:
            pipeline (Pipeline): The new pipeline data

        Returns:
            A JSON object representing the new pipeline.
        """
        response = self._api.put(self._name, data=pipeline)
        return response.json()

    def delete(self, pipeline_id):
        """
        Adds a connector.
        DELETE: /api/connectors
        
        Returns:
            A JSON object representing the details associated with the new connector.
        """
        
        response = self._api.delete(self._name, data={"pipelineId": pipeline_id})
        return response.json()

    def modify(self,  pipeline):
        """
        Modifies a pipeline.
        PUT: /api/pipelines

        Args:
            pipeline (Pipeline): The updated pipeline data

        Returns:
            A JSON object representing the updated pipeline.
        """
        response = self._api.put(self._name, data=pipeline)
        return response.json()
