from typing import Any, Optional

from pydantic import BaseModel, StrictStr

from qiita.v2.api.team_api import TeamApi
from qiita.v2.api.user_api import UserApi
from qiita.v2.api_client import ApiClient
from qiita.v2.configuration import Configuration


class Qiita(BaseModel, UserApi, TeamApi):
    class Config:
        arbitrary_types_allowed = True

    access_token: StrictStr
    api_client: Optional[ApiClient] = None

    def model_post_init(self, __context: Any) -> None:
        c = ApiClient(Configuration(access_token=self.access_token))
        UserApi.__init__(self, c)
        TeamApi.__init__(self, c)
