import httpx
from typing import Optional


class HttpClient:
    async def get(self, url: str, headers: Optional[dict[str, str]] = None):
        url: str = self.build_url(url)
        async with self.create_client() as client:
            return await client.get(url, headers=headers)

    def build_url(self, url: str) -> str:
        return url

    def create_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(verify=False)
