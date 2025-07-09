from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def test():
    response = {"message": "Up and running!!!!!!!!!!"}
    return response