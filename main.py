from typing import Optional
from fastapi import FastAPI, Response,status
from pydantic import BaseModel
from random import randrange

app = FastAPI()

my_posts=[{"title":"title post 1","content":"content of post 1","id":1},
          {"title":"title post 2","content":"content of post 2","id":2},
          {"title":"title post 3","content":"content of post 3","id":3}]

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
    return {"data":my_posts}

@app.get("/posts/{id}")
def get_post_by_id(id:int,response:Response):
    for post in my_posts:
        if post["id"]==int(id):
            response.status_code=status.HTTP_200_OK
            return {"post":post}

        else:
            response.status_code=status.HTTP_404_NOT_FOUND
    # return {"message":"post not found"} # Return 200 ok status code not 404
    return {"message":f"Post with id {id} not found"}


@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.model_dump()
    post_dict["id"]= randrange(0,1000000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data":post_dict}