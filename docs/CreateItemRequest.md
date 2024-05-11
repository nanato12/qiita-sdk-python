# CreateItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Markdown形式の本文 | 
**coediting** | **bool** | この記事が共同更新状態かどうか (Qiita Teamでのみ有効) | [optional] 
**group_url_name** | **str** | この投稿を公開するグループの url_name (null で全体に公開。Qiita Teamでのみ有効) | [optional] 
**private** | **bool** | 限定共有状態かどうかを表すフラグ (Qiita Teamでは無効) | [optional] 
**tags** | [**List[ItemTag]**](ItemTag.md) | 記事に付いたタグ一覧 | 
**title** | **str** | 記事のタイトル | 
**tweet** | **bool** | Twitterに投稿するかどうか (Twitter連携を有効化している場合のみ有効) | [optional] 
**organization_url_name** | **str** | 記事のOrganization の url_name を表します。 | [optional] 
**slide** | **bool** | スライドモードが有効を表すフラグ | [optional] 

## Example

```python
from qiita.v2.models.create_item_request import CreateItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateItemRequest from a JSON string
create_item_request_instance = CreateItemRequest.from_json(json)
# print the JSON string representation of the object
print(CreateItemRequest.to_json())

# convert the object into a dict
create_item_request_dict = create_item_request_instance.to_dict()
# create an instance of CreateItemRequest from a dict
create_item_request_from_dict = CreateItemRequest.from_dict(create_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


