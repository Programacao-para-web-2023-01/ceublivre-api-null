from fastapi import FastAPI, Response
from uvicorn import run
from routers import frete, pedidos

app = FastAPI()

app.include_router(frete.router, tags=(["Frete"]), prefix="/v1")
app.include_router(pedidos.router, tags=(["Pedidos"]), prefix="/v1")


@app.get("/")
def get_root(response: Response):
    response.status_code = 200
    return {"message": "Service online"}


def main():
    run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
