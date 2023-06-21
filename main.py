from fastapi import FastAPI, Response, HTTPException
from uvicorn import run
from routers import frete, pedidos, transportadoras
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Import middlewares
from middlewares.error import catch_exceptions_middleware
from middlewares.auth import AuthMiddleware


app = FastAPI()

# Middlewares
app.add_middleware(AuthMiddleware)
app.middleware('http')(catch_exceptions_middleware)

origins = [
    "https://localhost:3000",
    "https://localhost",
    "http://localhost:3000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(frete.router, tags=(["Frete"]), prefix="/frete")
app.include_router(pedidos.router, tags=(["Pedidos"]), prefix="/pedidos")
app.include_router(transportadoras.router, tags=(["Transportadoras"]), prefix="/transportadora")


# show Authorization header in docs
app.openapi_schema = app.openapi()
app.openapi_schema["components"]["securitySchemes"] = {
    "apiKeyAuth": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
    }
}
app.openapi_schema["security"] = [
    {
        "apiKeyAuth": ["*"]
    }
]


@app.get("/")
def get_root(response: Response):
    response.status_code = 200
    return {"message": "Service online"}


def main():
    run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()
