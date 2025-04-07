from simple_salesforce import Salesforce
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the Salesforce credentials
sf_username = os.getenv("username")
sf_password = os.getenv("password")
sf_token = os.getenv("security_token")
sf_domain = os.getenv("domain")

# Configure logging
logging.basicConfig(
    filename="salesforce_download.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Attempt to log in to Salesforce
try:
    sf = Salesforce(
        username=sf_username,
        password=sf_password,
        security_token=sf_token,
        domain=sf_domain,
    )
    print("✅ Logged in to Salesforce")
    logging.info("Logged in to Salesforce")
except Exception as e:
    print("❌ Error logging in to Salesforce:", e)
    logging.error(f"Error logging in to Salesforce: {e}")
    exit()
