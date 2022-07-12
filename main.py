from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/test")
def test():
    return {"message": "test"}

@app.post("/createposts")
def create_posts(post: Post):
    return {"message": f"{post}"}