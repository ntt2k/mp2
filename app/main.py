from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Number(BaseModel):
    num: int


@app.get("/")
def read_num():
    with open("num.txt", "r") as f:
        num = int(f.read())
    return {"num": num}


@app.post("/")
def save_num(n: Number):
    with open("num.txt", "w") as f:
        f.write(str(n.num))
    return str(n.num)
