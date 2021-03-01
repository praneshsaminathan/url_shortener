#URL Shortener

URL: **http://127.0.0.1:8000/api/v1/url-shorten/**
type: **POST**
Body: **URL **

Response: {
    "full_url": "https://www.linkedin.com/feed/",
    "hash_url": "04ee8b6039",
    "clicks": 0
}

URL: **http://127.0.0.1:8000/api/v1/full-url/--hash--/**
type: **GET**

Response: {
    "full_url": "https://www.linkedin.com/feed/",
    "hash_url": "04ee8b6039",
    "clicks": 0
}


