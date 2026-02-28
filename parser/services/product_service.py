from os import name

from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from parser.models import Product
from parser.database import get_db
from parser.schemas import WBProduct, WbProductResponse
from parser.wb_parser import WBParser

router = APIRouter(prefix="/product", tags=["product"])

@router.get('/{wb_id}')
async def parse_product(wb_id: int, db: AsyncSession = Depends(get_db)):
    async with WBParser() as parser:
        wb_product = await parser.get_product(wb_id)
        print(f"WB ответ: {wb_product}")
        if not wb_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товар не найден на WB")

        result = await db.execute(select(Product).where(Product.wb_id == wb_id))

        product = result.scalar_one_or_none()
        if not product:
            product = Product(
                wb_id=wb_id,
                name=wb_product.name,
                price=wb_product.price,
                price_old=wb_product.price.old
            )
        db.add(product)
        await db.commit()

        return {
            "wb_id": product.wb_id,
            "name": product.name,
            "price": f"{product.price:.2f} ₽",
            "price_old": f"{product.price_old:.2f} ₽" if product.price_old else None,
            "created_at": product.created_at.isoformat(),
            "updated_at": product.updated_at.isoformat()
        }