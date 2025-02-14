# FastAPI cURL-CFFI Proxy

This FastAPI application provides a proxy service using `curl-cffi`, allowing users to send HTTP requests (GET, POST, DELETE, PUT) with support for parameters, headers, cookies, proxies, and browser impersonation.

## Features
- **Supports multiple HTTP methods**: GET, POST, DELETE, and PUT.
- **cURL impersonation**: Mimic different browsers using `curl-cffi`'s `impersonate` option.
- **Supports proxies**: Route requests through specified proxies.
- **Handles JSON and text responses**: Automatically detects and parses JSON responses.

## Requirements
- Python 3.8+
- FastAPI
- curl-cffi
- Uvicorn
- Gunicorn (for running the server)

## Installation
```sh
pip install -r requirements.txt
```

## Running the Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoint
### Handle HTTP Requests
**Endpoint:**
```http
POST /
```
**Request Body:**
```json
{
  "method": "GET",
  "url": "https://example.com",
  "params": {"key": "value"},
  "headers": {"User-Agent": "MyApp"},
  "cookies": {"session": "abcd1234"},
  "data": {"field": "value"},
  "impersonate": "chrome",
  "proxies": {"http": "http://proxy.example.com:8080"}
}
```

**Example Request:**
```sh
curl -X POST "http://127.0.0.1:8000/" \
     -H "Content-Type: application/json" \
     -d '{"method": "GET", "url": "https://example.com"}'
```

**Response Format:**
```json
{
  "status_code": 200,
  "headers": {"Content-Type": "application/json"},
  "data": {"key": "value"},
  "cookies": {"session": "abcd1234"}
}
```

## Docker Support
### Build Your Own Image
You can build your own Docker image using the provided DOckerfile:
```sh
docker build -t fastapi-curl-proxy .
```
### Run the Container
```sh
docker run -p 8000:8000 fastapi-curl-proxy
```

### Pull from Repository
Alternatively, you can pull the existing image from the repository:
```sh
docker pull yenoluna/fastapi-curl-proxy
```

## License
This project is licensed under the MIT License.

