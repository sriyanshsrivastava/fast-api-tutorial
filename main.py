from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating:Optional[int]=None


@app.get("/")
def root():
    return{"message":"Hello world!"}

@app.get("/posts")
def get_post():
    return {"Data":"this is your post"}

@app.post("/createposts")
def create_posts(post:Post):
    print(post)
    print(post.model_dump())
    return {"data":post}