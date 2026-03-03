import pytest
import aiohttp
from unittest.mock import patch, AsyncMock, MagicMock

async def obtener_precio_bitcoin() -> float:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd") as response:
            data = await response.json()
            return data["bitcoin"]["usd"]

@pytest.mark.asyncio
async def test_obtener_precio_bitcoin():
    mock_response = AsyncMock()
    mock_response.json.return_value = {"bitcoin": {"usd": 50000.0}}
    
    mock_session = MagicMock()
    mock_session.get.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.get.return_value.__aexit__ = AsyncMock(return_value=False)
    
    with patch("aiohttp.ClientSession") as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
        
        resultado = await obtener_precio_bitcoin()
        assert resultado == 50000.0