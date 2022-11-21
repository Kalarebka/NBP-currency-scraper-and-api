from fastapi import FastAPI

from .routers import currency, table

app = FastAPI(debug=True)


app.include_router(currency.router)
app.include_router(table.router)


@app.get("/")
async def index() -> dict:
    return {"app status": "working"}