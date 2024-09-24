
# scope="00000003-0000-0000-c000-000000000000/.default"
#scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/.default"
# scope="2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default"
# scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/Databasin.API"
# scope="api://0f60d342-8fcc-4009-8a49-ab7760d896b2/Databasin.Hierarchies"

from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
import requests

credentials = DefaultAzureCredential(logging_enable=True,
    exclude_cli_credential=True,
    interactive_browser_tenant_id="4ccca3b5-71cd-4e6d-974b-4d9beb96c6d6",
    interactive_browser_client_id="0f60d342-8fcc-4009-8a49-ab7760d896b2",
    exclude_interactive_browser_credential=False)

credentials = InteractiveBrowserCredential(logging_enable=True,
    exclude_cli_credential=True,
    tenant_id="4ccca3b5-71cd-4e6d-974b-4d9beb96c6d6",
    client_id="0f60d342-8fcc-4009-8a49-ab7760d896b2")

scope="api://da78a353-fd13-4707-b327-4c91f0f2a7d1/Databasin.Hierarchies"
access_token = credentials.get_token(scope)


root_url = "https://api.databasin.wustl.edu/api"
endpoint_url = f"{root_url}/connector?institutionID=4&internalID=uJEj8d"
headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer: {access_token.token}"
        }
result = requests.get(endpoint_url, headers=headers, verify=False)

print(result.text)