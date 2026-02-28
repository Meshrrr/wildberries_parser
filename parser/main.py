from fastapi import FastAPI


from parser.database import create_tables
from parser.services.product_service import router as product_router

app = FastAPI(
    title="Wildberries Parser API",
    description="Parser of products from Wildberries"
)


app.include_router(product_router

                   )
@app.on_event("startup")
async def on_startup():
    await create_tables()


@app.get("/")
async def root():
    return {
        "message": "Parser ready"
    }

