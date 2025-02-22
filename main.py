from fastapi import FastAPI, HTTPException
from typing import get_args
import curl_cffi.requests as requests
from curl_cffi.requests import BrowserTypeLiteral
from pydantic import BaseModel
from typing import Dict, Optional , Any

app = FastAPI()

class RequestPayload(BaseModel):
    method: str
    url: str
    params: Optional[Dict[str, str]] = None
    headers: Optional[Dict[str, str]] = None
    data: Optional[Dict[str, Any]] = None 
    cookies: Optional[Dict[str, str]] = None
    impersonate: Optional[str] = None
    proxies: Optional[Dict[str, str]] = None
    
BROWSER_TYPES = set(get_args(BrowserTypeLiteral))    

def is_valid_browser_type(browser : str) -> bool:
    return browser in BROWSER_TYPES

@app.post("/")
def handle_request(payload : RequestPayload):
    try:
        method = payload.method.upper()
        
        if method not in {"GET" , "POST" , "DELETE" , "PUT"}:
            raise HTTPException(status_code=400 , detail="Unsupported HTTP method")
        
        if not is_valid_browser_type(payload.impersonate):
            raise HTTPException(status_code=400 , detail="Unsupported impersonate")
        
        response = requests.request(
            method=payload.method,
            url=payload.url,
            params=payload.params,
            headers=payload.headers,
            cookies=payload.cookies,
            json=payload.data if method in {"POST" , "PUT"} else None,
            impersonate=payload.impersonate,
            proxies=payload.proxies
        )
        
        return {
            "status_code" : response.status_code,
            "headers" : response.headers,
            "data" : response.json() if response.headers["Content-Type"] == "application/json" else response.text,
            "cookies" : response.cookies
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))      