from fastapi import FastAPI, Response
from uvicorn import run
from routers import correios_api

app = FastAPI()

app.include_router(correios_api.router, tags=(["Correios"]), prefix="/v1")

@app.get("/")
def get_root(response: Response):
    response.status_code = 200
    return {"message": "Service online"}


def main():
    run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
