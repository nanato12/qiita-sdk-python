# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered_body** | **str** | HTML形式の本文 | 
**body** | **str** | Markdown形式の本文 | 
**coediting** | **bool** | この記事が共同更新状態かどうか (Qiita Teamでのみ有効) | 
**comments_count** | **int** | この記事へのコメントの数 | 
**created_at** | **str** | データが作成された日時 | 
**group** | [**Group**](Group.md) |  | [optional] 
**id** | **str** | 記事の一意なID | 
**likes_count** | **int** | この記事への「いいね」の数（Qiitaでのみ有効） | 
**private** | **bool** | 限定共有状態かどうかを表すフラグ (Qiita Teamでは無効) | 
**reactions_count** | **int** | 絵文字リアクションの数（Qiita Teamでのみ有効） | 
**stocks_count** | **int** | この記事がストックされた数 | 
**tags** | [**List[ItemTag]**](ItemTag.md) | 記事に付いたタグ一覧 | 
**title** | **str** | 記事のタイトル | 
**updated_at** | **str** | データが最後に更新された日時 | 
**url** | **str** | 記事のURL | 
**user** | [**User**](User.md) |  | 
**page_views_count** | **int** | 閲覧数 | 
**team_membership** | [**ItemTeamMembership**](ItemTeamMembership.md) |  | [optional] 
**slide** | **bool** | スライドモードが有効を表すフラグ | 
**organization_url_name** | **str** | 記事のOrganization の url_name を表します。 | 

## Example

```python
from qiita.v2.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


