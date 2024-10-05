from os import environ

from dotenv import load_dotenv

from qiita import Qiita
from qiita.v2.models.create_item_request import CreateItemRequest
from qiita.v2.models.item_tag import ItemTag

load_dotenv(".env", verbose=True)

q = Qiita(access_token=environ["QIITA_API_ACCESS_TOKEN"])

res = q.create_item_with_http_info(
    CreateItemRequest(
        body="aaa",
        tags=[ItemTag(name="python", versions=[])],
        title="title",
        private=True,
        tweet=False,
        slide=True,
    )
)
print(f"{res.data=}")
