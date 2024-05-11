# coding: utf-8

"""
    Qiita API v2

    ## 概要  このドキュメントではQiita API v2の仕様について説明します。  ## リクエスト  APIとの全ての通信にはHTTPSプロトコルを利用します。アクセス先のホストには、Qiitaのデータを利用する場合には `qiita.com` を利用し、Qiita Teamのデータを利用する場合には `*.qiita.com` を利用します ( `*` には所属しているTeamのIDが入ります)。  ## パラメータ  API v2へのリクエストには、GET、POST、PUT、PATCH、DELETEの5種類のHTTPメソッドを利用します。多くのAPIへのリクエストにはパラメータを含められますが、GETリクエストにパラメータを含める場合にはURIクエリを利用し、それ以外の場合にはリクエストボディを利用します。パラメータには、ページネーション用途など任意で渡すものと、投稿時の本文など必須のものが存在します。APIドキュメントには、各APIごとに送信可能なパラメータが記載されています。  ## 利用制限  認証している状態ではユーザーごとに1時間に1000回まで、認証していない状態ではIPアドレスごとに1時間に60回までリクエストを受け付けます。  ## シングルサインオンを利用中のチームについて  シングルサインオンによる認証のみを許可しているQiita Teamのチームでは、セキュリティ上の理由から、チーム別アクセストークンでのみAPIを利用したアクセスが可能です。  ## ステータスコード  200、201、204、400、401、403、404、500の8種類のステータスコードを利用します。GETまたはPATCHリクエストに対しては200を、POSTリクエストに対しては201を、PUTまたはDELETEリクエストに対しては204を返します。但し、エラーが起きた場合にはその他のステータスコードの中から適切なものを返します。  ## データ形式  APIとのデータの送受信にはJSONを利用します。JSONをリクエストボディに含める場合、リクエストのContent-Typeヘッダにapplication/jsonを指定してください。但し、GETリクエストにバラメータを含める場合にはURIクエリを利用します。また、PUTリクエストまたはDELETEリクエストに対してはレスポンスボディが返却されません。日時を表現する場合には、[ISO 8601](http://ja.wikipedia.org/wiki/ISO_8601) 形式の文字列を利用します。  ``` GET /api/v2/items?page=1&per_page=20 HTTP/1.1 ```  ## エラーレスポンス  エラーが発生した場合、エラーを表現するオブジェクトを含んだエラーレスポンスが返却されます。このオブジェクトには、エラーの内容を説明するmessageプロパティと、エラーの種類を表すtypeプロパティで構成されます。typeプロパティはエラーの種類ごとに一意な文字列で、`^[a-z0-9_]+$` というパターンで表現できます。  ``` {   \"message\": \"Not found\",   \"type\": \"not_found\" } ```  ## ページネーション  一部の配列を返すAPIでは、全ての要素を一度に返すようにはなっておらず、代わりにページを指定できるようになっています。これらのAPIには、1から始まるページ番号を表すpageパラメータと、1ページあたりに含まれる要素数を表すper_pageパラメータを指定することができます。pageの初期値は1、pageの最大値は100に設定されています。また、per_pageの初期値は20、per_pageの最大値は100に設定されています。  ページを指定できるAPIでは、[Linkヘッダ](http://tools.ietf.org/html/rfc5988) を含んだレスポンスを返します。Linkヘッダには、最初のページと最後のページへのリンクに加え、存在する場合には次のページと前のページへのリンクが含まれます。個々のリンクにはそれぞれ、first、last、next、prevという値を含んだrel属性が紐付けられます。  ``` Link: <https://qiita.com/api/v2/users?page=1>; rel=\"first\",       <https://qiita.com/api/v2/users?page=1>; rel=\"prev\",       <https://qiita.com/api/v2/users?page=3>; rel=\"next\",       <https://qiita.com/api/v2/users?page=6>; rel=\"last\" ```  また、ページを指定できるAPIでは、要素の合計数が `Total-Count` レスポンスヘッダに含まれます。  ``` Total-Count: 6 ```  ## JSON Schema  Qiita API v2では、APIのインターフェースを定義したJSON-Schemaを提供しています。このスキーマでは、APIでどのようなリソースが提供されているか、それらはどのようなプロパティを持っているか、それらがどのように表現されるか、及びどのような操作が提供されているかといった事柄が定義されています。スキーマには、次のURLでアクセスできます。  - https://qiita.com/api/v2/schema - https://qiita.com/api/v2/schema?locale=en - https://qiita.com/api/v2/schema?locale=ja 

    The version of the OpenAPI document: 0.0.1
    Contact: admin@okj.info
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class UpdateCommentRequest(BaseModel):
    """
    UpdateCommentRequest
    """ # noqa: E501
    body: StrictStr = Field(description="コメントの内容を表すMarkdown形式の文字列")
    __properties: ClassVar[List[str]] = ["body"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateCommentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateCommentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body")
        })
        return _obj


