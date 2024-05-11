# coding: utf-8

"""
    Qiita API v2

    ## 概要  このドキュメントではQiita API v2の仕様について説明します。  ## リクエスト  APIとの全ての通信にはHTTPSプロトコルを利用します。アクセス先のホストには、Qiitaのデータを利用する場合には `qiita.com` を利用し、Qiita Teamのデータを利用する場合には `*.qiita.com` を利用します ( `*` には所属しているTeamのIDが入ります)。  ## パラメータ  API v2へのリクエストには、GET、POST、PUT、PATCH、DELETEの5種類のHTTPメソッドを利用します。多くのAPIへのリクエストにはパラメータを含められますが、GETリクエストにパラメータを含める場合にはURIクエリを利用し、それ以外の場合にはリクエストボディを利用します。パラメータには、ページネーション用途など任意で渡すものと、投稿時の本文など必須のものが存在します。APIドキュメントには、各APIごとに送信可能なパラメータが記載されています。  ## 利用制限  認証している状態ではユーザーごとに1時間に1000回まで、認証していない状態ではIPアドレスごとに1時間に60回までリクエストを受け付けます。  ## シングルサインオンを利用中のチームについて  シングルサインオンによる認証のみを許可しているQiita Teamのチームでは、セキュリティ上の理由から、チーム別アクセストークンでのみAPIを利用したアクセスが可能です。  ## ステータスコード  200、201、204、400、401、403、404、500の8種類のステータスコードを利用します。GETまたはPATCHリクエストに対しては200を、POSTリクエストに対しては201を、PUTまたはDELETEリクエストに対しては204を返します。但し、エラーが起きた場合にはその他のステータスコードの中から適切なものを返します。  ## データ形式  APIとのデータの送受信にはJSONを利用します。JSONをリクエストボディに含める場合、リクエストのContent-Typeヘッダにapplication/jsonを指定してください。但し、GETリクエストにバラメータを含める場合にはURIクエリを利用します。また、PUTリクエストまたはDELETEリクエストに対してはレスポンスボディが返却されません。日時を表現する場合には、[ISO 8601](http://ja.wikipedia.org/wiki/ISO_8601) 形式の文字列を利用します。  ``` GET /api/v2/items?page=1&per_page=20 HTTP/1.1 ```  ## エラーレスポンス  エラーが発生した場合、エラーを表現するオブジェクトを含んだエラーレスポンスが返却されます。このオブジェクトには、エラーの内容を説明するmessageプロパティと、エラーの種類を表すtypeプロパティで構成されます。typeプロパティはエラーの種類ごとに一意な文字列で、`^[a-z0-9_]+$` というパターンで表現できます。  ``` {   \"message\": \"Not found\",   \"type\": \"not_found\" } ```  ## ページネーション  一部の配列を返すAPIでは、全ての要素を一度に返すようにはなっておらず、代わりにページを指定できるようになっています。これらのAPIには、1から始まるページ番号を表すpageパラメータと、1ページあたりに含まれる要素数を表すper_pageパラメータを指定することができます。pageの初期値は1、pageの最大値は100に設定されています。また、per_pageの初期値は20、per_pageの最大値は100に設定されています。  ページを指定できるAPIでは、[Linkヘッダ](http://tools.ietf.org/html/rfc5988) を含んだレスポンスを返します。Linkヘッダには、最初のページと最後のページへのリンクに加え、存在する場合には次のページと前のページへのリンクが含まれます。個々のリンクにはそれぞれ、first、last、next、prevという値を含んだrel属性が紐付けられます。  ``` Link: <https://qiita.com/api/v2/users?page=1>; rel=\"first\",       <https://qiita.com/api/v2/users?page=1>; rel=\"prev\",       <https://qiita.com/api/v2/users?page=3>; rel=\"next\",       <https://qiita.com/api/v2/users?page=6>; rel=\"last\" ```  また、ページを指定できるAPIでは、要素の合計数が `Total-Count` レスポンスヘッダに含まれます。  ``` Total-Count: 6 ```  ## JSON Schema  Qiita API v2では、APIのインターフェースを定義したJSON-Schemaを提供しています。このスキーマでは、APIでどのようなリソースが提供されているか、それらはどのようなプロパティを持っているか、それらがどのように表現されるか、及びどのような操作が提供されているかといった事柄が定義されています。スキーマには、次のURLでアクセスできます。  - https://qiita.com/api/v2/schema - https://qiita.com/api/v2/schema?locale=en - https://qiita.com/api/v2/schema?locale=ja 

    The version of the OpenAPI document: 0.0.1
    Contact: admin@okj.info
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qiita.v2.models.like_history import LikeHistory

class TestLikeHistory(unittest.TestCase):
    """LikeHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LikeHistory:
        """Test LikeHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LikeHistory`
        """
        model = LikeHistory()
        if include_optional:
            return LikeHistory(
                created_at = '',
                user = qiita.v2.models.user.User(
                    description = 'Hello, world.', 
                    facebook_id = 'qiita', 
                    followees_count = 100, 
                    followers_count = 200, 
                    github_login_name = 'qiitan', 
                    id = 'qiita', 
                    items_count = 300, 
                    linkedin_id = 'qiita', 
                    location = 'Tokyo, Japan', 
                    name = 'Qiita キータ', 
                    organization = 'Qiita Inc.', 
                    permanent_id = 1, 
                    profile_image_url = 'https://s3-ap-northeast-1.amazonaws.com/qiita-image-store/0/88/ccf90b557a406157dbb9d2d7e543dae384dbb561/large.png?1575443439', 
                    team_only = True, 
                    twitter_screen_name = 'qiita', 
                    website_url = 'https://qiita.com', )
            )
        else:
            return LikeHistory(
                created_at = '',
                user = qiita.v2.models.user.User(
                    description = 'Hello, world.', 
                    facebook_id = 'qiita', 
                    followees_count = 100, 
                    followers_count = 200, 
                    github_login_name = 'qiitan', 
                    id = 'qiita', 
                    items_count = 300, 
                    linkedin_id = 'qiita', 
                    location = 'Tokyo, Japan', 
                    name = 'Qiita キータ', 
                    organization = 'Qiita Inc.', 
                    permanent_id = 1, 
                    profile_image_url = 'https://s3-ap-northeast-1.amazonaws.com/qiita-image-store/0/88/ccf90b557a406157dbb9d2d7e543dae384dbb561/large.png?1575443439', 
                    team_only = True, 
                    twitter_screen_name = 'qiita', 
                    website_url = 'https://qiita.com', ),
        )
        """

    def testLikeHistory(self):
        """Test LikeHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
