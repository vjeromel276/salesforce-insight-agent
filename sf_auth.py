from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

load_dotenv()

def connect_salesforce():
    try:
        sf = Salesforce(
            username=os.getenv("SF_USERNAME"),
            password=os.getenv("SF_PASSWORD"),
            security_token=os.getenv("SF_SECURITY_TOKEN"),
            domain=os.getenv("SF_DOMAIN", "test")
        )
        print("✅ Logged in to Salesforce")
        return sf
    except Exception as e:
        print("❌ Salesforce login failed:", e)
        raise
sf = connect_salesforce()