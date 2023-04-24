from pydantic import BaseModel
from fastapi import FastAPI, Response, HTTPException
import json

from instagram import Instagram


class SocialMedia(BaseModel):
    name: str
    username: str


app = FastAPI()


@app.post("/")
async def get_followers_count(social_media: SocialMedia):
    followers = None
    if social_media.name == 'instagram':
        insta = Instagram()
        followers = insta.get_followers(social_media.username)
    if followers:
        data = {'username': social_media.username,
                'name': social_media.name,
                'followers': followers}
        json_str = json.dumps(data, indent=4, default=str)
        return Response(content=json_str, media_type='application/json')
    else:
        raise HTTPException(status_code=404, detail="user_not_found")
