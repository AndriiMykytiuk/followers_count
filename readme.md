# Tech Stack

Docker, Python 3.7, FastAPI, Docker, Selenium, requests

# Supported platforms:
Instagram, TikTok, Twitch, Twitter

## Installation

Log in to Instagram with Firefox and export the cookies: https://instaloader.github.io/troubleshooting.html

```bash
docker-compose up --build -d

```

## Usage
Once you have the container up and running,
in order to get the followers count make the POST request with the payload

```
{
    "name": social_media_name,
    "username": username,
    "secret": SECRET
}

```
`social_media_name` option can be "instagram", "twitch", "tiktok" or "twitter"

You will receive the response like:
```
{
    "username": "violetroad",
    "name": "instagram",
    "followers": 10510
}
```

