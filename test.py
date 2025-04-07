import simple_salesforce as sf
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the Salesforce credentials
sf_username = os.getenv('username')
sf_password = os.getenv('password')
sf_security_token = os.getenv('token')
sf_domain = os.getenv('domain')

# Print to verify (remove these in production!)
print("Username:", sf_username)
print("Password:", sf_password)
print("Security Token:", sf_security_token)
print("Domain:", sf_domain)

# Connect to Salesforce
sf = sf.Salesforce(
    username=sf_username,
    password=sf_password,
    security_token=sf_security_token,
    domain=sf_domain
)
print("✅ Logged in to Salesforce {sf.sf_instance}")
