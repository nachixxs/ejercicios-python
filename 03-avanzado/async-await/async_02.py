#Async-02 — Consultá la API pública de CoinGecko y traé el precio actual de Bitcoin, Ethereum y Litecoin de forma concurrente con asyncio.gather(). Imprimí los 3 resultados y el tiempo total que tardó.

import asyncio
import aiohttp
import time

async def obtener_precio(session, cripto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=usd"
    async with session.get(url) as response:
        data = await response.json()
        precio = data[cripto]['usd']
        print(f"El precio de {cripto.capitalize()} es: ${precio}")
        return precio

async def main():
    start_time = time.time()
    criptos = ["bitcoin", "ethereum", "litecoin"]
    
    async with aiohttp.ClientSession() as session:
        tareas = [obtener_precio(session, cripto) for cripto in criptos]
        await asyncio.gather(*tareas)
    
    end_time = time.time()
    print(f"Tiempo total: {end_time - start_time:.2f} segundos.")

asyncio.run(main())