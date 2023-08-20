from http_client import HttpClient
from azdo_url_builder import AzdoUrlBuilder


class AzdoHttpClient:
    def __init__(self):
        self.client = HttpClient()
        self.url_builder = AzdoUrlBuilder()

    async def get_workitem_detail(self, work_item_id: int):
        url = self.url_builder.get_workitem_detail_url(work_item_id)
        print(url)
        return await self.client.get(url=url)
