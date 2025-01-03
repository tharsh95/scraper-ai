from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):
    url: HttpUrl

class ResponseModel(BaseModel):
    industry: str
    company_size: str
    location: str
