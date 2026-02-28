from fastapi import FastAPI


from parser.database import create_tables

app = FastAPI(
    title="Wildberries Parser API",
    description="Parser of products from Wildberries"
)

@app.on_event()
async def on_startup():
    await create_tables()


@app.get("/")
async def root():
    return {
        "message": "Parser ready"
    }

