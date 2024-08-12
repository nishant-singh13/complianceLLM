from pydantic import BaseModel, HttpUrl


class ComplianceRequest(BaseModel):
    url: HttpUrl

