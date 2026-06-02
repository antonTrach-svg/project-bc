import uvicorn
from fastapi import FastAPI

from tasks.router import router as task_router
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

...
app.include_router(task_router)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    completed: bool = False

@app.post("/tasks", status_code=201)
def create_task(task: Task):

@app.delete("/tasks/{item_id}", status_code=204)
def delete_task(item_id: int):
    return None