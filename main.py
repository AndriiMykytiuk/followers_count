from pydantic import BaseModel
from fastapi import FastAPI, Response, HTTPException
import json
from decouple import config
from instagram import Instagram
from tiktok import TikTok
from twitch import Twitch
from twitter import Twitter


class SocialMedia(BaseModel):
    name: str
    username: str
    secret: str


app = FastAPI()


@app.post("/")
async def get_followers_count(social_media: SocialMedia):
    if social_media.secret != config("SECRET"):
        raise HTTPException(status_code=401, detail="unauthorized_access")

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
    elif social_media.name == 'tiktok':
        tiktok = TikTok()
        followers = tiktok.get_followers_count(social_media.username)
        if followers:
            data = {'username': social_media.username,
                    'name': social_media.name,
                    'followers': followers}
            json_str = json.dumps(data, indent=4, default=str)
            return Response(content=json_str, media_type='application/json')
        else:
            raise HTTPException(status_code=404, detail="user_not_found")
    elif social_media.name == 'twitch':
        twitch = Twitch()
        followers = twitch.get_followers_count(social_media.username)
        if followers:
            data = {'username': social_media.username,
                    'name': social_media.name,
                    'followers': followers}
            json_str = json.dumps(data, indent=4, default=str)
            return Response(content=json_str, media_type='application/json')
        else:
            raise HTTPException(status_code=404, detail="user_not_found")
    elif social_media.name == 'twitter':
        twitter = Twitter()
        followers = twitter.get_followers_count(social_media.username)
        if followers:
            data = {'username': social_media.username,
                    'name': social_media.name,
                    'followers': followers}
            json_str = json.dumps(data, indent=4, default=str)
            return Response(content=json_str, media_type='application/json')
        else:
            raise HTTPException(status_code=404, detail="user_not_found")


