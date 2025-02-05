from fastapi import FastAPI
 
app = FastAPI()
 
 
@app.get("/", description="A root endpoint", response_model=dict, response_description="A welcome message")
async def index() -> dict:
    return {"message": "Hello, world!"}