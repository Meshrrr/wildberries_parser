from fastapi import FastAPI

app = FastAPI(
    title="Wildberries Parser API",
    description="Parser of products from Wildberries"
)

@app.get("/")
async def root():
    return {
        "message": "Parser ready"
    }

