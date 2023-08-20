from http_client import HttpClient
from azdo_url_builder import AzdoUrlBuilder
from secret_provider import SecretProvider


class AzdoHttpClient:
    def __init__(self):
        self.client = HttpClient()
        self.url_builder = AzdoUrlBuilder()
        self._secret_provider = SecretProvider()

    async def get_workitem_detail(self, work_item_id: int):
        url = self.url_builder.get_workitem_detail_url(work_item_id)
        print(url)
        return await self.client.get(url=url, headers=self.build_headers())

    def build_headers(self) -> dict[str, str]:
        return {"Authorization": f"Basic {self._secret_provider.get_secret('API_KEY')}"}
