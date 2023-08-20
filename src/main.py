from fastapi import FastAPI
from data_generator import DataGenerator
from azdo_http_client import AzdoHttpClient
import asyncio

app = FastAPI()
data = DataGenerator()
azdo_http_client = AzdoHttpClient()


@app.get("/workitems/{work_item_id}")
async def read_root(work_item_id: int):
    resp = await azdo_http_client.get_work_item(work_item_id)
    return resp.text


if __name__ == "__main__":

    async def main():
        result = await azdo_http_client.get_workitem_detail(1)
        print("Async task result:", result.text)

    asyncio.run(main())
