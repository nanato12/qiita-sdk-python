# qiita-sdk-python

## Requirements

Python 3.8+

## Installation

```sh
$ pip install qiita-sdk
```

## Getting Started

```python
from os import environ

from qiita import Qiita
from qiita.v2.models.create_item_request import CreateItemRequest
from qiita.v2.models.item_tag import ItemTag

# Instantiate the Qiita class by passing the API access token.
q = Qiita(access_token=environ["QIITA_API_ACCESS_TOKEN"])

# Create a new Qiita post (item) by calling the `create_item_with_http_info` method.
# This method not only creates the post but also returns detailed HTTP response
# information, which includes both the response data and status.
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
# res.data=Item(rendered_body='<p data-sourcepos="1:1-1:3">aaa</p>\n', body='aaa\n', coediting=False, comments_count=0, created_at='2024-10-06T03:11:04+09:00', group=None, id='e65b64d0e83e6f281a75', likes_count=0, private=True, reactions_count=0, stocks_count=0, tags=[ItemTag(name='Python', versions=[])], title='title', updated_at='2024-10-06T03:11:04+09:00', url='https://qiita.com/nanato12/private/e65b64d0e83e6f281a75', user=User(description='えんじにあ', facebook_id='', followees_count=10, followers_count=340, github_login_name='nanato12', id='nanato12', items_count=10, linkedin_id='', location='Tokyo', name='ななといつ', organization='', permanent_id=437282, profile_image_url='https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/437282/profile-images/1701305446', team_only=False, twitter_screen_name='nanato12_dev', website_url=''), page_views_count=None, team_membership=None, slide=True, organization_url_name=None)
```

## 概要

このドキュメントではQiita API v2の仕様について説明します。

## リクエスト

APIとの全ての通信にはHTTPSプロトコルを利用します。アクセス先のホストには、Qiitaのデータを利用する場合には `qiita.com` を利用し、Qiita Teamのデータを利用する場合には `*.qiita.com` を利用します ( `*` には所属しているTeamのIDが入ります)。

## パラメータ

API v2へのリクエストには、GET、POST、PUT、PATCH、DELETEの5種類のHTTPメソッドを利用します。多くのAPIへのリクエストにはパラメータを含められますが、GETリクエストにパラメータを含める場合にはURIクエリを利用し、それ以外の場合にはリクエストボディを利用します。パラメータには、ページネーション用途など任意で渡すものと、投稿時の本文など必須のものが存在します。APIドキュメントには、各APIごとに送信可能なパラメータが記載されています。

## 利用制限

認証している状態ではユーザーごとに1時間に1000回まで、認証していない状態ではIPアドレスごとに1時間に60回までリクエストを受け付けます。

## シングルサインオンを利用中のチームについて

シングルサインオンによる認証のみを許可しているQiita Teamのチームでは、セキュリティ上の理由から、チーム別アクセストークンでのみAPIを利用したアクセスが可能です。

## ステータスコード

200、201、204、400、401、403、404、500の8種類のステータスコードを利用します。GETまたはPATCHリクエストに対しては200を、POSTリクエストに対しては201を、PUTまたはDELETEリクエストに対しては204を返します。但し、エラーが起きた場合にはその他のステータスコードの中から適切なものを返します。

## データ形式

APIとのデータの送受信にはJSONを利用します。JSONをリクエストボディに含める場合、リクエストのContent-Typeヘッダにapplication/jsonを指定してください。但し、GETリクエストにバラメータを含める場合にはURIクエリを利用します。また、PUTリクエストまたはDELETEリクエストに対してはレスポンスボディが返却されません。日時を表現する場合には、[ISO 8601](http://ja.wikipedia.org/wiki/ISO_8601) 形式の文字列を利用します。

```plain
GET /api/v2/items?page=1&per_page=20 HTTP/1.1
```

## エラーレスポンス

エラーが発生した場合、エラーを表現するオブジェクトを含んだエラーレスポンスが返却されます。このオブジェクトには、エラーの内容を説明するmessageプロパティと、エラーの種類を表すtypeプロパティで構成されます。typeプロパティはエラーの種類ごとに一意な文字列で、`^[a-z0-9_]+$` というパターンで表現できます。

```plain
{
  \"message\": \"Not found\",
  \"type\": \"not_found\"
}
```

## ページネーション

一部の配列を返すAPIでは、全ての要素を一度に返すようにはなっておらず、代わりにページを指定できるようになっています。これらのAPIには、1から始まるページ番号を表すpageパラメータと、1ページあたりに含まれる要素数を表すper_pageパラメータを指定することができます。pageの初期値は1、pageの最大値は100に設定されています。また、per_pageの初期値は20、per_pageの最大値は100に設定されています。

ページを指定できるAPIでは、[Linkヘッダ](http://tools.ietf.org/html/rfc5988) を含んだレスポンスを返します。Linkヘッダには、最初のページと最後のページへのリンクに加え、存在する場合には次のページと前のページへのリンクが含まれます。個々のリンクにはそれぞれ、first、last、next、prevという値を含んだrel属性が紐付けられます。

```plain
Link: <https://qiita.com/api/v2/users?page=1>; rel=\"first\",
      <https://qiita.com/api/v2/users?page=1>; rel=\"prev\",
      <https://qiita.com/api/v2/users?page=3>; rel=\"next\",
      <https://qiita.com/api/v2/users?page=6>; rel=\"last\"
```

また、ページを指定できるAPIでは、要素の合計数が `Total-Count` レスポンスヘッダに含まれます。

```plain
Total-Count: 6
```

## JSON Schema

Qiita API v2では、APIのインターフェースを定義したJSON-Schemaを提供しています。このスキーマでは、APIでどのようなリソースが提供されているか、それらはどのようなプロパティを持っているか、それらがどのように表現されるか、及びどのような操作が提供されているかといった事柄が定義されています。スキーマには、次のURLでアクセスできます。

- <https://qiita.com/api/v2/schema>
- <https://qiita.com/api/v2/schema?locale=en>
- <https://qiita.com/api/v2/schema?locale=ja>

## Documentation for API Endpoints

All URIs are relative to *<https://qiita.com>*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TeamApi* | [**add_group_members**](docs/TeamApi.md#add_group_members) | **POST** /api/v2/groups/{url_name}/members | Add group members
*TeamApi* | [**create_comment**](docs/TeamApi.md#create_comment) | **POST** /api/v2/items/{item_id}/comments | Create comment
*TeamApi* | [**create_group**](docs/TeamApi.md#create_group) | **POST** /api/v2/groups | Create group
*TeamApi* | [**create_imported_comment**](docs/TeamApi.md#create_imported_comment) | **POST** /api/v2/items/{item_id}/imported_comments | Create imported comment
*TeamApi* | [**create_item**](docs/TeamApi.md#create_item) | **POST** /api/v2/items | Create item
*TeamApi* | [**create_item_stock**](docs/TeamApi.md#create_item_stock) | **PUT** /api/v2/items/{item_id}/stock | Create item stock
*TeamApi* | [**delete_comment**](docs/TeamApi.md#delete_comment) | **DELETE** /api/v2/comments/{comment_id} | Delete comment
*TeamApi* | [**delete_group**](docs/TeamApi.md#delete_group) | **DELETE** /api/v2/groups/{url_name} | Delete group
*TeamApi* | [**delete_group_members**](docs/TeamApi.md#delete_group_members) | **DELETE** /api/v2/groups/{url_name}/members | Delete group members
*TeamApi* | [**delete_item**](docs/TeamApi.md#delete_item) | **DELETE** /api/v2/items/{item_id} | Get item stockers
*TeamApi* | [**delete_item_stock**](docs/TeamApi.md#delete_item_stock) | **DELETE** /api/v2/items/{item_id}/stock | Delete item stock
*TeamApi* | [**get_authenticated_user**](docs/TeamApi.md#get_authenticated_user) | **GET** /api/v2/authenticated_user | Get authenticated user
*TeamApi* | [**get_authenticated_user_items**](docs/TeamApi.md#get_authenticated_user_items) | **GET** /api/v2/authenticated_user/items | Get authenticated user items
*TeamApi* | [**get_comment**](docs/TeamApi.md#get_comment) | **GET** /api/v2/comments/{comment_id} | Get comment
*TeamApi* | [**get_group**](docs/TeamApi.md#get_group) | **GET** /api/v2/groups/{url_name} | Get group
*TeamApi* | [**get_group_member**](docs/TeamApi.md#get_group_member) | **GET** /api/v2/groups/{url_name}/members/{user_id} | Get group member
*TeamApi* | [**get_group_members**](docs/TeamApi.md#get_group_members) | **GET** /api/v2/groups/{url_name}/members | Get group members
*TeamApi* | [**get_groups**](docs/TeamApi.md#get_groups) | **GET** /api/v2/groups | Get groups
*TeamApi* | [**get_item**](docs/TeamApi.md#get_item) | **GET** /api/v2/items/{item_id} | Get item
*TeamApi* | [**get_item_comments**](docs/TeamApi.md#get_item_comments) | **GET** /api/v2/items/{item_id}/comments | Get item comments
*TeamApi* | [**get_item_stockers**](docs/TeamApi.md#get_item_stockers) | **GET** /api/v2/items/{item_id}/stockers | Get item stockers
*TeamApi* | [**get_items**](docs/TeamApi.md#get_items) | **GET** /api/v2/items | Get items
*TeamApi* | [**get_oauth_team_authorize**](docs/TeamApi.md#get_oauth_team_authorize) | **GET** /api/v2/oauth/team_authorize | Get OAuth team authorize
*TeamApi* | [**is_item_stock**](docs/TeamApi.md#is_item_stock) | **GET** /api/v2/items/{item_id}/stock | Is item stock
*TeamApi* | [**update_comment**](docs/TeamApi.md#update_comment) | **PATCH** /api/v2/comments/{comment_id} | Update comment
*TeamApi* | [**update_group**](docs/TeamApi.md#update_group) | **PATCH** /api/v2/groups/{url_name} | Update group
*TeamApi* | [**update_item**](docs/TeamApi.md#update_item) | **PATCH** /api/v2/items/{item_id} | Update item
*UserApi* | [**create_comment**](docs/UserApi.md#create_comment) | **POST** /api/v2/items/{item_id}/comments | Create comment
*UserApi* | [**create_item**](docs/UserApi.md#create_item) | **POST** /api/v2/items | Create item
*UserApi* | [**create_item_like**](docs/UserApi.md#create_item_like) | **PUT** /api/v2/items/{item_id}/like | Create item like
*UserApi* | [**create_item_stock**](docs/UserApi.md#create_item_stock) | **PUT** /api/v2/items/{item_id}/stock | Create item stock
*UserApi* | [**delete_api_v2_access_tokens_access_token**](docs/UserApi.md#delete_api_v2_access_tokens_access_token) | **DELETE** /api/v2/access_tokens/{access_token} | Delete access token
*UserApi* | [**delete_comment**](docs/UserApi.md#delete_comment) | **DELETE** /api/v2/comments/{comment_id} | Delete comment
*UserApi* | [**delete_item**](docs/UserApi.md#delete_item) | **DELETE** /api/v2/items/{item_id} | Get item stockers
*UserApi* | [**delete_item_like**](docs/UserApi.md#delete_item_like) | **DELETE** /api/v2/items/{item_id}/like | Delete item like
*UserApi* | [**delete_item_stock**](docs/UserApi.md#delete_item_stock) | **DELETE** /api/v2/items/{item_id}/stock | Delete item stock
*UserApi* | [**follow**](docs/UserApi.md#follow) | **PUT** /api/v2/users/{user_id}/following | Follow
*UserApi* | [**get_authenticated_user**](docs/UserApi.md#get_authenticated_user) | **GET** /api/v2/authenticated_user | Get authenticated user
*UserApi* | [**get_authenticated_user_items**](docs/UserApi.md#get_authenticated_user_items) | **GET** /api/v2/authenticated_user/items | Get authenticated user items
*UserApi* | [**get_comment**](docs/UserApi.md#get_comment) | **GET** /api/v2/comments/{comment_id} | Get comment
*UserApi* | [**get_item**](docs/UserApi.md#get_item) | **GET** /api/v2/items/{item_id} | Get item
*UserApi* | [**get_item_comments**](docs/UserApi.md#get_item_comments) | **GET** /api/v2/items/{item_id}/comments | Get item comments
*UserApi* | [**get_item_likes**](docs/UserApi.md#get_item_likes) | **GET** /api/v2/items/{item_id}/likes | Get item likes
*UserApi* | [**get_item_stockers**](docs/UserApi.md#get_item_stockers) | **GET** /api/v2/items/{item_id}/stockers | Get item stockers
*UserApi* | [**get_items**](docs/UserApi.md#get_items) | **GET** /api/v2/items | Get items
*UserApi* | [**get_oauth_authorize**](docs/UserApi.md#get_oauth_authorize) | **GET** /api/v2/oauth/authorize | Get OAuth authorize
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /api/v2/users/{user_id} | Get user
*UserApi* | [**get_user_followees**](docs/UserApi.md#get_user_followees) | **GET** /api/v2/users/{user_id}/followees | Get user followees
*UserApi* | [**get_user_followers**](docs/UserApi.md#get_user_followers) | **GET** /api/v2/users/{user_id}/followers | Get user followers
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **GET** /api/v2/users | Get users
*UserApi* | [**is_item_like**](docs/UserApi.md#is_item_like) | **GET** /api/v2/items/{item_id}/like | Is item like
*UserApi* | [**is_item_stock**](docs/UserApi.md#is_item_stock) | **GET** /api/v2/items/{item_id}/stock | Is item stock
*UserApi* | [**is_user_following**](docs/UserApi.md#is_user_following) | **GET** /api/v2/users/{user_id}/following | Is user following
*UserApi* | [**issue_access_tokens**](docs/UserApi.md#issue_access_tokens) | **POST** /api/v2/access_tokens | Issue access token
*UserApi* | [**unfollow**](docs/UserApi.md#unfollow) | **DELETE** /api/v2/users/{user_id}/following | Unfollow
*UserApi* | [**update_comment**](docs/UserApi.md#update_comment) | **PATCH** /api/v2/comments/{comment_id} | Update comment
*UserApi* | [**update_item**](docs/UserApi.md#update_item) | **PATCH** /api/v2/items/{item_id} | Update item

## Documentation For Models

- [AddGroupMemberRequest](docs/AddGroupMemberRequest.md)
- [AuthenticatedUser](docs/AuthenticatedUser.md)
- [Comment](docs/Comment.md)
- [CreateCommentRequest](docs/CreateCommentRequest.md)
- [CreateGroupRequest](docs/CreateGroupRequest.md)
- [CreateImportedCommentRequest](docs/CreateImportedCommentRequest.md)
- [CreateItemRequest](docs/CreateItemRequest.md)
- [DeleteGroupMemberRequest](docs/DeleteGroupMemberRequest.md)
- [GetAuthenticatedUserItemsResponseInner](docs/GetAuthenticatedUserItemsResponseInner.md)
- [GetAuthenticatedUserItemsResponseInnerGroup](docs/GetAuthenticatedUserItemsResponseInnerGroup.md)
- [GetAuthenticatedUserItemsResponseInnerTagsInner](docs/GetAuthenticatedUserItemsResponseInnerTagsInner.md)
- [GetAuthenticatedUserItemsResponseInnerTeamMembership](docs/GetAuthenticatedUserItemsResponseInnerTeamMembership.md)
- [GetAuthenticatedUserItemsResponseInnerUser](docs/GetAuthenticatedUserItemsResponseInnerUser.md)
- [Group](docs/Group.md)
- [GroupMember](docs/GroupMember.md)
- [IssueAccessTokenRequest](docs/IssueAccessTokenRequest.md)
- [IssueAccessTokenResponse](docs/IssueAccessTokenResponse.md)
- [Item](docs/Item.md)
- [ItemTag](docs/ItemTag.md)
- [ItemTeamMembership](docs/ItemTeamMembership.md)
- [LikeHistory](docs/LikeHistory.md)
- [UpdateCommentRequest](docs/UpdateCommentRequest.md)
- [UpdateGroupRequest](docs/UpdateGroupRequest.md)
- [UpdateItemRequest](docs/UpdateItemRequest.md)
- [User](docs/User.md)
