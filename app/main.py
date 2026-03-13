from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD pipeline working"}

@app.get("/hello")
def hello():
    return {"message": "Hello Developer"}