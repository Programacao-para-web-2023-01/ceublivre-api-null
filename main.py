from fastapi import FastAPI, Response
from uvicorn import run

app = FastAPI()

@app.get("/")
def get_root(response: Response):
    response.status_code = 200
    return {"message": "Service online"}


def main():
    run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
