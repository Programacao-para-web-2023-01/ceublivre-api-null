from fastapi import FastAPI, Response
from uvicorn import run
from routers import frete, pedidos, transportadoras

app = FastAPI()

app.include_router(frete.router, tags=(["Frete"]), prefix="/frete")
app.include_router(pedidos.router, tags=(["Pedidos"]), prefix="/pedido")
app.include_router(transportadoras.router, tags=(["Transportadoras"]), prefix="/transportadora")


@app.get("/")
def get_root(response: Response):
    response.status_code = 200
    return {"message": "Service online"}


def main():
    run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
