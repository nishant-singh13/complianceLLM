import os
from fastapi import HTTPException
from app.services.web import Web
from app.services.compliance import Compliance

# Read the COMPLIANCE_URL from environment variables
COMPLIANCE_URL = os.getenv("COMPLIANCE_URL", "https://stripe.com/docs/treasury/marketing-treasury")


class ComplianceAPI:
    def __init__(self, url: str):
        self.url = url
        self.compliance_policy = COMPLIANCE_URL

    def run_compliance_check(self) -> dict:
        try:
            web = Web(self.url)
            # fetching URL details
            web.fetch()
            text_content = web.extract_text()
            compliance = Compliance(self.compliance_policy)
            findings = compliance.check_compliance(text_content)

            return {"findings": findings}
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=f"Input validation error: {ve}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while processing the request: {e}")




