# Comment

記事やプロジェクトに付けられたコメントを表します。プロジェクトへのコメントはQiita Teamでのみ有効です。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | コメントの内容を表すMarkdown形式の文字列 | 
**created_at** | **str** | データが作成された日時 | 
**id** | **str** | コメントの一意なID | 
**rendered_body** | **str** | コメントの内容を表すHTML形式の文字列 | 
**updated_at** | **str** | データが最後に更新された日時 | 
**user** | [**User**](User.md) |  | 

## Example

```python
from qiita.v2.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


