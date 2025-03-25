import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping", name="view")
def index():
    """
    Тестовая страница
    """
    return {
        "message": "pong"
    }


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)