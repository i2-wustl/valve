from pprint import pprint
from dotenv import load_dotenv
import valve.core.api as api
import valve.core.auth

# Load environment variables from .env file
load_dotenv()

# Log in using envrionment variables
credentials = valve.core.auth.login()

# Initialize API
client = api.API().init(credentials=credentials)   

# List users
users = client.users.list()

pprint(users)