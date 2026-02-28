import aiohttp
import json

from typing import Dict, Any, Optional


from parser.schemas import WBProduct, WbProductResponse

class WBParser:
    BASE_URL = "https://card.wb.ru/cards/detail"

    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def get_product(self, wb_id: int) -> Optional[WBProduct]:
        params = {
            'appType': 1,
            'curr': 'rub',
            'dest': -1257786,  # Москва
            'spp': 0,
            'nm': wb_id
        }

        try:
            async with self.session.get(self.BASE_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    product_data = data.get('data', {}).get('products', [{}])[0]

                    return WBProduct(
                        id=wb_id,
                        name=product_data.get('name'),
                        price=product_data.get('priceU', 0),
                        base_price=product_data.get('salePriceU')
                    )
        except Exception as exc:
            print(f"Ошибка при парсинге {wb_id}: {exc}")

            return None
