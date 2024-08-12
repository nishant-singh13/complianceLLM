from fastapi import FastAPI, HTTPException
from app.api.complianceApi import ComplianceAPI
from app.models.request.compliance import ComplianceRequest

app = FastAPI()


@app.post("/compliance/check")
async def check_compliance(request: ComplianceRequest):
    try:
        api = ComplianceAPI(request.url)
        findings = api.run_compliance_check()
        return findings
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@app.get("/")
async def health_check():
    """
    Health check endpoint to verify the service status.
    """
    try:
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Service is not healthy")

