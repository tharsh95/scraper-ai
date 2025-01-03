from fastapi import FastAPI, HTTPException, Header, Depends
from app.models import URLRequest, ResponseModel
from app.scraper import scrape_website
from app.utils import verify_secret_key

app = FastAPI()

SECRET_KEY = "your-secret-key"

@app.post("/scrape", response_model=ResponseModel)
async def scrape(
    url_request: URLRequest, 
    authorization: str = Header(..., alias="Authorization"),
    is_authenticated: bool = Depends(verify_secret_key(SECRET_KEY))
):
    try:
        result = scrape_website(url_request.url)
        return ResponseModel(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
